from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
ALPHABET = 26

class Msg(BaseModel):
    msg: str

class Encode(BaseModel):
    key: str
    message: str

class Decode(BaseModel):
    key: str
    code: str

@app.get("/")
async def root():
    return {"message": "Тодор Вълков 471221113 76гр."}

@app.post("/encode")
async def encoding(enc: Encode):
    # шифриране
    P = enc.message
    P = P.upper()
    P = P.replace(" ", "")
    pLen = len(P)

    K = enc.key
    K = K.upper()
    kLen = len(K)

    if pLen % kLen != 0:
        return "Дължината на ключа не е кратна на дължината на изречението!"
        
    result = ""
    for idx in range(0, pLen):
        asciiCode = ord(P[idx]) + ord(K[idx % kLen])
        alphabetIdx = (asciiCode - ord('A') * 2 ) % ALPHABET
        result = result + chr(ord('A') + alphabetIdx + 1) 
    return result

@app.post("/decode")
async def decoding(dec: Decode):
    # дешифриране
    P = dec.code
    P = P.upper()
    P = P.replace(" ", "")
    pLen = len(P)

    K = dec.key
    K = K.upper()
    kLen = len(K)

    if pLen % kLen != 0:
        return "Дължината на ключа не е кратна на дължината на изречението!"
        
    result = ""
    for idx in range(0, pLen):
        asciiCode = ord(P[idx]) - ord(K[idx % kLen])
        asciiCode = (asciiCode + ALPHABET) % ALPHABET
        result = result + chr(ord('A') + asciiCode - 1) 
    return result
