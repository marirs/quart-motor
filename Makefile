install:
	pip install -U pip
	pip install -e .[tests,docs]

tests:
	pydocstyle quart_motor
	pytest --cov=./ --disable-warnings

codecov:
	bash <(curl -s https://codecov.io/bash) -t 06726b38-2a0d-4781-8fc1-efae09fb723c
