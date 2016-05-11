# To install locally: python setup.py develop
# To register: python setup.py register
# To make distribution and upload it: python setup.py sdist upload

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='thinkx',
      version='1.1',
      description='Modules supporting books by Allen Downey',
      long_description=readme(),
      url='http://github.com/AllenDowney/ThinkX',
      author='Allen Downey',
      author_email='downey@allendowney.com',
      license='MIT',
      py_modules=['thinkbayes2', 'thinkstats2', 'thinkplot', 'thinkdsp'],
      install_requires=[
          'matplotlib',
          'numpy',
          'pandas',
          'scipy',
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)
