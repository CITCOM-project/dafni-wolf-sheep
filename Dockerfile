# Use the official Python 3.7 image from Dockerhub to provide a Python environment
FROM python:3.7

# Install requirements
RUN pip install mesa

# Copy the contents from the local ./src/ directory to the output container's /src/ directory
COPY ./src /src

# Tell Docker how to run the Model when it starts the container.
CMD ["python", "/src/main.py"]