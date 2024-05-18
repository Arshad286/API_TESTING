# Citation Extraction API

This project is a Flask API that fetches data from a given API endpoint and extracts citations based on the response content.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Introduction

The Citation Extraction API fetches data from a paginated API endpoint, identifies whether the response for each response-sources pair came from any of the sources, and lists down the sources from which the response was formed. It returns an empty array if the response did not come from any source.

## Features

- Fetch data from a paginated API.
- Identify citations for each response.
- Return citations in a structured format.

## Requirements

- Python 3.x
- Flask
- Requests library

## Create a virtual environment and activate it:
- python -m venv venv
- source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
- 
## install the required Python packages:

- pip install Flask requests

## Running the API
- Ensure you're in the project root directory and activate your virtual environment.
- Run the Flask server:
- python app.py
- The API will be available at http://127.0.0.1:5000/get_citations.

## API Endpoints
- GET /get_citations
- Fetches data from the API endpoint and returns a list of citations.

## Response Format
Success (200 OK): Returns a JSON array of citations.
Example response:

json
Copy code
[
  [
    {
      "id": "71",
      "link": "https://orders.brikoven.com"
    },
    {
      "id": "8",
      "link": "https://www.brikoven.com/reservations"
    }
  ],
  []
]


### Explanation

- **Introduction**: Brief overview of what the API does.
- **Features**: List of main features of the API.
- **Requirements**: Dependencies required to run the project.
- **Setup**: Step-by-step instructions to set up the project.
- **Running the API**: Instructions to run the Flask server.
- **API Endpoints**: Description of the available API endpoints and the response format.

This `README.md` file should provide clear instructions on how to set up and run your Citation Extraction API project. Make sure to update the repository URL and other specific details as needed.








## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/arshad286/API_TESTING.git
   cd citation-extraction-api
