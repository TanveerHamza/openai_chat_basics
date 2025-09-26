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


# The answer should be this or something like this


# The distance from the Louvre to the Eiffel Tower is approximately 2 miles (about 3.2 kilometers) when driving. The actual travel distance may vary slightly depending on the route taken.
# The Arc de Triomphe is located at the western end of the Champs-Élysées in Paris, France. It stands at the Place Charles de Gaulle, which is a large junction where several major roads converge. The monument honors those who fought and died for France during the French Revolutionary and Napoleonic Wars and is one of the most famous landmarks in the city.
# The Louvre Museum is home to countless masterpieces, but some must-see artworks include:

# 1. **Mona Lisa** by Leonardo da Vinci - Perhaps the most famous painting in the world, known for its enigmatic expression.
# 2. **Venus de Milo** - An ancient Greek statue representing the goddess Aphrodite, celebrated for its beauty and artistry.
# 3. **Winged Victory of Samothrace** - A stunning Hellenistic sculpture of the goddess Nike, known for its dynamic pose and intricate
