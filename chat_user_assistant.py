messages = [
    {"role": "system", "content": "You are a physics teacher who provides short and helpful answers."},
  ]
user_questions= ["why is radian answer different from degree?","Summarize this in one sentence."]
# these questions are examples which can be asked from the user and we are training the model to answer them


# how to loop through user questions

for q in user_questions:

    user_dict = {"role":"user","content":q}
    messages.append(user_dict)

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages,
    )
    # Now using these responses we can train the model to answer the questions so we will give this to the 
    # assistant which will get trained by the answer of all the questions we trained the model on  

    assistant_dict = {
        "role":"assistant",
        "content":response.choices[0].message.content
    }
    messages.append(assistant_dict)