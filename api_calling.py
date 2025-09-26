client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Moderation endpoint
response = client.chat.completions.create(
    model="groq-ai",
   
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the meaning of life?"}
    ],
    tools= function_definations,
)

print(response.choices[0].message.tools_calls[0].function.arguments)

# so tools is used to define the functions which are used to call external api's, example given below
# function is a list of dictionaries


# type : function is used to define the functions which are written by the user
    function_definations = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the weather for a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                        },
                        "api_key": {
                            "type": "string",
                            "description": "The api key to use for the weather api",
                        }
                    }
                }
            }
        }
    ]





function_def = [{
    'type':'funtion',
    'function':{
        'name':"get_stationery_price",
        'description':'Get the price of stationery items',
        'parameters':{'type':'object',
        'properties':{
            'item':{'type':'string',
            'description':'The name of the stationery item'},
            'quantity':{'type':'integer',
            'description':'The quantity of the stationery item'},
            'api_key':{'type':'string',
            'description':'The api key to use for the weather api'}
         }
    }
}]