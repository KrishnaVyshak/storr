from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()
    
setup(
    name='storr',
    version='0.1.1',
    description='A painless way to store session data',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['cryptography'],
    author='Krishnavyshak R',
    author_email='krishnavyshak.dev@gmail.com',
    keywords = [
    "secure storage",
    "session management",
    "session data",
    "encryption",
    "data security",
    "data privacy",
    "data storage",
    "data protection",
    "data access",
    "data retrieval",
    "data encryption",
    "data decryption",
    "Fernet encryption",
    "Python module",
    "PyPI",
    "session",
    "storr",
    "storing",
    "store"
],
    url='https://github.com/KrishaVyshak/storr',
)
