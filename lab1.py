import json
import platform
import sys
import os
import getpass

result = {
    "system": platform.platform(),
    "os_family": platform.system(),
    "release": platform.release(),
    "version": platform.version(),
    "processor": platform.processor(),
    "machine": platform.machine(),
    "architecture_bits": platform.architecture()[0],
    "hostname": platform.node(),
    "username": getpass.getuser(),
    "python_version": platform.python_version(),
    "interpreter_path": sys.executable,
    "cpu_count": os.cpu_count()

}
with open("result.json", "w") as f:
    json.dump(result, f, indent = 4)
