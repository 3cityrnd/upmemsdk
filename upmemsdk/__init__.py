
import platform
import os

def getpath():

    inside_ver = 'upmem-2025.1.0-Linux-x86_64'
    dist = [
        ("debian", "10", f"debian10/{inside_ver}"),              # Debian 10 (Buster)
        ("ubuntu", "20.04", f"ubuntu-2004/{inside_ver}"),        # Ubuntu 20.04 LTS
        ("ubuntu", "22.04", f"ubuntu-2204/{inside_ver}"),        # Ubuntu 22.04 LTS
        ("rocky", "8", "rocky8"),                                # Rocky Linux
    ]

    arch = platform.machine()
    if arch != "x86_64":
        raise Exception(f"Unsupported architecture: {arch}")
 
    os_info = {}
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=", 1)
                    os_info[key] = val.strip('"')
    except FileNotFoundError:
        raise Exception(f"Can't read /etc/os-release: {arch}")

    distro_id = os_info.get("ID", "").lower()
    version_id = os_info.get("VERSION_ID", "")

    for dist_id, ver_id, subfolder in dist:
        if dist_id == distro_id and ver_id == version_id:
            folder = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.join(folder, subfolder, "upmem_env.sh")
            if os.path.isfile(fpath): 
                return fpath
            else:
                raise Exception(f"File not found {fpath}")

    raise Exception(f"Os is not supported:{dist_id} {ver_id}")
 
