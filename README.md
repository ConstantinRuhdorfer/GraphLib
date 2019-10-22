# Welcome

This is a simple graph class implementation modeld after https://github.com/DanielWochnik/CombOptWS2018.
The input files also come from this repo.

# A note on versions

Version 1.0.0 of this repo just contains the graph data structure which does not implement any of the algorithms presented in the class CombOpt.
It is released as a pip package and as a source code archieve.
Use this when you want to use the datastructure for the class because you - like me - can't work with the c++ template.

# Project structure

The relevant folders are:

```
.
+-- graph_lib/            All relevant classes are here
|   +-- graph.py
|   +-- edge.py
|   +-- vertex.py
+-- input/                Some sample input files are here
+-- test/                 All unittests are here
```

# How to use

You can either use this library by installing it as a pip package or you can just modify this code for your own use.

## Package

When using the package you can't add methods to the classes directly.
Keep this in mind if you want to implement algorithms that work with the graph data structure.
The advantage is that installing this as a package keeps your project folder tidy.

Download the files from the release section.
Then run:

```sh
pip3 install --upgrade pip
pip3 install graph_lib_constantin_ruhdorfer-1.0.0-py3-none-any.whl
```

You can verify that it works by installing the package into a sample project like (assumes Unix-like shell):

```sh
mkdir my_project
cd my_project
python3 -m venv venv
source venv/bin/activate
(venv) pip3 install --upgrade pip
(venv) pip3 install graph_lib_constantin_ruhdorfer-1.0.0-py3-none-any.whl
(venv) touch test.py
```

Put this in `test.py`:

```python
import graph_lib

print(graph_lib.name)
```

Then:

```sh
$ (venv) python3 test.py
graph_lib
```

## Source Code

Just fork this project or download the source code from the release section.

# Why?

Because I can't write c++ and the original template was in c++.
