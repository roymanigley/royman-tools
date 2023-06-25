from setuptools import setup, find_packages

long_description = open('README.md', "rt").read()

setup(
    name='aaaa',
    version='0.0.1',    
    description='generated project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/roymanigley/aaaa',
    author='Roy Manigley',
    author_email='roy.manigley@gmail.com',
    license='MIT',
    packages=['aaaa'],
    install_requires=[
        'requests>=2.28.1',
        'click>=8.1.3',
    ],
    # entry_points = {
    #     'console_scripts': [
    #         'your-command = aaaa.your_module:main',
    #     ],
    # },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.10',
    ],
)
