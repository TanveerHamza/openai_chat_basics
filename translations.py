client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Translate the transcript into English
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    max_completion_tokens = 100,
    messages = [ {
        "role":"user",
        "content":f"""Act as a professional transcripter of any language to English
                  Now use {transcript} with country code {country_code} and convert it into english (en)"""
    }]
)

# Extract the translated transcript text
en_transcript = response.choices[0].message.content
print(en_transcript)