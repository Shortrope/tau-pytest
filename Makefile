run: venv/bin/activate
	./venv/bin/python ./app.py
	

test: venv/bin/activate
	./venv/bin/python -m pytest


venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt

	
clean:
	rm -rf __pycache__
	rm -rf venv