# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Instalacja curl i innych pakietów jako root
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app_a.py app_a.py

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENV FLASK_PORT=5001
EXPOSE ${FLASK_PORT}
ENV FLASK_APP=app_a.py
ENV FLASK_RUN_PORT=${FLASK_PORT}

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
