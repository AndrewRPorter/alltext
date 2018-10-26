FROM python:3.6-slim

RUN apt-get update && apt-get install -y gcc

COPY scripts/start.sh /start.sh

ADD requirements.txt requirements.txt

EXPOSE 5000
EXPOSE 8000
EXPOSE 443
EXPOSE 80

CMD ["./start.sh"]
