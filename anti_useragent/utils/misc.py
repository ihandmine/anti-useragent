import sys
import subprocess


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

