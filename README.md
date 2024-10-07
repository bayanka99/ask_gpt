# ask_gpt

simple app that uses openAI API to send http requests containing questions, after receiving an answer from the OpenAI API, the app saves both the question and answer in a PostgreSQL database.
both the database and the app run in a docker container.

# to run the app you need:
* Docker
* OpenAI API Key (you can get it here: https://platform.openai.com/api-keys)

after obtaining the API key you need set up an environment variable:
OPENAI_API_KEY=your_openai_api_key

# run the application:
  Run the following commands in the project directory:
  
  Build and run the application:
  
  `docker-compose up --build`

  Apply database migrations,
  After the app is running, apply the Alembic migrations to set up the database schema:

  `docker-compose exec flask_app  alembic upgrade head`

  Send requests, now you can send POST requests with JSON data containing a question, you can see an example here: src/http_request.py


