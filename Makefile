all: test static run

run:
	sudo docker build -t andrew/alltext .
	sudo docker run -it -p 8000:8000 andrew/alltext

static:
	python3 manage.py collectstatic

test:
	python3 manage.py test

.PHONY: all run test zip static
