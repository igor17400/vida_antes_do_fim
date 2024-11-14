# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8089

# Set the working directory to the src directory
WORKDIR /app/src

# Run the application
CMD ["gunicorn", "--config", "gunicorn_config.py", "app:server"]
