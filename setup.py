# Copyright (C) 2018 Łukasz Langa
from setuptools import setup

setup(
    name="black",
    version="18.9b0",
    description="The uncompromising code formatter.",
    keywords="automation formatter yapf autopep8 pyfmt gofmt rustfmt",
    author="Łukasz Langa",
    author_email="lukasz@langa.pl",
    url="https://github.com/ambv/black",
    license="MIT",
    py_modules=["black", "blackd", "black_redirect"],
    packages=["blib2to3", "blib2to3.pgen2"],
    package_data={"blib2to3": ["*.txt"]},
    zip_safe=False,
    install_requires=["click>=6.5", "attrs>=18.1.0", "appdirs", "toml>=0.9.4", "procrunner"],
    extras_require={"d": ["aiohttp>=3.3.2", "aiohttp-cors"]},
    test_suite="tests.test_black",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={
        "console_scripts": [
            "black=black_redirect:patched_main",
        ]
    },
)
