try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(name='livetest',
      version='0.1dev',
      description='Live WebTesting',
      long_description='Make live website tests look like Paste WebTest',
      author='Scott Torborg',
      author_email='storborg@mit.edu',
      url='http://github.com/storborg/livetest',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      install_requires=['WebTest'],
      test_requires=['nose>=0.11'],
      test_suite='nose.collector',
      zip_safe=False)
