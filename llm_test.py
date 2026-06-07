from openai import OpenAI

client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "Hello"}
        ]
    )

    print(response.choices[0].message.content)

except Exception as e:
    print("Error occurred:")
    print(e)