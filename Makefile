init:
	pip install -r requirements.txt

test:
	py.test -v .

coverage:
	py.test -v --cov=. --cov-report=html

