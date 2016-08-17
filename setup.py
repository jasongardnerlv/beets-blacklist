from setuptools import setup

setup(
    name='beets-blacklist',
    version='0.1',
    description='beets plugin to blacklist items from beets queries',
    long_description=open('README.md').read(),
    author='Jason Gardner',
    author_email='jason.gardner.lv@gmail.com',
    url='https://github.com/jasongardnerlv/beets-blacklist',
    license='MIT',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.3.7',
        'futures',
    ],
)
