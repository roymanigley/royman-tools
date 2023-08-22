from setuptools import setup, find_packages

long_description = open('README.md', "rt").read()

setup(
    name='royman_tools',
    version='0.0.2',
    description='A collection of tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/roymanigley/royman-tools',
    author='Roy Manigley',
    author_email='roy.manigley@gmail.com',
    license='MIT',
    packages=['royman_tools'],
    install_requires=[
        'click>=8.1.3',
    ],
    entry_points = {
        'console_scripts': [
            'royman-tools:create-project = royman_tools.project_creator:main',
        ],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.10',
    ],
)
