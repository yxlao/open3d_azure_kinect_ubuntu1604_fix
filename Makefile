all:
	python setup.py bdist_wheel --dist-dir pip_package

.PHONY: clean

clean:
	rm -rf open3d_azure_kinect_ubuntu1604_fix.egg-info build pip_package
