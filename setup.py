from setuptools import (
    find_packages,
    setup
)


setup(
    name="py-forks",
    version="1.0.0",
    description="util that retrieves a list of forks for a given github user and repo",
    url="https://github.com/critical-path/py-forks",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords="python util github forks user repo",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    extras_require={
        "test": [
            "pylint",
            "pytest",
            "pytest-cov",
            "responses"
        ]
    },
    entry_points={
        "console_scripts": [
            "forks=forks.forks_cli:get_forks"
        ]
    }
)
