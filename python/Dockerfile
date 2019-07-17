FROM bretttolbert/uvicorn-gunicorn-sklearn:python3.7-alpine3.8

LABEL maintainer="Brett Tolbert <bretttolbert@gmail.com>"

COPY . /code
WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

EXPOSE 8000

CMD gunicorn verbecc_svc:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0
