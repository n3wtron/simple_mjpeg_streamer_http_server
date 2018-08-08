from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='simple_mjpeg_streamer_http_server',
    version='1.0.0',
    description='Simple python mjpeg streamer http server',
    url='https://github.com/n3wtron/simple_mjpeg_streamer_http_server',
    author='Igor Maculan',
    author_email='n3wtron@gmail.com',
    classifiers=[
        'Environment :: Web Environment'
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia :: Video :: Capture'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='mjpg stream http server',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['opencv-python','pillow'],
    project_urls={
        'Bug Reports': 'https://github.com/n3wtron/simple_mjpeg_streamer_http_server/issues',
        'Source': 'https://github.com/n3wtron/simple_mjpeg_streamer_http_server',
    },
)