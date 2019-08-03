from behave import __main__ as behave_executable


# from features.environment import *

def executar():
    behave_executable.main(' --no-capture --no-capture-stderr --stop')


executar()
