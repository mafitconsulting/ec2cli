from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='ec2cli',
    version='1.0.0',
    description='ec2 instance instrumetation for AWS cells',
    long_description=readme,
    author='Mark Fieldhouse',
    author_email='Mark.Fieldhouse@mafitconsulting.co.uk',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ec2cli=ec2tool.ec2cli:main',
        ]
    }
)
