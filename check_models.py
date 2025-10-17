import google.generativeai as genai

# COLE SUA CHAVE DE API AQUI NOVAMENTE
API_KEY = 'AIzaSyBX2bsCxOmdczDf-HffePxv6KG3EZIhDFE' 

try:
    genai.configure(api_key=API_KEY)
    
    print("Buscando modelos disponíveis para sua chave de API...")
    print("-" * 30)

    found_model = False
    for m in genai.list_models():
      # Vamos verificar quais modelos suportam a geração de conteúdo (chat)
      if 'generateContent' in m.supported_generation_methods:
        print(f"Modelo encontrado: {m.name}")
        found_model = True

    if not found_model:
        print("Nenhum modelo compatível com 'generateContent' foi encontrado para esta chave de API.")
    
    print("-" * 30)

except Exception as e:
    print(f"Ocorreu um erro: {e}")