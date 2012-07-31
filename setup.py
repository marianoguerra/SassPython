from __future__ import absolute_import

from distutils.core import setup


try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = None


setup(
    name='SassPython',
    version='0.1.0',
    py_modules=['sass'],
    package_dir={'': 'src'},
    package_data={'': ['README.rst']},
    description='binding for libsass',
    long_description=readme,
    license='MIT License',
    author='Mariano Guerra',
    author_email='luismarianoguerra' '@' 'gmail.com',
    url='https://github.com/marianoguerra/SassPython'
)
