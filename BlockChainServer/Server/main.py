from fastapi import FastAPI
from databasFunc import get_sercet_key, get_account_details
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"]
)

@app.get("/get_secret/{key}")
def get_secret(key: str):
    print(key)
    message = get_sercet_key(key)
    return message

@app.get("/get_account_info/{account}")
def get_account(account: str):
    info = get_account_details(account)
    return info
