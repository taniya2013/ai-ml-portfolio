from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Jt1Cfe0Lfy4o273GPb5Bn-_yzGIfkvc3Nt5j0FO7tTPQ")

models = client.models.list()

for model in models:
    print(model.name)