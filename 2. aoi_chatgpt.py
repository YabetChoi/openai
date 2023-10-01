import openai

openai.api_type = "azure"
openai.api_key = "d79f238475304db4b7247d70f88930df"
openai.api_base = "https://yb-japaneast.openai.azure.com/"
openai.api_version = "2023-05-15"

response = openai.ChatCompletion.create(
  engine="gpt-35-turbo-16k",
  messages=[
        {"role": "system", "content": "나는 관광가이드 처럼 질문에 대한 상세한 답변을 해줍니다. 예를 들어, 주요 항목에 대해서 특징과 2줄 이상의 설명을 해줍니다. 또한 대화의 시작은 인사말로 시작하고 마지막은 추가 질문이 있는 또는 권장하는 내용이 있는지 함께 알려줍니다."},
        {"role": "user", "content": "서울에서 가장 유명한 관광지 5곳을 알려주세요"}
    ],
  temperature=0.7,
  max_tokens=800,
  stop=None)

print(response['choices'][0]['message']['content'])