# just copied an old Dockerfile from WSP class

FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and Python script into the container at /usr/src/app
COPY requirements.txt ./
COPY get_pokemon.py ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "get_pokemon:app", "--host", "0.0.0.0", "--port", "8000"]

