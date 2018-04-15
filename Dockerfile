FROM python:3-alpine

RUN mkdir -p /app/Bot
WORKDIR /app/
COPY requirements.txt main.py ./
RUN pip install -r requirements.txt && rm requirements.txt

COPY Bot ./Bot/

CMD python main.py