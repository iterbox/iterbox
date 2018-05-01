from setuptools import setup, find_packages


__version__ = None
exec(open('iterbox/version.py').read())

def readme():
    with open('README.rst') as f:
        return f.read()

config = dict(
    name='iterbox',
    version=__version__,
    packages=find_packages(exclude=['docs']),
    url='https://github.com/iterbox/iterbox',
    license='Apache License 2.0',
    author='Ilya Kisil',
    author_email='ilyakisil@gmail.com',
    description='Interactive Tensor Toolbox',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    keywords=['tensor decompositions', 'machine learning'],
    install_requires=['numpy', 'scipy'],
    include_package_data=True,
    zip_safe=False
)

setup(**config)

print("\nWelcome to ITERBOX!")
print("If any questions please visit documentation page")