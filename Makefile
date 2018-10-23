all: test static run

run:
	python3 manage.py runserver

static:
	python3 manage.py collectstatic

test:
	python3 manage.py test

.PHONY: all run test zip static
