from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

# DEMO ONLY DOES DEMO DATA
with open('demo-persona.json', "r") as file:
    data = json.load(file)

tags = data["tags"]
output_string = ', '.join(f'{tag["name"]}: {tag["value"]} ({tag["confidence"]*100:.0f}%)' for tag in tags)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will only be given tags about someones face with a yes or no value. Based on these values, give 5 compliments and 5 roasts, format these in 2 lists, not markdown. Do not add extra text. The roasts must be mean and the compliments must be nice."
    },
    {
      "role": "user",
      "content": output_string
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

response_content = response.choices[0].message.content
print(response_content)