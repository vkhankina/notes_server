# Use the official image as a parent image.
FROM debian:buster-slim

RUN apt update && \
    apt install python3 python3-pip uwsgi-plugin-python3 -y && \
    mkdir /usr/src/app && \
    useradd -d /usr/src/app --system --user-group --shell /usr/sbin/nologin  uwsgi

# Copy the file from your host to your current location.
COPY requirements.txt /usr/src/app

# Run the command inside your image filesystem.
# FIX: remove temp files
RUN ls -l /usr/src/app
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8080 9191

# Copy the rest of your app's source code from your host to your image filesystem.
# FIX: do not copy .env and /venv
COPY . /usr/src/app

# Running uWSGI HTTP Router.
CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
