full-test: test

test:
	pytest --cov-report term-missing --cov=payu --create-db tests/

run:
	cd example && \
		python manange.py runserver

build:
	echo "No need to build someting"

lint:
	echo "TBA"

.PHONY: test full-test build lint run
