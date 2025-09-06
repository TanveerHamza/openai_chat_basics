import os
from openai import OpenAI

model = "gpt-4o-mini"

client = OpenAI()
sys = """Give the answer correctly as you are a tourist and you know everything. Any question other then Parisian Tourist related should be discarded and replied by 
Sleep tight nigga
"""
conversation = [
    {
        "role":"system",
        "content":"How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"
    },
    {
        "role":"user",
        "content":"what is the most famous landmark in Paris"
    },
    {
        "role":"assistant",
        "content":"The most famous landmark in paris is EIFFEL TOWER"
    
    }
]

questions = ['How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?',
'Where is the Arc de Triomphe?',
'What are the must-see artworks at the Louvre Museum?']

for q in questions:

    assistant_dict = {"role":"assistant", "content":q}
    conversation.append(assistant_dict)

    response = client.chat.completions.create(
        model= model,
        messages= conversation,
        temperature= 0.0,
        max_tokens= 100
        
    )

    resp = response.choices[0].message.content
    print(resp)

    resp_dict = {"role":"assistant","content":resp}
    conversation.append(resp_dict)



# Add as many cells as you like