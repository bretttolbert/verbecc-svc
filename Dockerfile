FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-2025-11-17

LABEL org.opencontainers.image.authors="bretttolbert@gmail.com"

COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN apt install g++ gcc libxslt-dev
RUN pip install --upgrade pip
RUN pip install coverage snowballstemmer
RUN pip install cython==3.1.4
RUN pip install fastapi==0.121.3
RUN pip install lxml-stubs==0.5.1
RUN pip install lxml==6.0.2
RUN pip install mock==5.2.0
RUN pip install numpy==1.26.4
RUN pip install pylama==8.4.1
RUN pip install pytest-cov==4.1.0
RUN pip install pytest==7.4.4
RUN pip install requests==2.32.5
RUN pip install starlette==0.50.0
RUN pip install uvicorn==0.38.0
#RUN pip install verbecc==2.0.0
EXPOSE 8000
#CMD ["uvicorn", "verbecc_svc:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]
