import toml

config = toml.load(".secrets/secrets.toml")

FASTAPI_AUTH = config["FASTAPI"]["AUTH"]
FASTAPI_BEARER_TOKEN = config["FASTAPI"]["BEARER_TOKEN"]
FASTAPI_MIDDLEWARE_SECRECT_KEY = config["FASTAPI"]["MIDDLEWARE_SECRECT_KEY"]

OPENAI_API_KEY = config["OPENAI"]["API_KEY"]
OPENAI_MODEL = config["OPENAI"]["MODEL"]

TAVILY_API_KEY = config["TAVILY"]["API_KEY"]
