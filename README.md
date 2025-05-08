
# TianGong AI Crews

## Env Preparing

### Setup `venv`:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Install requirements

```bash
python.exe -m pip install --upgrade pip

pip install --upgrade pip

pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

### Lock requirements
```bash
pip freeze > requirements_freeze.txt
```

### Auto lint
```bash
black .
```

### Train Agents
```bash
python -m src.crews.research.train 5 train.pkl
```

### Start Server

```bash

uvicorn src.main:app --host 0.0.0.0 --port 9770

# run in background

nohup uvicorn src.main:app --host 0.0.0.0 --port 9770 > uvicorn.log 2>&1 &
```

### Docker
```bash
docker build -t tiangong-ai-crews:latest .
docker run -d -p 9770:9770 tiangong-ai-crews:latest
```

### Tracing
In another project directory, run the following command to start OpenLIT for tracing:
```bash
git clone git@github.com:openlit/openlit.git
docker compose up -d
```

Just head over to OpenLIT at 127.0.0.1:3000 on your browser to start exploring. You can login using the default credentials

Email: user@openlit.io

Password: openlituser
