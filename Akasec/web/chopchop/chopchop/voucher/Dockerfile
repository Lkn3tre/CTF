FROM python:3.6
COPY ./app/ /app
WORKDIR /app
RUN pip install flask flask_socketio eventlet
EXPOSE 6969
ENTRYPOINT ["python", "/app/main.py"]
