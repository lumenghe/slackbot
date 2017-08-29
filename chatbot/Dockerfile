FROM python:3.4

WORKDIR app/

# Install required python libs
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy code from current folder to /app in container
ADD . app/

# Make port 5002/5003 available
EXPOSE 5002:5002
EXPOSE 5003:5003

#CMD python server.py --name WallE --host 0.0.0.0 --port 5002 --bot Zen ; python server.py --name HAL --host 0.0.0.0 --port 5003 --bot English


