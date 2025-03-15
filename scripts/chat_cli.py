import openai
from azure.storage.blob import BlobClient

# Configurações do Azure OpenAI e do Blob Storage
AZURE_OPENAI_API_KEY = "sua_chave_api_aqui"  # Insira sua chave de API do Azure OpenAI
AZURE_OPENAI_ENDPOINT = "sua_url_endpoint_aqui"  # Insira seu endpoint do Azure OpenAI
AZURE_BLOB_SAS_URL = "url_do_blob_com_sas_aqui"  # Insira a URL SAS do seu blob
MODEL_NAME = "text-davinci-003"  # Modelo a ser usado

# Configurar OpenAI
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_type = "azure"
openai.api_version = "2022-12-01"  # Substitua pela versão correta do seu serviço

def baixar_arquivo_blob():
    """Baixa o arquivo do Azure Blob Storage para uso no chat."""
    try:
        print("Baixando arquivo do Blob Storage...")
        blob_client = BlobClient.from_blob_url(AZURE_BLOB_SAS_URL)
        with open("arquivo_blob.txt", "wb") as arquivo:
            arquivo.write(blob_client.download_blob().readall())
        print("Arquivo baixado com sucesso: arquivo_blob.txt")
    except Exception as e:
        print(f"Erro ao baixar o arquivo do Blob Storage: {e}")

def perguntar_ao_modelo(pergunta):
    """Envia uma pergunta ao modelo Azure OpenAI e retorna a resposta."""
    try:
        print("Consultando o modelo Azure OpenAI...")
        resposta = openai.Completion.create(
            engine=MODEL_NAME,
            prompt=pergunta,
            max_tokens=150,
            temperature=0.7
        )
        return resposta.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao consultar o modelo: {e}"

def iniciar_chat():
    """Inicia o chat CLI com o Azure OpenAI."""
    print("\nIniciando chat CLI com Azure OpenAI.")
    print("Digite 'sair' para encerrar o chat.\n")
    
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Encerrando o chat. Até logo!")
            break
        
        resposta = perguntar_ao_modelo(pergunta)
        print(f"Assistente: {resposta}")

if __name__ == "__main__":
    # Baixa o arquivo do blob antes de iniciar o chat
    baixar_arquivo_blob()
    iniciar_chat()
