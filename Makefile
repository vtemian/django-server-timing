full-test: test

test:
	pytest --cov=server_timing tests/

run:
	cd example && \
		python manange.py runserver

build:
	echo "No need to build someting"

lint:
	echo "TBA"

.PHONY: test full-test build lint run
