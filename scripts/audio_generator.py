import azure.cognitiveservices.speech as speechsdk

# Configurações do serviço Text-to-Speech (TTS)
SPEECH_KEY = "sua_chave_do_azure_tts_aqui"  # Insira sua chave de API do Azure Speech
SERVICE_REGION = "sua_regiao_aqui"  # Exemplo: "brazilsouth"

def gerar_audio(texto, nome_arquivo="audio_gerado.wav"):
    """Gera um arquivo de áudio a partir de um texto."""
    try:
        # Configurar o cliente de TTS
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
        audio_config = speechsdk.audio.AudioOutputConfig(filename=nome_arquivo)

        # Configurar o sintetizador de fala
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Gerar o áudio
        print(f"Gerando áudio para o texto: {texto}")
        result = speech_synthesizer.speak_text_async(texto).get()

        # Verificar status do resultado
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Áudio gerado com sucesso: {nome_arquivo}")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"A geração de áudio foi cancelada: {cancellation_details.reason}")
            if cancellation_details.error_details:
                print(f"Detalhes do erro: {cancellation_details.error_details}")

    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")

if __name__ == "__main__":
    # Texto para gerar o áudio
    texto_exemplo = "Bem-vindo ao projeto Azure OpenAI. Este é um exemplo prático de geração de áudio."
    gerar_audio(texto_exemplo)
