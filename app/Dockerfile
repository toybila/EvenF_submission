FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY ds_clicks.parquet.gzip ds_clicks.parquet.gzip
COPY ds_leads.parquet.gzip ds_leads.parquet.gzip
COPY ds_offers.parquet.gzip ds_offers.parquet.gzip

CMD ["python", "-u", "app.py"]