"""
Deuces-numpy: Numpy version of deuces package
"""

from setuptools import setup

setup(
    name='deuces_numpy',
    version='0.5',
    description=__doc__,
    long_description='descr',
    long_description_content_type='text/plain',
    author='Anatol Grabowski',
    url='https://github.com/grabantot/deuces-numpy',
    license='MIT',
    packages=['deuces_numpy'],
    install_requires=[
        'numpy',
        'scipy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment'
    ]
)
