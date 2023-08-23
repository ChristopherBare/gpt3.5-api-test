import openai
from dotenv import dotenv_values
env = dotenv_values(".env")
API_KEY = env.get("API_KEY")
openai.api_key = API_KEY
model_engine = "gpt-3.5-turbo"

working = True
while working:
    prompt = input()
    if prompt == "end-session":
        working = False
        break
    completion = openai.Completion.create(engine=model_engine, prompt=prompt,
                                          max_tokens=1024, n=1, stop=None,
                                          temperature=0.7)
    message = completion.choices[0].text
