from setuptools import setup

with open("requirements.txt") as rq:
    requirements = rq.read().split('\n')

setup(
    name='Ceaser_cipher',
    version='0.0.2',
    author='data_engineers2',
    packages=['Ceaser_cipher'],
    # license='LICENSE.txt',
    description='Package that cipher or decipher text using ceaser cipher',
    # long_description=open('README.txt').read(),
    install_requires=[requirements],
)
