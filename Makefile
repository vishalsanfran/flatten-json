ACTIVATE = pipenv run

package:
	command -v pipenv || pip install pipenv
	pipenv install

test: package
	$(ACTIVATE) pytest test/