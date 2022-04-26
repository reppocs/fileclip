.PHONY: bootstrap

bootstrap:
	@pip3 install -r binaryornot
	@pip3 install -r pyperclip
	@python3 setup.py develop
