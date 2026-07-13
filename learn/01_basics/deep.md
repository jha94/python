- when we run a python file, it generates a byte code, which is mostly hidden and platform independent and which can be run on any system that has python virtual machine
- Byte code runs faster
    - .pyc file gets generated only for imported files
    - .pyc :- compiled python (frozen binaries). This .pyc is stored in __pycache__
    - hello.cpython-312.pyc
        - hello : file name
        - cpython : a python implementation, cpython is default/standard implementation of python
        - 312 : python version
        - .pyc : compiled python

- PVM : python virtual machine
    - code loop to iterate byte code
    - Run time engine
    - Also known as python interpreter

- Byte code is not machine code
    - it is python specific interpretation

