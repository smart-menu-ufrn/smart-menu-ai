from typing import List
from fastapi import FastAPI
import models
import chat



api: FastAPI = FastAPI(
    title="Smart Menu AI",
)


@api.post("/receiver/items/menu")
def receiver_menu(items: List[models.MenuItem]) -> List[int]:
    # mandar para o chat
    # ele deverá organizar
    # receber e dar a resposta
    order = chat.orderToLowPrice(items)
    print(order)
    return order
