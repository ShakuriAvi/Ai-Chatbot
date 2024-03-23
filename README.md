# Ai-Chatbot
# AIChatBot Service:

1) Clone the AIChatBot Project:
* Clone the AIChatBot project from its GitHub repository.

2) Install Dependencies:
* Run pip install -r requirements.txt to install the required dependencies.

3) Build and Start Docker Compose:
* Execute docker-compose up --build -d to build and start the Docker containers.

4) Setup MongoDB Database:
* Manually create a new MongoDB database named "AIChatBot" and a schema named "users_conversations". (It's my first time with mongo).

5) Configure AIChatBot:
* Append the content of the config.py file you received via email to the AIChatBot project. This file likely contains configurations necessary for the * correct operation of the service.

6) Run the AIChatBot Service:
* Finally, launch service.py to activate the AIChatBot service, which will be accessible through port 8080.
* (Make sure before you running this service that you set up the previous service),

With these additional steps, your AIChatBot service should now be properly configured with the settings provided in the config.py file.




# Project Details:
* My architecture in the project:
![image](https://github.com/ShakuriAvi/Ai-Chatbot/assets/65177459/a8a5615c-fbbe-4a91-b3b4-b6fa4d998616)


I handling In Two cases:
# Case 1: New User Query

1) When a new user sends a query, I call the Neural Service to retrieve relevant information.
2) Once I receive the response from the Neural Service, I use the ChatGPT API to formulate an answer to the user's query.
3) After processing the user's query and formulating the response, I store the user's query, the ChatGPT response, and the Neural Service response in MongoDB for future reference.

# Case 2: Returning User Query

1) When a returning user asks a question, I check if the last response from the Neural Service contains an answer provided by ChatGPT.
2) If there's a ChatGPT-generated answer in the last Neural Service response, I return that answer to the user.
3) If there's no ChatGPT-generated answer in the last Neural Service response, I use ChatGPT to formulate a new question and repeat the process described in Case 1.

About the handling request, I'm sure there are many use cases to handle them, I handling just in the case the Neural service doesnt have answer.
I used in strategy design patterns to init and use in the Chatgpt API and the Neural API.

If you have any question please let me know.


![image](https://github.com/ShakuriAvi/Ai-Chatbot/assets/65177459/065e09b0-b76e-47cc-8c4f-9b7527e96bd7)
![image](https://github.com/ShakuriAvi/Ai-Chatbot/assets/65177459/abaccf39-3976-4fc7-9b43-bd575203c766)

