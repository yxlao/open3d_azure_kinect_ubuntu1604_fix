from setuptools import setup, find_packages
import glob

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
