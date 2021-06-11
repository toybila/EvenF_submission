FROM python:latest AS train
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app2/train.py /app/train.py
RUN python /app/train.py


FROM python:latest
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY --from=train predictions.pkl app/predictions.pkl
COPY ./app2 /app
#EXPOSE 5000
CMD python /app/main.py





