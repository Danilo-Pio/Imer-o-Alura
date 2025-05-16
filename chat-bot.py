import os
from google.genai import Client, types
from dotenv import load_dotenv # Opcional: para carregar de um arquivo .env

# --- Gerenciamento da Chave de API ---
# A forma mais segura é definir a variável de ambiente GOOGLE_API_KEY
# antes de executar o script.
# Ex: export GOOGLE_API_KEY='SUA_CHAVE_AQUI'

# Opcional: Carregar de um arquivo .env na raiz do projeto
# Certifique-se de que o arquivo .env NÃO seja adicionado ao Git (.gitignore)
# O arquivo .env conteria algo como: GOOGLE_API_KEY=SUA_CHAVE_AQUI
# load_dotenv()

# A biblioteca google-genai carregará GOOGLE_API_KEY automaticamente
# da variável de ambiente se ela estiver definida.
try:
    client = Client()
    print("Cliente da API Gemini inicializado.")
except Exception as e:
    print(f"Erro ao inicializar o cliente da API: {e}")
    print("Certifique-se de que a variável de ambiente GOOGLE_API_KEY está definida corretamente.")
    exit() # Sai do script se a chave não estiver configurada


# --- Interação com a API Gemini ---

# Listar modelos (opcional)
print("\nModelos disponíveis:")
try:
    for model in client.models.list():
      print(model.name)
except Exception as e:
    print(f"Erro ao listar modelos: {e}")


modelo = "gemini-2.0-flash"

# Exemplo de generate_content
print("\nExemplo generate_content:")
try:
    resposta = client.models.generate_content(model=modelo, contents="quem é a empresa por tras dos modelos gemini")
    print("Resposta:")
    print(resposta.text)
except Exception as e:
    print(f"Erro ao usar generate_content: {e}")


# Exemplo de chat
print("\nExemplo de chat:")
try:
    chat = client.chats.create(model=modelo)

    resposta = chat.send_message("Oi, tudo bem?")
    print("Resposta inicial do chat:")
    print(resposta.text)

    resposta = chat.send_message("voce é um assistente pessoal e voce sempre responde de forma sucinta. oque é inteligencia artificial ?")
    print("Resposta sobre IA:")
    print(resposta.text)
except Exception as e:
    print(f"Erro durante a interação do chat: {e}")


# Exemplo de chat com system_instruction
print("\nExemplo de chat com system_instruction:")
try:
    chat_config = types.GenerateContentConfig(system_instruction="voce é um assistente pessoal e voce sempre responde de forma sucinta.")
    chat_com_config = client.chats.create(model=modelo, config=chat_config)

    resposta = chat_com_config.send_message("oque é computação quntica?")
    print("Resposta sobre computação quântica:")
    print(resposta.text)

    # Obter histórico do chat (opcional)
    print("\nHistórico do chat:")
    print(chat_com_config.get_history())
except Exception as e:
    print(f"Erro durante o chat com system_instruction: {e}")


# Loop de interação com o usuário (opcional)
print("\nIniciando loop de perguntas (digite 'fim' para sair):")
try:
    prompt = input("esperando pergunta: ")

    while prompt != "fim":
      resposta = chat_com_config.send_message(prompt)
      print("resposta:", resposta.text)
      prompt = input("esperando pergunta: ")
except Exception as e:
    print(f"Erro durante o loop de interação: {e}")

print("\nFim do script.")
