
# TianGong AI Crews

## Env Preparing

Setup `venv`:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```bash
python.exe -m pip install --upgrade pip

pip install --upgrade pip

pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

Lock requirements:
```bash
pip freeze > requirements_freeze.txt
```

Auto lint:
```bash
pip install black
black .
```

Train Agents:
```bash
python -m src.crews.research.train 5 train.pkl
```

Start Server:

```bash

uvicorn src.main:app --host 0.0.0.0 --port 9770

# run in background

nohup uvicorn src.main:app --host 0.0.0.0 --port 9770 > uvicorn.log 2>&1 &
```
