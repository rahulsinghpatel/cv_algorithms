#!/usr/bin/env python3
from cffi import FFI
import imp
import sys

__all__ = ["_ffi", "_libcv_algorithms"]

_ffi = FFI()

# Open native library
if sys.version_info >= (3, 4):
    import importlib
    soname = importlib.util.find_spec("cv_algorithms._cv_algorithms").origin
else:
    curmodpath = sys.modules[__name__].__path__
    soname = imp.find_module('_cv_algorithms', curmodpath)[1]

_libcv_algorithms = _ffi.dlopen(soname)