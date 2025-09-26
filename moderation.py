# The same we did in the ai astrolabe PROJECT red teaming. It is to check the moderation of the LLM prompt and 
# to check if the LLM is being used to generate bad content, harmful or otherwise inappropriate content.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Moderation endpoint
response = client.moderations.create(
    model="text-moderation-latest",
    input="My favorite book is To Kill a Mockingbird."
)

# Print the category scores
print(response.results[0].category_scores)

# The output will be:

# CategoryScores(harassment=5.208459697314538e-06, harassment_threatening=1.152930508396821e-06, hate=4.802220792043954e-05, hate_threatening=3.197100895135918e-08, illicit=None, illicit_violent=None, self_harm=9.755882501849555e-07, self_harm_instructions=5.577317097049672e-08, self_harm_intent=1.6099545518954983e-07, sexual=3.548413360476843e-06, sexual_minors=1.1231519465582096e-06, violence=0.0001063624004018493, violence_graphic=1.1045777682738844e-05, self-harm=9.755882501849555e-07, sexual/minors=1.1231519465582096e-06, hate/threatening=3.197100895135918e-08, violence/graphic=1.1045777682738844e-05, self-harm/intent=1.6099545518954983e-07, self-harm/instructions=5.577317097049672e-08, harassment/threatening=1.152930508396821e-06)