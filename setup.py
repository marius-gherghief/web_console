from os.path import join, dirname
from setuptools import setup, find_packages

__version__ = open(join(dirname(__file__), 'web_console/VERSION')).read().strip()

install_requires = (
    'requests>=2.4.0',
    'websocket-client>=0.22.0',
    'slacker>=0.9.50',
    'six>=1.10.0',
    'paramiko>=2.1.1',
    'pyOpenSSL>=17.5.0',
    'cryptography>=2.1.4'
)  # yapf: disable

excludes = (
    '*test*',
    '*local_settings*',
)  # yapf: disable

setup(name='web-console',
      version=__version__,
      license='GPL-3.0',
      description='A local ssh - chat bot for Slack',
      author='Marius Gherghief',
      author_email='marius.gherghief@gmail.com',
      url='https://github.com/symmetry-apps/web_console.git',
      platforms=['Any'],
      packages=find_packages(exclude=excludes),
      install_requires=install_requires,
      scripts=['web_console/app.py'],
      classifiers=['Development Status :: 0.1.1 - Beta',
                   'License :: GNU General Public License v3.0',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'])
