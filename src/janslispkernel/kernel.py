#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""lisp kernel"""

from ipykernel.kernelbase import Kernel
from pexpect import replwrap

not_allowed = ["(quit)","(exit)"]

def code_valid(string):
    """Test for valid input to avoid kernel hang"""
    string = string.strip()
    if string != '':
        bracket = 0
        quote = 0
        sense = True
        for elem in string:
            if sense:
                if elem == '(':
                    bracket += 1
                elif elem == ')':
                    bracket -= 1
                elif elem == '"':
                    sense = False
                    bracket += 1
            else:
                if elem == '"':
                    sense = True
                    bracket -= 1
        if bracket == 0 and quote == 0 and sense:
            return True
        else:
            return False
    else:
        return False

lispwrapper = replwrap.REPLWrapper("clisp -q", "]> ", None)

class janslispkernel(Kernel):
    """kernel class hooks into the clisp repl via replwrap"""
    implementation = 'IPython'
    implementation_version = '8.12.0'
    language = 'clisp'
    language_version = '2.49.93'
    language_info = {
        'name': 'lisp',
        'mimetype': 'application/lisp',
        'file_extension': '.lisp',
    }
    banner = "Lisp kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            code = code.replace("\n"," ")
            code = code.strip()
            if code_valid(code):
                if code[0:7] in not_allowed:
                    solution = f'"{code}" is not allowed in the Lisp kernel'
                solution = lispwrapper.run_command(code)
                cut = solution.rfind("\n")
                solution = solution[:cut]
            else:
                solution = "Your input was incomplete or invalid."
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
