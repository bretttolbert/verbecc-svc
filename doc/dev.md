# Verbecc-svc Development

### Build verbecc-svc image

```bash
docker build -t bretttolbert/verbecc-svc .
docker tag bretttolbert/verbecc-svc:latest bretttolbert/verbecc-svc:2.0.0
```

### Run verbecc-svc image
```bash
docker run -it -p 8000:8000 --name verbecc_svc bretttolbert/verbecc-svc:2.0.0
```

### Run verbecc-svc image with source repo mappings and install from source
Optional: Comment out the `RUN pip install verbecc==` line in the Dockerfile
```bash
docker run -it -p 8000:8000 --name verbecc_svc -v $(pwd):/code/verbecc_svc -v /home/$(whoami)/Git/verbecc/verbecc:/code/verbecc bretttolbert/verbecc-svc /bin/bash
pip install ./verbecc
pip install ./verbecc_svc
cd verbecc_svc
uvicorn verbecc_svc:app --host 0.0.0.0 --reload --port 8000
```

### Exec into running verbecc-svc container
```bash
docker exec -it verbecc_svc /bin/bash
```

### Start previously stopped verbecc-svc container
```bash
docker start verbecc_svc
```

### Stop and remove verbecc-svc container
```bash
docker stop verbecc_svc
docker rm verbecc_svc
```

### Misc commands
```bash
docker run -it --name verbecc_svc -v $(pwd):/app bretttolbert/verbecc-svc /bin/bash
docker run -it --name verbecc_svc -v $(pwd):/app tiangolo/uvicorn-gunicorn-fastapi:python3.11-2025-11-17 /bin/bash
```
