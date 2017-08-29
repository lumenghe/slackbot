FROM python:3.4

WORKDIR app/

# Install required python libs
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy code from current folder to /app in container
ADD . app/

