from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()



setup(name='thinkx',
      version='1.0',
      description='Modules supporting books by Allen Downey',
      long_description=readme(),
      url='http://github.com/AllenDowney/ThinkX',
      author='Allen Downey',
      author_email='downey@allendowney.com',
      license='MIT',
      packages=['thinkx'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)
