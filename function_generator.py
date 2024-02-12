from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a python function generator.  When requesting a function only return the code with docstrings in the function but nothing else."
    },
    {
      "role": "user",
      "content": "Create a merge sort function."
    },
  ],
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Print the content of the response
print(response.choices[0].message.content)
