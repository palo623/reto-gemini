from google import genai
 
client = genai.Client(api_key="Api aquí")
 
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Hola. Responde únicamente: Conexión correcta."
)
 
print(response.text)