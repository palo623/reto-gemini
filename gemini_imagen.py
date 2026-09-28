from google import genai
from PIL import Image

client = genai.Client(api_key="Api aqui")

imagen = Image.open("imagen.webp")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        "Describe esta imagen en detalle",
        imagen
    ]
)

print(response.text)