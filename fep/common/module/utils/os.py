import os

from typing import LiteralString, final


class Os:
    """Class that contains OS utils"""

    @final
    def execute_shell_command(self, cmd: LiteralString):
        """Run a shell command"""
        os.system(cmd)
