from google import genai

client = genai.Client(
    api_key="Api aquí"
)

modelos = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-3.5-flash",
    "gemini-3.6-flash"
]

for modelo in modelos:
    try:
        response = client.models.generate_content(
            model=modelo,
            contents="Di hola"
        )
        print(f"[OK] {modelo}")
        print(response.text)
        break

    except Exception as e:
        print(f"[ERROR] {modelo}")
        print(e)