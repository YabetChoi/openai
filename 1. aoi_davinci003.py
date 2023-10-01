import openai

openai.api_type = "azure"
openai.api_key = "3f64fb01b20b4d04bea2ffabe52ea494"
openai.api_base = "https://aoi-yb1.openai.azure.com/"
openai.api_version = "2023-05-15"


prompt = 'GPT-4와 GPT-3.5의 차이점을 알려줘'
response = openai.Completion.create(
    engine="text-davinci-003", 
    prompt=prompt,
    temperature=0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response['choices'][0]['text'])