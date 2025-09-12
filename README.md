DOCUMENTATION IS INCOMPLETE

Project keywords: Python FastApi, JavaScript, Machine Learning, OpenAI API, Python ChatterBot

ABOUT THE APP

A browser-based machine learning application where the user can train a ChatterBot-based chatbot 
(https://pypi.org/project/ChatterBot/) using prompts, files, and artificial intelligence. In this example, the bot is trained to answer only historical questions. The backend of the application is built with Python's FastApi framework, and the frontend is built with Vanilla JavaScript and HTML.
AI features are built using JavaScript and the OpenAI REST API.

ENTERING TRAINING DATA TO THE BOT

The application offers several ways to input training data into the bot. The methods are described below.

ENTERING DATA BY GIVING FILE PATH AND NAME

The frontend has an HTML input field where the user can enter the path and filename of the file containing the training data. Currently, it only accepts .txt files.
The text is read from the file using Python's Open and read methods, and then passed to Chatterbot's ListTrainer method. ListTrainer stores the data in an SQLite database.

ENTERING DATA FROM A UPLOADED FILE

The user can select a file using the file selection dialog. Once the file is selected, the file is loaded into the application's root directory and the data is read from the file. After reading, the data is passed to the Chatterbot using the ListTrainer method. The upload is done using the HTML input type=file attribute and the FastApi uploadFile class.

ENTERING DATA RETRIEVED FROM REST API

The application has integration with Api-Ninja's historical events API. The user can retrieve training data from the API by selecting a topic from the HTML select component and entering a date to retrieve historical events. The retrieved data is passed to the chatterbot using the ListTrainer method. Communication between the API and the application is done using the JavaScript fetch method.

Creating training data using AI

The application has integration with the OpenAI GPT REST API. Communication between the application and the GPT API is done using the JavaScript Fetch method. Rest-Api question-answer pairs are limited to historical events only using the content property, which is given the value: "create short history question with answer"