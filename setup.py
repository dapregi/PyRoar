from distutils.core import setup


# Getting client version
def get_version():
    version = 'Undefined'
    init_fhand = open('pyroar/__init__.py', 'r')
    for line in init_fhand:
        if line.startswith('__version__'):
            exec(line.strip())
            break
    init_fhand.close()
    return version


# Getting long description
def get_long_description():
    with open('README.rst') as f:
        long_desc = f.read()
    return long_desc


setup_kwargs = {
    'name': 'pyroar',
    'version': get_version(),
    'description': 'Python client for PokeAPI',
    'long_description': get_long_description(),
    'author': 'Daniel Perez-Gil',
    'author_email': 'dperezgil89@gmail.com',
    'url': 'https://github.com/dapregi/pyroar',
    'packages': ['pyroar'],
    'package_dir': {'pyroar': 'pyroar'},
    'install_requires': ['pyyaml']
}

setup(**setup_kwargs)
