from openai import OpenAI

client = OpenAI(api_key="your key")

def gpt(text):
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [ # setting roles
            {"role": "system", "content": "you are an assistant bot"},
            {"role": "user", "content": f"{text}"}
        ],
        temperature = 0.5 # randomness
    )
    return_text = completion.choices[0].message.content

    return return_text