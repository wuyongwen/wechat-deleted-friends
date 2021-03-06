#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

import py2exe

options = {"py2exe":
                {"compressed": 1,
                 "optimize": 2,
                 "bundle_files": 1, # 表示把所有文件打包进exe可执行程序
                 # "packages": extra_modules,
                 #"includes": extra_modules
                }
          }
setup(
    version = "1.0.0",
    description = "test for py2exe",
    name = "Py2exeTest",
    options = options,
    zipfile = None,
    console = [{"script": "wdf.py"}]
)