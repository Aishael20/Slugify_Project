from setuptools import setup, find_packages

setup(
    name="Slug",
    description="Un projet Python qui permet de convertir n'importe quelle chaîne de caractères en slug",
    author="Borgellas Samuel and Picard Aïshael",
    author_email='aishael.picard@gmail.com and borgellassamuel@gmail.com',
    url="https://github.com/Aishael20/Slugify_Project",
    version="0.1",
    packages=find_packages(),
    entry_points={},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
