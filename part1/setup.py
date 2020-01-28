from setuptools import setup, find_packages


setup(
    name='python-exercise',
    version='1.4.0',
    description='Simple python project for recruitment',
    maintainer='https://github.com/ModusCreateOrg',
    license='MIT',
    url='https://github.com/ModusCreateOrg/python-exercise',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires = [
    ],
    entry_points={
        'console_script': [
            'python-exercise = python_exercise.__main__:main'
        ]
    }
)
