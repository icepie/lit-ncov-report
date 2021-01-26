all: build

build:
	mkdir scf
	cp -r server index.py README.md ./scf
	pip3 install -r requirements.txt -t ./scf
	zip lit-ncov-scf.zip -r ./scf