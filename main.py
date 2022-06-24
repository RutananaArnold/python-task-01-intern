from fastapi import FastAPI, HTTPException
from typing import List
from models import User, SendMoney

app = FastAPI()

db: List[User] = [
    User(
        id=1,
        name="Arnold",
        balance=0
    ),
    User(
        id=2,
        name="Rutanana",
        balance=0
    ),
]


@app.get('/api/user')
async def fetch():
    return db


@app.put('/api/user/topup/{user_id}')
async def topup(sendMoney: SendMoney, user_id: int):
    for client in db:
        if client.id == user_id:
            if sendMoney.balance is not None:
                client.balance = client.balance + sendMoney.balance
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )


@app.put('/api/user/withdraw/{user_id}')
async def withdraw(sendMoney: SendMoney, user_id: int):
    for user in db:
        if user.id == user_id:
            if sendMoney.balance <= user.balance:
                user.balance = user.balance - sendMoney.balance
            else:
                return "Insuffient funds"    
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.post('/api/user/send/{sender_id}/{receiveruser_id}')
async def sendAmount(sendMoney: SendMoney, sender_id: int, receiveruser_id: int):
    pass