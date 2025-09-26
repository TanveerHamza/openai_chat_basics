client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Complete a request identify the country code from the transcript
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role":"user", "content":f"""identify the language of the following text and respond in the (en for english, fr for French) country code.  :{transcript}"""}],
    max_completion_tokens = 5 
    
)
# Extract the country code from the response
country_code = response.choices[0].message.content
print(country_code)