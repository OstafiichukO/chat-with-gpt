- Use human experts to engineer prompts and audit responses for potential errors and biases
- Make a backup of important data before running AI-generated update queries
- Ensure that private and sensitive information is anonymized or excluded from the data used by the model
- Make sure to follow any relevant corporate rules or policies for sharing code and data with third parties


#Uses of AI for SQL

AI has many uses in SQL, including:

- generating queries
- brainstorming ideas
- explaining code
- debugging code


#Privacy and Security with AI

The data we feed into an AI model may be used to train future iterations of the model, or stored in some other way, which can result in data leaks where our information becomes part of the publicly available large language model. This poses privacy and security risks if the data is sensitive or confidential.


#Conversational Prompting

Instead of writing one large detailed prompt, it is often more effective to interact with an AI system using a conversational approach, adding details as necessary and asking for refinements to build our analytics step by step.

By using a conversational approach, we:

Avoid repeating the same information in multiple prompts.
Save time crafting overly detailed prompts.
Build the habit of reflecting and iterating on the AI output.
Here are some different types of prompts we might write during a conversation:

Explain the goal (I’m working on an analytics report about electric vehicles)
Provide context (I have three tables with the following names)
State your request clearly (Write a query to determine the most efficient vehicle)
Review and refine (Can you explain this piece of the query you generated:)
Continuing the conversation (That’s great, what other types of statistics should I look into for this report?)


#Hallucination in AI

Hallucination is when an AI model generates outputs that are not based on real data but rather are fabricated by the model itself.

For example, an AI model might generate code using syntax that doesn’t actually exist.


#Confirmation Bias and AI

As human beings, we are psychologically prone to believing new things that confirm our existing beliefs, known as confirmation bias. If we run code provided by an AI and it produces a result that “makes sense”, we are less likely to catch errors in the AI code.

We need to be very stringent with ourselves when using AI generated code, double-checking everything the AI has done for validity. Note that we can’t use AI to do these checks, as that is using the same flawed system to check itself.