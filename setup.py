from setuptools import setup

long_description = None
with open('README.md') as f:
    long_description = f.read()

setup(
    name='gita',
    packages=['gita',],
    version='0.5.6',
    description='Manage multiple git repos',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nosarthur/gita',
    keywords=['git', 'manage multiple repositories'],
    author='Dong Zhou',
    author_email='zhou.dong@gmail.com',
    license='MIT',
    entry_points={
        'console_scripts':[
            'gita = gita.__main__:main'
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        ],
    include_package_data=True,
)
