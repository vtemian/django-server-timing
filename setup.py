from setuptools import find_packages, setup

import server_timing

setup(
    name="django-server-timing",
    version=server_timing.__version__,
    author="Vlad Temian",
    author_email="vladtemian@gmail.com",
    url="http://github.com/vtemian/django-server-timing",
    description="Django middleware that integrates Server-Timing header",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
