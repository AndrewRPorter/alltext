FROM python:3.6-slim

ENV PROJECT=alltext
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

WORKDIR $CONTAINER_PROJECT

COPY . $CONTAINER_PROJECT

COPY start.sh /start.sh
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 8000

CMD ["/start.sh"]
