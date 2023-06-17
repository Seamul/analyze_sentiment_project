
# analyze_sentiment_project

## Django Project

This is a Django project for sentiment analysis. It aims to analyze the sentiment of textual data using natural language processing techniques.

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Installation

1. Clone the repository:

shell:
   git clone https://github.com/Seamul/analyze_sentiment_project.git
   

Create a virtual environment:

shell:
python3 -m venv env
Activate the virtual environment:

For Windows:

shell:
.\env\Scripts\activate
For macOS/Linux:

shell:
source env/bin/activate
Install project dependencies using the requirements.txt file:

shell:
pip install -r requirements.txt
Database Setup
Apply database migrations:

shell:
python manage.py migrate
(Optional) If you want to use a different database backend, update the DATABASES configuration in the project's settings.py file accordingly.

Usage
To run the Django development server, execute the following command:

shell

python manage.py runserver
The server will start running at http://localhost:8000/. Open this URL in your web browser to access the sentiment analysis project.
