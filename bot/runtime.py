import sys
import platform
import disnake
from datetime import datetime
import time

class RuntimeInfo():
    def __init__(self):
        self.python_version = platform.python_version()
        self.disnake_version = disnake.__version__
        self.os_name = platform.system()
        self.architecture = platform.machine()

        self.startup_time = datetime.now()
        self.startup_timestamp = time.monotonic()

    @property
    def uptime(self):
        return time.monotonic() - self.startup_timestamp
