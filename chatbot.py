import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key = api_key
)

user_question = input("Enter your question")

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": "hey\n"
      },
      {
        "role": "assistant",
        "content": "Hey there! How can I help you today?"
      },
      {
        "role": "user",
        "content": "what color is your pen\n"
      },
      {
        "role": "assistant",
        "content": "I don’t actually have a physical pen, but if I had to pick a color I’d go with a classic, reliable blue—like the ink that’s been a favorite for typing and writing for ages. Blue feels professional, easy on the eyes, and is a staple in many offices and classrooms. If you’re looking for a different vibe, feel free to tell me what kind of pen or color you’re thinking about!"
      },
      {
        "role": "user",
        "content": user_question
      }
    ],
    temperature=1,
    max_completion_tokens=1000,

)

print(completion.choices[0].message.content)