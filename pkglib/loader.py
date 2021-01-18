import os, types, sys
from importlib.machinery import ModuleSpec
import importlib.util

from . import packagebuiltins

class PkgFinder():
    """ Class to find modules from package repo """

    def __init__(self):
        pass
    
    @classmethod
    def find_spec(cls,fullname, path, target=None):
        if fullname.find("packages") == 0:
            return importlib.util.spec_from_loader(fullname, PkgLoader())    


class PkgLoader():
    audit_enable = False

    @staticmethod
    def audit_hook(event, args):
        if PkgLoader.audit_enable:
            print(event, args)


    def is_package(self, fullname):
        if fullname == "packages":
            return True
        return False

    def get_code(self, fullname):
        if fullname == "packages":
            return None
        if fullname.find("packages.") == 0:
            f = open(os.path.join('./repo', fullname[9:], "package"), 'r')
            code = f.read()
            f.close()
            return code

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        code = self.get_code(module.__name__)
        if code is None:
            return
        builts = packagebuiltins.PackageScriptBuiltins(__builtins__)
        module.__dict__["__builtins__"] = builts
        PkgLoader.audit_enable = True
        exec(code, module.__dict__)
        PkgLoader.audit_enable = False



sys.addaudithook(PkgLoader.audit_hook)
