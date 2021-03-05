FROM python:3.8.7-buster

# Make the WOKRDIR for your app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install dependencies
RUN pip3.8 install -r requirements.txt

EXPOSE 6060

# Run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
