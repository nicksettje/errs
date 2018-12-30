# -*- coding: utf-8 -*-
import traceback
from functools import wraps

"""Main module."""

class ErrorResult(object):
    def check(self):
        if self.is_error:
            return True
        return False

class NoError(ErrorResult):
    def __init__(self):
        self.is_error = False 

class Error(ErrorResult):
    def __init__(self, error):
        self.is_error = True 
        self.traceback = traceback.format_exc()
        self.error = error

def errs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            out = func()
            return out, NoError() 
        except Exception as e:
            err = Error(e)
            print(err.traceback)
            return args, err 
    return wrapper
