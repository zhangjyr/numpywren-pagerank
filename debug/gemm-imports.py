from numpywren.binops import gemm
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)
for mod in list(sys.modules):
    if "." not in mod and "_" not in mod:
        if mod not in sys.builtin_module_names:
            print(mod)