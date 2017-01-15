.DEFAULT_GOAL := test

prefix ?= /usr

VIRTUAL_ENV ?= env
PY = $(VIRTUAL_ENV)/bin/python
PIP = $(VIRTUAL_ENV)/bin/pip
PHOTONIZER = $(VIRTUAL_ENV)/bin/photonizer
PYTEST = $(VIRTUAL_ENV)/bin/pytest
BOTTLE_PY = $(VIRTUAL_ENV)/bin/bottle.py


$(PY):
	python3 -m venv $(VIRTUAL_ENV)


$(BOTTLE_PY): $(PY)
	$(PIP) install -r requirements.txt


$(PYTEST): $(PY)
	$(PIP) install -r requirements-tests.txt


$(PHOTONIZER): $(PY) $(BOTTLE_PY)
	$(PY) setup.py develop


.PHONY: venv
venv: $(PY) $(BOTTLE_PY)


.PHONY: develop
develop: $(PHOTONIZER)


.PHONY: test
test: $(PHOTONIZER) $(PYTEST)
	$(PYTEST) --cov=photonizer --cov-report term --cov-report html tests/ $(ARGS)


.PHONY: dist
dist: test
	$(PY) setup.py sdist


.PHONY: install
install: venv
	$(PY) setup.py install --prefix="$(prefix)" --root="$(DESTDIR)" --optimize=1


.PHONY: clean
clean:
	find * -path $(VIRTUAL_ENV) -prune -o -type d -name __pycache__ | grep __pycache__ | xargs rm -rf
	rm -rf .tox *.egg dist build .coverage MANIFEST
