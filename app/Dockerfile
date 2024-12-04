# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /Project

# Copy the application code to the container
COPY . /Project

# Expose the application's port
EXPOSE 5000

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the app
CMD ["python", "app.py"]
