FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14

MAINTAINER "Brett Tolbert <bretttolbert@gmail.com>"

COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN apk add --update --no-cache g++ gcc gfortran libxslt-dev openblas-dev
RUN pip install coverage snowballstemmer
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "verbecc_svc:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]
