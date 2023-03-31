#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""lisp kernel main"""

from ipykernel.kernelapp import IPKernelApp
from .kernel import janslispkernel
IPKernelApp.launch_instance(kernel_class=janslispkernel)
