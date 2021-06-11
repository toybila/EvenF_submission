# Even_challenge
To run this assignment, please have docker-compose installed on your machine.

Clone the github repository https://github.com/toybila/Even_challenge.

In the directory where the files are downloaded to, run the bash script startbuild.sh, which runs the docker-
compose.yml file

Manually, if preferred, the commands to do this individually are:

docker-compose up -d --build db

docker-compose up -d --build app

docker-compose up -d --build trainer

Once, all the containers are running the API endpoints will be available on

http://127.0.0.1:5000/predict_api for the single offer inference and

http://127.0.0.1:5000/predict_multiple_api for multiple offers.

Please refer to the file request.py and batchrequest.py for the sample JSON formatting for the API
calls.

The endpoints can be tested with these files or with postman or any other api testing
software.

At the background the Docker file does the following: it spins up a postgresql server and also writes files
into it using python, the Dockerfile waits for the database to be healthy before attempting to write.
All the files for these is included in the github repository.
Once the database is setup, the training file is executed which trains the model using logistic regression
and then finally deploys the FlaskAPI server.

Please note from a Data Science perspective:

The assignment insists on using Logistic regression on the set features above and gives a probability of
click for each offer. This has not allowed the candidate to explore other algorithms that might be able to
better differentiate the classes. To properly optimize the Logistic regression metrics, it will be essential to
understand what the business case will be. Accuracy is not a good measure in this case because of the
imbalanced dataset and based on the business case we can adjust the threshold of the Logistic
regression to affect the precision, recall and F1 score. To handle the imbalance in the dataset, we used
an up sampling approach.
