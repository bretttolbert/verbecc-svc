FROM python:3.6-slim

MAINTAINER Brett Tolbert "bretttolbert@gmail.com"

COPY . /code
WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

CMD ["python", "./code/verb_conjugate_fr/run.py"]
ENTRYPOINT ["python", "./verb_conjugate_fr/run.py"]
