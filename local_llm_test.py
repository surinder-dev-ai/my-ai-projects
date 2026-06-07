from ollama import chat

response = chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': 'How much max salary can person expect if he has skill set of Java Springboot kafka git python Ollama microservice docker'
        }
    ]
)

print(response['message']['content'])