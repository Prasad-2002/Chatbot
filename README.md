# Chatbot

An idea to develop a chatbot which can take input as speech and give output as speech to text.

The graphical user interface (GUI) for a chatbot is implemented in this code using the Tkinter package. The OpenAI ChatGPT model is used by the chatbot to provide responses in response to user input.
Let's step-by-step through the code:

The required libraries are imported, such as Tkinter for the GUI, threading to run the chat in a separate thread, speech_recognition to capture speech input, openai to access the ChatGPT model, os for environment variables, pyttsx3 to convert text to speech, and sqlite3 to perform database operations.

The text-to-speech conversion is configured in the pyttsx3 engine.

The ChatGPT model has been set up.

The api_key variable is used to store the OpenAI API key, which is read from a file.

To run the code generate your own api from openAI key and rename the text file to(hidden_text).

To save generated responses for later use, a response cache is established.

The speak() function uses pyttsx3 to translate text to speech.


The generate_response() function is responsible for generating a response from the ChatGPT model in response to a prompt. It sends a completion request to the OpenAI API and returns the resulting response.


The transcribe_speech() function is used to record microphone speech and convert it to text using the Google Speech Recognition API.

The function start_chat_threaded() is designed to launch the chatbot in a different thread.

The start_chat() function is used to construct a Tkinter GUI and manage the chat logic. It loads the GUI window, displays the chat history, recognises user inputs using speech recognition, generates responses using the ChatGPT model, and updates the GUI with the dialogue. It also has a button to end the discussion.

The stop_chat() function terminates the chat by closing the chat thread.

The register_user() method is responsible for user registration. It saves the entered login and password to a file and then clears the input fields.

The register() function is designed to provide a registration window in which users can enter their information in order to register.

The login() function is used to generate a login window in which users can enter their login information.

The main_screen() function is designated as the program's main entry point. It uses Tkinter to construct the main screen, configures the GUI elements for login and registration, and begins the Tkinter event loop.

Finally, the programme is started by calling the main_screen() function.

This code allows users to register, login, and interact with a chatbot in a Tkinter-based GUI using speech input and text-to-speech output.


