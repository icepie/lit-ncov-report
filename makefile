init:
	pip install -r requirements.txt
clean:
	-rm -rf */__pycache__
	-rm -rf *.log
build:
	pyinstaller -F main.py
task:
	python3 task.py