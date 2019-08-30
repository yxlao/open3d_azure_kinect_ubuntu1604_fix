import sys
import os
import platform
import ctypes
import glob

if sys.platform in {"linux", "linux2"}:
    # Must be loaded in order
    # libstdc++.so: copied from ubuntu 18.04
    # libdepthengine.so*: copied from K4A installation on ubuntu 18.04
    # libk4a.so*: build on ubuntu 16.04
    # libk4arecord.so*: build on ubuntu 16.04
    dll_files = ["libstdc++.so*", "libdepthengine.so*", "libk4a.so*", "libk4arecord.so*"]
    pwd = os.path.dirname(os.path.realpath(__file__))
    for dll_file in dll_files:
        full_paths = glob.glob(pwd + "/" + dll_file)
        if len(full_paths) != 1:
            raise RuntimeError("Not found or more than one libs found for", dll_file)
        else:
            ctypes.cdll.LoadLibrary(full_paths[0])
            print("Loaded {}".format(dll_file))
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
    pass
else:
    raise RuntimeError("Unsupported system " + sys.platform)

