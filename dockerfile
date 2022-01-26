FROM python:2.7

RUN mkdir /app/
WORDIR /app/

COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY ./src/  /app/

EXPOSE 8000
CMD python -m SimpleHTTPServer 8000