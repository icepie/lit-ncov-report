init:
	pip3 install -r requirements.txt
clean:
	-rm -rf */__pycache__
	-rm -rf *.log
build:
	pyinstaller -F main.py