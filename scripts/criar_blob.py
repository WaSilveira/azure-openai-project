from azure.storage.blob import BlobServiceClient

# Configurações do Azure Storage
connection_string = "sua_connection_string"
container_name = "seu-container"
blob_name = "dados.json"
file_path = "./blobs/dados.json"

# Criar Blob
service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = service_client.get_container_client(container_name)

with open(file_path, "rb") as file:
    container_client.upload_blob(name=blob_name, data=file, overwrite=True)

print(f"Blob '{blob_name}' enviado com sucesso para o contêiner '{container_name}'.")
