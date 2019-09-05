from setuptools import setup, find_packages
import glob

setup(
    author='Open3D Team',
    description=[
        "Quick fix for using Azure Kinect SDK with Open3D on Ubuntu 16.04"
    ],
    include_package_data=True,
    license="MIT",
    name="open3d_azure_kinect_ubuntu1604_fix", # On PyPI
    packages=['open3d_azure_kinect_ubuntu1604_fix'], # Actual package
    url="https://github.com/yxlao/open3d_azure_kinect_ubuntu1604_fix",
    project_urls={
        'Source code': 'https://github.com/yxlao/open3d_azure_kinect_ubuntu1604_fix',
    },
    version='0.2',
)
