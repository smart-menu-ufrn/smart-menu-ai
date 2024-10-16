from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: int
    category: str

api: FastAPI = FastAPI(
    title="Smart Menu AI",
)


@api.post("/receiver/items/menu")
def receiver_menu(items: List[MenuItem]) -> List[int]:
    # mandar para o chat
    # ele deverá organizar
    # receber e dar a resposta
    return json
