from __future__ import absolute_import

import os
import sys
import shutil
import tarfile
import tempfile
import subprocess
import distutils.cmd
import distutils.log

if sys.version_info[0] == 2:
    import urllib2
else:
    import urllib as urllib2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = None


if sys.version_info < (2, 7, 0):
    install_requires = ['argparse']
else:
    install_requires = []


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
        shutil.copyfileobj(response, tmp)
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
                        shutil.copyfileobj(f, f2)
        log.info("Removing the source tree...")
        shutil.rmtree(dirname)
        self.distribution.data_files.extend(self.data_files)


setup(
    name='SassPython',
    version='0.2.1',
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
    cmdclass={'build_libsass': build_libsass},
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Web Environment',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows Server 2003',
        'Operating System :: Microsoft :: Windows :: Windows Server 2008',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: Microsoft :: Windows :: Windows XP',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: BSD/OS',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: GNU Hurd',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Other',
        'Operating System :: Unix',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities'
    ]
)
