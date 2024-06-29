from flask import Flask, request, jsonify
from flask_cors import CORS

from openai import OpenAI
import openai

#client = OpenAI()

# Configura tu clave de API de OpenAI
#openai.api_key = 'sk-proj-OkYtn6dU4uwbgIzY0Gs2T3BlbkFJcKuz5CEccgOdkSkOc2jK'
api_key = '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'


client = openai.OpenAI(api_key=api_key)


app = Flask(__name__)
CORS(app)  # Habilitar CORS para toda la aplicación

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    description = data.get('description')

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=description,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return jsonify({'image_url': image_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/')
def index ():
    return "Iniciando"

if __name__ == '__main__':
    app.run(debug=True)