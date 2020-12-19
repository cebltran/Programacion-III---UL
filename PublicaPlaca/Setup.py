import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PackageTestPlacas',
    version=['1'],
    author='Cesar Beltran',
    author_email='cesarbeltran.co@gmail.com',
    description='Testea programa de placas',
    url='https://github.com/cebltran/Programacion-III---UL/tree/master/PublicaPlaca',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',    
    
    
    
)