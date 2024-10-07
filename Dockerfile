# use the official Python image
FROM python:3.9-slim

# set the working directory inside the container
WORKDIR /app


COPY requirements.txt .

# install the required Python packages accordting to requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code to the container
COPY . .

# set environment variables
#specify the main Flask application file
ENV FLASK_APP=main.py
# allow the server to be accessible externally
ENV FLASK_RUN_HOST=0.0.0.0

# expose the port that the app runs on
# flask's default port
EXPOSE 5000

# command to run the application
CMD ["flask", "run"]
