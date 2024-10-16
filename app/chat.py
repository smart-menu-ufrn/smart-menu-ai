# this file is only to the test


import openai




# Defina sua chave de API
openai.api_key = "sk-Ds4DjBinqmbiEh6ZlAgn5314E0Rq5lCSERr7FEBX-GT3BlbkFJe29i65VSJbtlCC-pmXqtFhTIngKwW1nTdfyFR_gHAA"

# Novo método para geração de texto
def gerar_texto(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Defina o modelo corretamente
        prompt=prompt,          # O prompt deve ser passado diretamente
        max_tokens=100          # Limite de tokens na resposta
    )
    return response.choices[0].text.strip()  # Ajuste para capturar o texto gerado corretamente

# Exemplo de uso
texto = gerar_texto("Escreva um poema sobre o mar.")
print(texto)




# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
#
# # Carregar o modelo e o tokenizer
# model_name = "EleutherAI/gpt-j-6B"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)
#
# # Função para gerar texto
# def gerar_texto(prompt):
#     inputs = tokenizer(prompt, return_tensors="pt")
#     outputs = model.generate(inputs.input_ids, max_length=150)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)
#
# # Exemplo de uso
# print(gerar_texto("Era uma vez em um zoológico"))
