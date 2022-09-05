from distutils.debug import DEBUG
from flask import Flask, redirect, url_for, request, render_template, session


import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')#return "Los llamo amigos,"
if __name__ == '__main__':
    app.run(DEBUG=True, PORT=5001)




@app.route('/', methods=['POST'])
def index_post():
    # Leer los valores del formulario
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']
    
    # Cargar los valores de .env
    # Load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # Indicar que queremos traducir  la versión de la API (3.0) y el idioma de destino
    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'

    # Agregar el parámetro de idioma de destino
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language

    # Crear la URL completa
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter
    
    # Configurar la información del encabezado, que incluye nuestra clave de suscripción
    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    # Crear el cuerpo de la solicitud con el texto a traducir
    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]
    
    # Hacer la llamada usando post
    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Recuperar la respuesta JSON
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Recuperar la traducción
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Plantilla de renderizado de llamadas, pasando el texto traducido,
    # Call render template, passing the translated text,
    # texto original e idioma de destino de la plantilla
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )








# app = Flask(__name__)
# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)