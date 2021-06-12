FROM bretttolbert/uvicorn-gunicorn-sklearn:python3.8-alpine3.10

MAINTAINER "Brett Tolbert <bretttolbert@gmail.com>"

COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

EXPOSE 8000

# CMD gunicorn verbecc_svc:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0 --timeout 60 --log-level=debug --access-logfile - --error-logfile -
CMD ["uvicorn", "verbecc_svc:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]
