from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
ALPHABET = 26

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

    # проверка дали P съдържа само букви
    for idx in range(0, pLen):
        if P[idx] < 'A' or P[idx] > 'Z':
            return "Изречението съдържа символи различни от букви!"

    # проверка дали K съдържа само букви
    for idx in range(0, kLen):
        if K[idx] < 'A' or K[idx] > 'Z':
            return "Ключът съдържа символи различни от букви!"

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
    Code = dec.code
    Code = Code.upper()
    Code = Code.replace(" ", "")
    codeLen = len(Code)

    K = dec.key
    K = K.upper()
    kLen = len(K)

    # проверка дали кодът съдържа само букви
    for idx in range(0, codeLen):
        if P[idx] < 'A' or Code[idx] > 'Z':
            return "Шифрираното изречение съдържа символи различни от букви!"

    # проверка дали K съдържа само букви
    for idx in range(0, kLen):
        if K[idx] < 'A' or K[idx] > 'Z':
            return "Ключът съдържа символи различни от букви!"

    if codeLen % kLen != 0:
        return "Дължината на ключа не е кратна на дължината на шифрираното изречение!"
        
    result = ""
    for idx in range(0, codeLen):
        division = ord(Code[idx]) - ord(K[idx % kLen])
        letterIdx = (division + ALPHABET) % ALPHABET
        result = result + chr(ord('A') + letterIdx - 1)
    return result
