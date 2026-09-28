from google import genai

client = genai.Client(api_key="api aqui")

textos = [
    "Me encanta esta película, es increíble.",
    "Ha sido una experiencia horrible.",
    "La película dura dos horas."
]

for texto in textos:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"Clasifica como positivo, negativo o neutro este texto: {texto}"
    )

    print(response.text)