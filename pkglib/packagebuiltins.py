from collections.abc import MutableMapping


class PackageScriptBuiltins(MutableMapping):
    
    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))


    def __len__(self):
        pass

    def __getitem__(self, key):
        print(f"[audit] attempting to use {key}")
        return self.store[key]

    def __setitem__(self, key, value):
        print(f"[audit] package tried to set builtin {key} to {value}")
        self.store[key] = value        

    def __delitem__(self, key):
        pass

    def __iter__(self):
        return iter(self.store)

    def _keytransform(self, key):
        return key


