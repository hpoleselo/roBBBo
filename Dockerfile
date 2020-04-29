# Para dar build no docker: sudo docker build . -t robbbo
FROM python:3.6-slim

COPY src/subscriber_bot.py /home/src/
COPY src/talker_bot.py /home/src/
COPY src/face_detection.py /home/src/
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# Adicionar exports no .bashrc

WORKDIR /home/src
CMD ["python3.6", "subscriber_bot.py"]
