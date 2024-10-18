# this file is only to the test

from openai import OpenAI

base_url = "https://api.aimlapi.com/v1"
api_key = "bfaa01c84dc1432482b30a8dd137d1c9"

system_prompt = "You must receiver json with many items of menu, filter and order to low prices and give me."


api = OpenAI(api_key=api_key, base_url=base_url)


def orderToLowPrice(json):
    user_prompt = json

    completion = api.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content

    print(response)

    return response
    # print("User:", user_prompt)
    # print("AI:", response)


# test
# orderToLowPrice("""[
#   {
#     "id": 3,
#     "name": "empada",
#     "description": "feito de massa de trigo e frango desfiado ao molho",
#     "price": 12.4,
#     "category": "lanche"
#   },
#   {
#     "id": 7,
#     "name": "chocolate",
#     "description": "chocolate",
#     "price": 11.9,
#     "category": "doce"
#   },
#   {
#     "id": 2,
#     "name": "churrasco de carne",
#     "description": "100g de carne bovina coxão mole",
#     "price": 4.5,
#     "category": "pestico"
#   },
#   {
#     "id": 19,
#     "name": "Heineken",
#     "description": "cerveja de 600ml",
#     "price": 10.0,
#     "category": "bebida"
#   }
#
# ]""")
