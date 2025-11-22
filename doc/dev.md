# Verbecc-svc Development

### Build verbecc-svc image

```bash
docker build -t bretttolbert/verbecc-svc .
docker tag bretttolbert/verbecc-svc:latest bretttolbert/verbecc-svc:2.0.0
```

### Create docker network for proxy connection between front-end and back-end service
(`docker-compose` will do this automagically)
```bash
docker network create verbecc-proxy-network
```

### Run dockers with verbecc-proxy-network
Add this to the `docker run` commands:
```bash
--network verbecc-proxy-network
```

### Run verbecc-svc image
```bash
docker run -it --network verbecc-proxy-network -p 8000:8000 --name verbecc-svc bretttolbert/verbecc-svc:2.0.0
```

### Run verbecc-svc image with source repo mappings and install from source
Optional: Comment out the `RUN pip install verbecc==` line in the `Dockerfile`
```bash
docker run -it --network verbecc-proxy-network -p 8000:8000 --name verbecc-svc -v $(pwd):/code/verbecc_svc -v /home/$(whoami)/Git/verbecc/verbecc:/code/verbecc bretttolbert/verbecc-svc /bin/bash
pip install ./verbecc
pip install ./verbecc_svc
cd verbecc_svc
uvicorn verbecc_svc:app --host 0.0.0.0 --reload --port 8000
```

### Exec into running verbecc-svc container
```bash
docker exec -it verbecc-svc /bin/bash
```

### Start previously stopped verbecc-svc container
```bash
docker start verbecc-svc
```

### Stop and remove verbecc-svc container
```bash
docker stop verbecc-svc
docker rm verbecc-svc
```

### Misc commands
```bash
docker run -it --name verbecc-svc -v $(pwd):/app bretttolbert/verbecc-svc /bin/bash
docker run -it --name verbecc-svc -v $(pwd):/app tiangolo/uvicorn-gunicorn-fastapi:python3.11-2025-11-17 /bin/bash
```
