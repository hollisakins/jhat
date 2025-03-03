from setuptools import setup
import os,glob,warnings,sys,fnmatch,subprocess
from setuptools.command.test import test as TestCommand
from distutils.core import setup
import numpy


if sys.version_info < (3,0):
    sys.exit('Sorry, Python 2 is not supported')

class jhattest(TestCommand):

   def run_tests(self):
       import jhat
       errno = jhat.test()
       jhat.test_jhat()
       sys.exit(errno)

AUTHOR = 'Armin Rest & Justin Pierel'
AUTHOR_EMAIL = 'arest@stsci.edu'
VERSION = '0.2.3'
LICENSE = ''
URL = ''



def recursive_glob(basedir, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(basedir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

PACKAGENAME='jhat'


# Add the project-global data
data_files = []
for dataFolderName in ['[]']:
  pkgdatadir = os.path.join(PACKAGENAME, dataFolderName)
  data_files.extend(recursive_glob(pkgdatadir, '*'))

data_files = [f[len(PACKAGENAME)+1:] for f in data_files]


setup(
    name=PACKAGENAME,
    cmdclass={'test': jhattest},
    packages=['bin',PACKAGENAME],
    scripts=['bin/run_st_wcs_align.py','bin/run_st_wcs_align_batch.py'],
    setup_requires=['numpy'],
    install_requires=['argparse', 'numpy', 'matplotlib', 'astropy', 'jwst', 'scipy', 
                        'photutils', 'pysiaf', 'astroquery', 'pandas>=1.5', 'stsci.skypac',
                         'tweakreg_hack','tweakwcs>=0.8','pytest-astropy'],
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    include_dirs=numpy.get_include(),
    package_data={PACKAGENAME:data_files},
    include_package_data=True
)

