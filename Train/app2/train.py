import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import pickle
import imblearn
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline



db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'host.docker.internal'
db_port = '5432'

conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(conn_string)
conn = db.connect()

if conn:
    print('connected')
else:
    conn = db.connect()

join_statement = '''SELECT requested, loan_purpose, credit, annual_income, apr, clicked_at
                    FROM leads
                    INNER JOIN offers ON offers.lead_uuid = leads.lead_uuid
                    LEFT JOIN clicks ON clicks.offer_id = offers.offer_id '''

joined_df = pd.read_sql(join_statement, conn)
joined_df['clicked_at'] = joined_df['clicked_at'].fillna(0)
joined_df.loc[(joined_df.clicked_at != 0), 'clicked_at'] = 1
joined_df['clicked_at'] = joined_df['clicked_at'].astype(int)
joined_df = joined_df.dropna().copy()

labelencoder = LabelEncoder()
joined_df['loan_purpose'] = labelencoder.fit_transform(joined_df['loan_purpose'])
joined_df['credit'] = labelencoder.fit_transform(joined_df['credit'])

# Separate input features and target
y = joined_df.clicked_at
X = joined_df.drop('clicked_at', axis=1)

# setting up testing and training sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=27)

# Handling imbalanced dataset
sm = SMOTE(sampling_strategy=1.0, random_state=27)
X_train, y_train = sm.fit_resample(X_train, y_train)

#Hyperparameterization tuning commented out on rerun
#solvers = ['newton-cg', 'lbfgs', 'liblinear']
#penalty = ['l2']
#c_values =[100, 10, 1.0, 0.1, 0.01]
#params= dict(solver=solvers, penalty=penalty, C=c_values )
#clf = RandomizedSearchCV(lr, params, n_iter = 250, cv = 5, random_state =1, n_jobs = -1)
#print(clf.best_)

lr = LogisticRegression(penalty= 'l2', C=100, solver = 'newton-cg', n_jobs= -1, max_iter= 300)

lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

pickle.dump(lr, open('predictions.pkl','wb'))
