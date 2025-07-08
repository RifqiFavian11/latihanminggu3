from fastapi import FastAPI, Header, HTTPException
import pandas as pd

# create object FastAPI
app = FastAPI()

password = "kopiluwakgakbikinkenyang123"

# membuat endpoint halaman utama -> untuk mengambil data (GET)
@app.get("/")
def getData():
    return {
        "message": "hello"
    }


@app.get("/data")
def getData():
    # 1. read csv
    df = pd.read_csv('data.csv')

    # 2. return data
    return {
        "data": df.to_dict(orient="records")
    }


@app.get("/data/{id}")
def getData(id: int, api_key: str = Header()):
    #authentication
    if api_key == None or api_key != password:
        raise HTTPException(status_code=401, detail="Failed Authentication")
    
    # 1. read csv
    df = pd.read_csv('data.csv')

    # 2. filter
    result = df[df['id'] == id]

    # 3. return data
    return {
        "data": result.to_dict(orient="records")
    }
