from . import add, divide, multiply, subtract

OPERATIONS = {
    '+': add.compute,
    '-': subtract.compute,
    '*': multiply.compute,
    '/': divide.compute,
}