from setuptools import setup

setup(name='bec1db',
      version='0.1',
      description='The hackiest database reader ever',
      author='biswaroop',
      author_email='mail.biswaroop@gmail.com',
      license='MIT',
      packages=['bec1db'],
       install_requires=[
          'pandas',
          'sqlite3'
      ],
      zip_safe=False)
