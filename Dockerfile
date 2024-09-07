FROM tensorflow/tensorflow:2.10.0

COPY taxifare /taxifare
COPY requirements_prod.txt /requirements_prod.txt
COPY setup.py /setup.py
COPY .env /.env

RUN pip install --upgrade pip
RUN pip install -r requirements_prod.txt

CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT
