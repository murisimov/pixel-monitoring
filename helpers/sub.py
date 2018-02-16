import sys
import subprocess
from subprocess import PIPE, CalledProcessError, TimeoutExpired


def s(string):
    if isinstance(string, (bytes, bytearray)):
        return string.decode('utf-8')
    else:
        return str(string)


def sub(command):
    assert isinstance(command, list)

    try:
        result = subprocess.run(command, stdout=PIPE, stderr=PIPE, check=True)

    except CalledProcessError as e:
        print("Subprocess returned an error:")
        print(e)

    except TimeoutExpired as e:
        print("Subprocess timed out.")
        print(e)
        
    else:
        return s(result.stdout)
