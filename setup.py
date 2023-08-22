from setuptools import setup

long_description = open('README.md', "rt").read()

setup(
    name='royman_tools',
    version='0.0.3',
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
        'requests == 2.31.0',
    ],
    entry_points={
        'console_scripts': [
            'royman-tools:create-project = royman_tools.project_creator:main',
            'royman-tools:web-dir-scan = royman_tools.web:main',
            'royman-tools:tcp-port-scan = royman_tools.tcp:port_scan',
            'royman-tools:tcp-rsh = royman_tools.tcp:rsh',
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
