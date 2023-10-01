import openai

openai.api_type = "azure"
openai.api_key = "a5e4bc24b0e44a85b2bc0372529da89d"
openai.api_base = "https://yb-eastus.openai.azure.com/"
#https://yb-eastus.openai.azure.com/openai/images/generations:submit?api-version=2023-06-01-preview
openai.api_version = "2023-06-01-preview"

response = openai.Image.create(
    prompt='Smiling Statue of Liberty ',
    size='1024x1024',
    n=1
)

image_url = response["data"][0]["url"]
print(image_url)