from setuptools import setup, find_packages

setup(
    name='mixpeek',
    version='0.6.11',
    author='Ethan Steininger',
    author_email='ethan@mixpeek.com',
    description='Mixpeek Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mixpeek/mixpeek-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
