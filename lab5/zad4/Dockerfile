ARG PYTHON_VERSION=3.12-alpine
FROM python:${PYTHON_VERSION}

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
# RUN python -m pip install -r requirements.txt
RUN /usr/local/bin/python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "./app/index.py"]
EXPOSE 3000

ENV FLASK_APP=app/app.py
ENV FLASK_RUN_PORT=3000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]