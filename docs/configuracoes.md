# Configurações do Azure OpenAI Playground

## Parâmetros e Suas Funções

O Azure OpenAI Playground permite configurar diferentes parâmetros para adaptar o modelo às suas necessidades. Aqui estão os principais parâmetros usados neste projeto:

### **Temperatura**
- **Descrição:** Controla o nível de criatividade das respostas.
  - Baixo valor (ex.: 0.1-0.3): Respostas mais focadas e previsíveis.
  - Alto valor (ex.: 0.7-1.0): Respostas mais criativas e variadas.
- **Exemplo no Playground:** 
  - *Temperatura = 0.3* para gerar respostas técnicas.
  - *Temperatura = 0.8* para respostas criativas.

### **Top-P**
- **Descrição:** Controla a probabilidade cumulativa usada para limitar as respostas.
  - *Top-P = 0.1*: Restringe as opções.
  - *Top-P = 1.0*: Permite mais diversidade nas respostas.

### **Max Tokens**
- **Descrição:** Define o número máximo de tokens (palavras ou partes de palavras) que podem ser gerados na resposta.
- **Exemplo:** Configurar 100 tokens para respostas curtas.

### **Frequency Penalty**
- **Descrição:** Penaliza a repetição de palavras na resposta.
- **Range:** 0 a 2.
- **Uso:** Valores mais altos evitam redundância.

### **Presence Penalty**
- **Descrição:** Incentiva o modelo a abordar novos tópicos.
- **Range:** 0 a 2.
- **Uso:** Útil para diversificar as respostas.

## Explicação de Scripts Relacionados

### **1. criar_blob.py**
- **Função:** Faz o upload de arquivos locais para o Azure Blob Storage.
- **Configuração Necessária:**
  - Connection String da sua conta de armazenamento.
  - Nome do container e do arquivo.
- **Como Usar:**
  1. Configure sua connection string no script.
  2. Execute:
     ```bash
     python criar_blob.py
     ```

### **2. chat_cli.py**
- **Função:** Permite interagir com o Azure OpenAI via terminal (CLI).
- **Configuração Necessária:**
  - API Key e Endpoint do Azure OpenAI.
  - URL SAS do Blob Storage (para acessar dados de exemplo).
- **Como Usar:**
  1. Configure as credenciais no script.
  2. Execute:
     ```bash
     python chat_cli.py
     ```
  3. Digite perguntas no terminal e receba respostas do modelo.

### **3. audio_generator.py**
- **Função:** Gera arquivos de áudio a partir de texto usando Azure Text-to-Speech.
- **Configuração Necessária:**
  - API Key e região do serviço Azure Speech.
- **Como Usar:**
  1. Insira sua chave e região no script.
  2. Execute:
     ```bash
     python audio_generator.py
     ```
  3. O arquivo de áudio será salvo como `audio_gerado.wav`.

Esperamos que este guia ajude a configurar e usar os modelos com eficiência. Para dúvidas ou melhorias, sinta-se à vontade para contribuir.
