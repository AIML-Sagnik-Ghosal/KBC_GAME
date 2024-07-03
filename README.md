# KBC_GAME
# KBC Quiz App

## Overview
This is a Python program to create a quiz app using Flask, similar to the famous Indian show KBC (Kaun Banega Crorepati). The frontend is built using HTML, CSS, and JavaScript, while Flask is used for the backend. We fetch quiz data from the 'the-trivia-api.com' API.

## Features
- **Dynamic Quiz Generation**: The app dynamically generates quiz questions by fetching data from the 'the-trivia-api.com' API. 
- **Multiple Choice Questions**: Each question is accompanied by multiple choice options.
  - **Question Format**: Uses the `question` field from the API response.
  - **Options**: Uses the `correctAnswer` and `incorrectAnswers` fields to form the multiple-choice options.
- **User Helps**: The app provides several helps for the user, similar to the TV show:
  - **50:50**: Removes two incorrect options.
  - **Expert Advice**: Provides advice from an expert.
  - **Double Dip (2x)**: Allows two attempts to answer the question.
  - **Flip the Question (Flip)**: Changes the current question.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Requests

### Steps
1. **Clone the repository:**
    ```sh
    git clone https://github.com/AIML-Sagnik-Ghosal/KBC_GAME.git
    ```
2. **Navigate into the project directory:**
    ```sh
    cd KBC_GAME
    ```
3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To use the app, follow these steps:

1. **Run the Flask application:**
    ```sh
    python app.py
    ```
2. **Open your browser and go to `http://localhost:5000` to start the quiz.**

### Template
The template for the app can be found at [this link](https://codepen.io/21_Sagnik-Ghosal/pen/RwmzvRg).

### API Data Format
The app fetches data from 'the-trivia-api.com' API in the following format:
```json
{
  "category": "Arts & Literature",
  "id": "622a1c397cc59eab6f950eb6",
  "correctAnswer": "Charles Darwin",
  "incorrectAnswers": [
    "Percy Bysshe Shelley",
    "H. Rider Haggard",
    "Robert Louis Stevenson"
  ],
  "question": "Which author wrote 'On the Origin of Species'?",
  "tags": ["arts_and_literature"],
  "type": "Multiple Choice",
  "difficulty": "easy",
  "regions": [],
  "isNiche": false
}
```
##Question: The question field is used to form the quiz question.
##Options: The correctAnswer and incorrectAnswers fields are used to form the multiple-choice options.
###Question Example
##Question: Which author wrote 'On the Origin of Species'?
##Options:
-**Charles Darwin
-**Percy Bysshe Shelley
-**H. Rider Haggard
-**Robert Louis Stevenson
###Scope of Improvement
##Database Integration: Build a database to store user data such as name, preferences, and highest score.
##Multi-user Support: Enhance the app to handle multiple users simultaneously.
##Category and Difficulty Selection: Add another page for users to initialize categories and difficulty levels from 'the-trivia-api.com' before starting the quiz.
##Welcome Page: Create a welcome page to greet users and provide instructions or options before starting the quiz.
