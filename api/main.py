
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Req(BaseModel):
    supplier:str

@app.post('/analyze')
def analyze(req:Req):
    return {'supplier':req.supplier,'risk_score':72,'status':'HIGH'}
