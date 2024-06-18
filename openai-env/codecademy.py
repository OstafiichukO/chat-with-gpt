from openai import OpenAI  

client = OpenAI() 

def process(response):
  message = response.choices[0].message
  print(message.content, "\n")
  
  return {
    "role": message.role, 
    "content": message.content
  }

saved_messages = [{
    "role": "user", 
    "content": "Output a list of social media marketing strategies." 
}] 

response = client.chat.completions.create( 
  model="gpt-3.5-turbo", 
  messages=saved_messages
) 

# Your code below:
saved_messages.append(process(response))

# This content will change based on the previous response message
saved_messages.append({
  "role": "user", 
  "content": "Output the instructions for item 5."
})

response = client.chat.completions.create( 
  model="gpt-3.5-turbo", 
  messages=saved_messages
) 

saved_messages.append(process(response))
