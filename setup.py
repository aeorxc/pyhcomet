import setuptools

setuptools.setup(
    name="pyhcomet",
    version="0.0.6",
    author="aeorxc",
    description="Wrapper around Haverly HComet",
    url="https://github.com/aeorxc/pyhcomet",
    project_urls={
        "Source": "https://github.com/aeorxc/pyhcomet",
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "requests", "cachetools"],
    python_requires=">=3.8",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
