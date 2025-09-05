DOCUMENTATION IS INCOMPLETE

Project keywords: Python FastApi, JavaScript, Machine Learning, OpenAI API, Python ChatterBot

ABOUT THE APP

A browser-based machine learning application where the user can train a ChatterBot-based chatbot 
(https://pypi.org/project/ChatterBot/) using prompts, files, and artificial intelligence. In this example, the bot is trained to answer only historical questions. The backend of the application is built with Python's FastApi framework, and the frontend is built with Vanilla JavaScript and HTML.

AI features are implemented with the official OpenAI API Python library:
https://github.com/openai/openai-python

ENTERING TRAINING DATA TO THE BOT

The application offers several ways to input training data into the bot. The methods are described below.

ENTERING DATA BY GIVING FILE PATH AND NAME

The frontend has an HTML input field where the user can enter the path and filename of the file containing the training data. Currently, it only accepts .txt files.
The text is read from the file using Python's Open and read methods, and then passed to Chatterbot's ListTrainer method. ListTrainer stores the data in an SQLite database.


