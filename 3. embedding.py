import openai

openai.api_type = "azure"
openai.api_key = "3f64fb01b20b4d04bea2ffabe52ea494"
openai.api_base = "https://aoi-yb1.openai.azure.com/"
openai.api_version = "2023-05-15"

response = openai.Embedding.create(
    input="마이크로소프트 openAI",
    engine="text-embedding-ada-002"
)

print(response['data'][0]['embedding'])