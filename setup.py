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
        'Environment :: Web Environment',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
