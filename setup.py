import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='instapy-cli',
    version='0.0.1',
    description='Python library and cli used to upload photo on Instagram. W/o a phone!',
    long_description=open('README.md.rst').read(),
    classifiers=[
        # How mature is this project?
        'Development Status :: 5 - Production/Stable',

        # For who your project is intended for and its usage
        'Intended Audience :: Developers',
        'Environment :: Console',

        # Project's License
         'License :: OSI Approved :: MIT License',

        # Python versions instapy-cli support here
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='instagram private upload api instapy instapy-cli instapycli',
    author='Benedetto Abbenanti',
    author_email='benedetto.abbenanti@gmail.com',
    url='https://github.com/b3nab/instapy-cli',
    license='MIT',
    packages=['instapy_cli'],
    install_requires=[ # external packages as dependencies
        'requests>=2',
        'emoji'
    ],
    entry_points={
        'console_scripts': [
            'instapy=instapy_cli.__main__:main'
        ]
    },
    # python_requires='>=2.7'
)