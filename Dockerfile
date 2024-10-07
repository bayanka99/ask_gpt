# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set environment variables
#Specify the main Flask application file
ENV FLASK_APP=main.py
# Allow the server to be accessible externally
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port that the app runs on
# Flask's default port
EXPOSE 5000

# Command to run the application
CMD ["flask", "run"]
