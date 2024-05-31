from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure OpenAI service client 
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)

deployment="gpt-4o"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
