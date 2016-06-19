env:
	python3 -m venv --without-pip env
	wget https://bootstrap.pypa.io/ez_setup.py -O - | env/bin/python
	env/bin/easy_install pip
env/requirements_dev: env
	env/bin/pip install -r requirements_dev.txt
	touch env/requirements_dev
env/requirements: env
	env/bin/pip install -r requirements.txt
	touch env/requirements
tests: env/requirements_dev env/requirements
	env/bin/py.test src -s
app: env/requirements
	env/bin/python run.py
clean:
	rm -rf env
	rm -rf local.db
