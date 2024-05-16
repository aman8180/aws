# Use Python base image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Install AWS SDK for Python (Boto3)
RUN pip install boto3

# Copy Python script to the container
COPY data_processing.py /app/

# Command to run the Python script
CMD ["python", "data_processing.py"]