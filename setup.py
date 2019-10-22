import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graph_lib_constantin_ruhdorfer",
    version="1.0.1",
    author="Constantin Ruhdorfer",
    author_email="constantin.ruhdorfer@gmnx.de",
    description="A small library for representing graphs for the class of Combinatorial Optimization at Baden-Wuerttemberg Cooperative State University Stuttgart.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ConstantinRuhdorfer/GraphLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
