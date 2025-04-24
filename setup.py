from setuptools import setup, find_packages

setup(
    name='ec2-component',
    version='0.1.0',
    packages=find_packages(),  
    install_requires=[
        'pulumi',
        'pulumi-aws',
    ],
    python_requires='>=3.6',
)

