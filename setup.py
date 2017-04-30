from setuptools import setup


try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

try:
    with open('LICENSE') as f:
        license = f.read()
except IOError:
    license = ''

setup(
    name='slasher',
    version='0.1.0',
    description='Easily build Slack slash commands with AWS Lambda',
    long_description=readme,
    author='Alex DeBrie',
    author_email='alexdebrie1@gmail.com',
    url='https://github.com/alexdebrie/slasher',
    license=license,
    keywords=['slack', 'lambda'],
    packages=['slasher']
)
