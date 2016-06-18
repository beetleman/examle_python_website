env:
	python3 -m venv env
	env/bin/pip install -U pip
env/requirements_dev: env
	env/bin/pip install -r requirements_dev.txt
	touch env/requirements_dev
env/requirements: env
	env/bin/pip install -r requirements.txt
	touch env/requirements
tests: env/requirements_dev env/requirements
	env/bin/py.test src
app: env/requirements
	env/bin/python run.py
clean:
	rm -rf env
