import os
import requests
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Obtendo a URL do documento através dos parâmetros da requisição HTTP
        document_url = req.params.get('document_url')
        
        # Verificar se a URL foi fornecida na requisição
        if not document_url:
            return func.HttpResponse(
                "Erro: A URL do documento não foi fornecida.",
                status_code=400
            )

        # Credenciais do Azure Form Recognizer
        subscription_key = os.getenv('6TNkrdnBKBXB7M5oywTOj5T29Koaq1067CFZ5D3iw3pJd5dxnJ1gJQQJ99BDACYeBjFXJ3w3AAALACOGZYx4')
        endpoint = "https://diandressa.cognitiveservices.azure.com/"  # Substitua com o seu endpoint

        # Definindo o modelo que você usará (exemplo com o modelo de layout 'prebuilt-layout')
        model_id = "prebuilt-layout"  # Você pode escolher o modelo apropriado, como prebuilt-invoice, etc.

        # URL para chamar o Azure Form Recognizer
        url = f"{endpoint}/formrecognizer/v2.1-preview.3/layout/analyze"

        # Cabeçalhos necessários para autenticação
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key
        }

        # Dados enviados para a API (contém a URL do documento)
        data
