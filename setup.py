from __future__ import absolute_import

import distutils.cmd
import distutils.log
import os
import os.path
import subprocess
import shutil
import tarfile
import tempfile
import urllib2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = None


def copy(source, destination):
    while 1:
        chunk = source.read(4096)
        if chunk:
            destination.write(chunk)
        else:
            break


class build_libsass(distutils.cmd.Command):
    """Download the source tarball of libsass and then build it."""

    description = __doc__
    libsass_url = 'https://github.com/hcatlin/libsass/tarball/master'
    user_options = [
        ('url=', None, 'url of the source tarball to download [default: %s]'
                       % libsass_url)
    ]
    suffixes = ('.so', '.dylib')
    data_files = set()

    if os.path.isdir('build'):
        for _name in os.listdir('build'):
            if _name.endswith(suffixes):
                data_files.add(os.path.join('build', _name))

    def initialize_options(self):
        self.url = self.libsass_url

    def finalize_options(self):
        pass

    def run(self):
        log = distutils.log
        self.distribution.has_ext_modules = lambda: True # fake
        if self.data_files:
            log.info('Built libsass already exists')
            return
        log.info("Downloading the libsass source tarball...")
        log.info(self.url)
        response = urllib2.urlopen(self.url)
        tmp = tempfile.TemporaryFile()
        copy(response, tmp)
        log.info("Extracting libsass source tarball...")
        response.close()
        tmp.seek(0)
        tar = tarfile.open(fileobj=tmp)
        dirname = tar.getnames()[0]
        tar.extractall('.')
        tmp.close()
        log.info("Getting configured libsass...")
        subprocess.call(['./configure', '--enable-shared'], cwd=dirname)
        log.info("Building libsass...")
        subprocess.call(['make'], cwd=dirname)
        log.info("Copying libsass shared objects...")
        build_dir = os.path.join(dirname, '.libs')
        if not os.path.isdir('build'):
            os.mkdir('build')
        for filename in os.listdir(build_dir):
            if filename.endswith(self.suffixes):
                with open(os.path.join(build_dir, filename), 'rb') as f:
                    dst_name = os.path.join('build', filename)
                    self.data_files.add(dst_name)
                    with open(dst_name, 'wb') as f2:
                        copy(f, f2)
        log.info("Removing the source tree...")
        shutil.rmtree(dirname)
        self.distribution.data_files.extend(self.data_files)


setup(
    name='SassPython',
    py_modules=['sass'],
    package_dir={'': 'src'},
    data_files=[
        ('', ['README.rst'] + list(build_libsass.data_files))
    ],
    zip_safe=False,
    description='binding for libsass',
    long_description=readme,
    license='MIT License',
    author='Mariano Guerra',
    author_email='luismarianoguerra' '@' 'gmail.com',
    url='https://github.com/marianoguerra/SassPython',
    cmdclass={'build_libsass': build_libsass}
)
