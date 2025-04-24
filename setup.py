from setuptools import setup, find_packages

setup(
    name="bfthon",
    version="1.0.0",
    author="whotfusests",
    description="Encode Python strings to Brainfuck and decode Brainfuck to Python strings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/whotfusests/bfthon",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    install_requires=[],
    keywords=["brainfuck", "encode", "decode", "python"],
)