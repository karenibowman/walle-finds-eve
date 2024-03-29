# Use an official Python runtime as a parent image
FROM python:3

ENV APP /app

# create and set the working directory to app
RUN mkdir $APP
WORKDIR $APP

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "server/app.py"]
