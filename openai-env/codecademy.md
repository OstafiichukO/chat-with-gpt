Creating a Chat by Passing Context
2 min
So far we have initiated chat completions with the model, presenting a new user prompt in each interaction. But what if we want the model to retain context from prior discussions to imitate a full real-world conversation?

We can convey historical context to the model by including our previous messages and responses in subsequent prompts. This technique is particularly beneficial when we want the model to build upon or refer back to information provided in earlier points of the conversation.

Passing the conversation context helps us not repeat portions of the conversation to re-train the model. This concept is akin to how ChatGPT works. To the user, there is an assumption that context will persist in the prompt as the conversation continues. Under the hood, the entire conversation context is essentially resubmitted with each new prompt submission.

Let’s look at an example of how to provide this historical context. Imagine we still want our model to suggest non-Caribbean destinations when prompted, and we stored our previous user and assistant message pairs in a variable called message_data:

message_data = [ 
{
  "role": "system", 
  "content": "You are a friendly travel guide excited to help users travel the Caribbean. Your responses should only include destinations that are in the Caribbean"
}, 
{
  "role": "user", 
  "content": "Suggest a destination suitable for a family with toddlers."
}, 
{
  "role": "assistant", 
  "content": "Sure! Consider visiting Aruba for a family vacation. It offers beautiful beaches, family-friendly resorts, and attractions like the Butterfly Farm and Arikok National Park that kids would enjoy."
}, 
{
  "role": "user", 
  "content": "We're looking for a Mediterranean destination with beaches. Any suggestions?"
}, 
{
  "role": "assistant", 
  "content": "While I specialize in Caribbean destinations, I am familiar with a few Mediterranean destinations with great beaches. Majorca for instance is right off the coast of Spain and has beautiful, pristine beaches."
}]

We will append our new "user" prompt to the message_data list and pass the list to the messages parameter in the chat completion method. This will pass on the previous conversational data:

message_data.append( 
{
  "role": "user", 
  "content": "Give me some destinations in Canada to travel to for good snowboarding." 
}) 

response= client.chat.completions.create( 
  model="gpt-3.5-turbo",  
  messages=message_data
) 

first_reply = response.choices[0].message.content) 

Output (Model Response):

As a travel guide focused on the Caribbean, I can't provide specific information about Canadian destinations for snowboarding. However, some popular destinations in Canada for snowboarding include Whistler Blackcomb in British Columbia, Banff National Park in Alberta, and Mont Tremblant in Quebec. These locations are renowned for their excellent snowboarding terrain and facilities. I recommend researching these destinations further to find the one that suits you best. 

We can now take the newly generated reply and send it back to the model as an "assistant" message to continue the conversation:

message_data.append( 
  {
    "role": "assistant", 
    "content": first_reply
  } 
) 

message_data.append(
  {
    "role": "user", 
    "content": "I am only interested in western-most parts of Canada." 
  } 
) 

second_response = client.chat.completions.create( 
  model="gpt-3.5-turbo",  
  messages=message_data, 
) 

second_reply = second_response.choices[0].message.content

Output (Model Response):

If you're specifically looking for snowboarding destinations in the westernmost parts of Canada, here are a few suggestions: 

1. Whistler, British Columbia: As mentioned earlier, Whistler is renowned for its world-class slopes and is consistently ranked among the top snowboarding destinations worldwide. 

2. Cypress Mountain, British Columbia: Located just north of Vancouver, Cypress Mountain hosted events during the 2010 Winter Olympics. It offers a range of terrain suitable for all levels, including panoramic views of the city and the ocean. 

Things to keep in mind when providing conversational context:

Token limits: The more contextual information we provide in the prompt, the closer we’ll be to hitting the model’s token limit. While token limits are increasing with every new model, we may need to eventually truncate or rephrase some of the included historical data to make sure the prompt stays within the limit.

Relevance: We want to make sure we provide historical responses that are relevant to the current conversation we are having. For example, we may not want to include responses from a conversation about recommendations for classic novels in a new conversation about the history of quantum physics.

Instructions
Checkpoint 1 Passed
1.
To support passing the chat context, the list variable saved_messages has been defined and initialized to the first prompt.

There is also a helper function process() that takes the chat response as an argument and does the following:

Outputs the content
Returns a dictionary with the "role" and "content" from the chat response.
You will use process() to add the chat responses to the saved_messages list.

The first chat completion is already set up, so when you are ready, run the code.

Checkpoint 2 Passed
2.
Now you will want to add the assistant message from response to the saved_messages list. This is where you will use the process() helper function.

Pass the chat completion response to the process() function and append the return value to saved_messages.

When you run the code, the message content should be output in the terminal.

Checkpoint 3 Passed
3.
Now append a new user prompt dictionary to saved_messages to continue the chat.

The output is potentially a list of ideas so one option is to write a prompt to explain one of the ideas. Since the previous chat is being passed, you can simply reference the number of the item in the list.

Prompt example: "Tell me more about item 2"

Checkpoint 4 Passed
4.
With the new user prompt in saved_messages, perform another chat completion using saved_massages and pass the response to process() to output the formatted chat reply.

The output should be a continuation of the conversation since you sent the context along with your new prompt.
