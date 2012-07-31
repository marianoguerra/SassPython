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
    url='https://github.com/marianoguerra/SassPython',
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
