# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Flask application code
COPY app.py /app

# Install Flask and psycopg2 (for PostgreSQL connection)
RUN pip install flask psycopg2

# Expose the backend on port 5000
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
