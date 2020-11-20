from setuptools import setup

setup(
    name='logos-server',
    version='0.2',
    packages=['logos_server'],
    url='',
    license='MIT',
    author='Elielton Kremer',
    author_email='elieltonkremer2392@gmail.com',
    description='Simple bottle wrapper to Logos',
    install_requires=[
        'bottle'
    ],
    dependency_links=[
        'https://github.com/elieltonkremer/logos.git'
    ]
)
