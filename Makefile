PACKAGE ?= photonizer
VIRTUAL_ENV ?= $(PWD)/env
PY = $(VIRTUAL_ENV)/bin/python

$(PY):
	pyvenv env
	$(eval VIRTUAL_ENV = $(PWD)/env)

build: $(PY)
	$(PY) setup.py sdist

develop: $(PY)
	$(PY) setup.py develop

deps: $(PY)
	if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi

clear:
	@echo TODO create this

bump:
	@echo "Current $(PACKAGE) version is: $(shell sed -nE "s/^__version__ = .([^']+)./\\1/p" $(PACKAGE)/__init__.py)"
	@test ! -z "$(version)" || ( echo "specify a version number: make bump version=X.X.X" && exit 1 )
	@! git status --porcelain 2> /dev/null | grep -v "^??" || ( echo 'uncommited changes. commit them first' && exit 1 )
	@echo "Bumping to $(version)"
	sed -i'.bak' -e "/^__version__ = .*$$/s/'[^']*'/'$(version)'/" $(PACKAGE)/__init__.py
	rm -f $(PACKAGE)/__init__.py.bak
	git add $(PACKAGE)/__init__.py
	git commit -m 'Bumped version number to $(version)'
	git tag $(version)
	@echo "Version $(version) commited and tagged. Don't forget to push to github."
	@echo
	@echo "git push origin master && git push origin $(version)"
