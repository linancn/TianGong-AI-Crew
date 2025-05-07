
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

Auto lint:
```bash
pip install black
black .
```

Start Server:

```bash

uvicorn src.main:app --host 0.0.0.0 --port 7770

# run in background

nohup uvicorn src.main:app --host 0.0.0.0 --port 7770 > uvicorn.log 2>&1 &
```
