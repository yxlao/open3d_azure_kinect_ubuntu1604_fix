all:
	python setup.py bdist_wheel

.PHONY: clean

clean:
	rm -rf *.egg-info build pip_package
