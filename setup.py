from setuptools import setup, find_packages
import glob

# Force platform specific wheel
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    # https://stackoverflow.com/a/45150383/1255535
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    print('Warning: cannot import "wheel" package to build platform-specific wheel')
    print('Install the "wheel" package to fix this warning')
    bdist_wheel = None

cmdclass = {'bdist_wheel': bdist_wheel} if bdist_wheel is not None else dict()

setup(
    author='Open3D Team',
    description=[
        "Quick fix for using Azure Kinect SDK with Open3D on Ubuntu 16.04"
    ],
    # cmdclass=cmdclass,
    include_package_data=True,
    license="MIT",
    # Name of the package on PyPI
    name="open3d_azure_kinect_ubuntu1604_fix",
    packages=[
        'open3d_azure_kinect_ubuntu1604_fix',
    ],
    url="https://github.com/yxlao/open3d-azure-kinect-ubuntu1604-fix",
    project_urls={
        'Source code': 'https://github.com/yxlao/open3d-azure-kinect-ubuntu1604-fix',
    },
    version='0.1',
)
