import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)
prompt="Give me a one sentence story about Michael"
temperatures=[0.1,0.7]
no_loops=3

print("/n |Temperatures| Run| Response|")
print("|-----|-----|--------------|")

for temp in temperatures:
    for run in range(1,no_loops+1):
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temp
        )
        answer =response.choices[0].message.content
        print(f"|{temp}|{run}|{answer}|")