from setuptools import setup, find_packages

import server_timing


setup(
    name='django-server-timing',
    version=server_timing.__version__,
    author='Vlad Temian',
    author_email='vladtemian@gmail.com',
    url='http://github.com/vtemian/django-silver-timing',
    description='Django middleware that integrates Server-Timing header',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
