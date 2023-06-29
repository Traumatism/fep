import random

from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.shortcuts import prompt

from rich.console import Console
from rich.console import ConsoleRenderable

from typing import Callable, Generator, Any

from fep.common.module import Module
from fep import VERSION

BANNERS = [
    """
[green][bright]
  [white]_[/]__
[white].'[/]  _|[white].--[/]---[white].--[/]---.
|   _||  -__|  _  |
|_[bright_black]_|[/]  |___[bright_black]__[/]|   _[bright_black]_|[/]  [red]finir en prison[/]
            |_[bright_black]_|[/]     [white]version %(version)s[/]

[/][/]
    """,
    """
[bold bright_white]
      [bright_black] ___[/]       [bright_black] ___[/]       [bright_black] __   [/]
[bright_black]  .'|[/]=[bright_black]|_.'[/] [bright_black]  .'|[/]=[bright_black]|_.'[/] [bright_black]  .'|[/]=[bright_black]|  |  [/]
[bright_black].'  |[/] [bright_black] ___[/] [bright_black].'  |[/] [bright_black] ___[/] [bright_black].'  |[/] [bright_black]|  |  [/]
[bright_black]|   |[/]=[bright_black]|_.'[/] [bright_black]|   |[/]=[bright_black]|_.'[/] [bright_black]|   |[/]=[bright_black]|.'   [/]
[bright_black]|   |[/]      [bright_black]|   |[/] [bright_black] ___[/] [bright_black]|   |[/]
[bright_black]|___|[/]      [bright_black]|___|[/]=[bright_black]|_.'[/] [bright_black]|___|[/]

[red]finir en prison[/] (%(version)s)
[/]
    """,
]


Command = Callable[[list[str]], Generator[ConsoleRenderable, None, None]]
"""A command is a function that takes a list of strings
(command arguments) as parameters and that yields messages
to log (renderable by the Rich module)."""


class Ui:
    """Command line user interface"""

    def __init__(self) -> None:
        self.console = Console()

        self.modules: dict[str, Module] = {}
        self.commands: dict[str, Command] = {}

        self.completer = NestedCompleter.from_nested_dict(
            {command: None for command in self.commands.keys()}
        )

        self.env: dict[str, Any] = {"__console": self.console}

    def add_module(self, instance: Module):
        """Add a new module"""
        self.modules[instance.data["name"]] = instance

    def add_command(self, command: Command):
        """Decorator for adding new commands"""
        self.commands[command.__name__] = command

        self.completer = NestedCompleter.from_nested_dict(
            {command: None for command in self.commands.keys()}
        )

    def handle_cmd_with_args(self, cmd: str, args: list[str]):
        """Handle a command with arguments"""

        if (command := self.commands.get(cmd)) is None:
            self.console.log(f"Command `{cmd}` not found.")
            return

        for obj in command(args):
            if isinstance(obj, str):
                self.console.print(f"[cyan][*][/] {obj}")
                continue

            self.console.print(obj)

    def run(self):
        """Run the UI"""
        self.console.print(random.choice(BANNERS) % {"version": VERSION})

        dct = dict.fromkeys(self.commands.keys())
        dct["run"] = dict.fromkeys(self.modules.keys())

        self.completer = NestedCompleter.from_nested_dict(dct)

        while True:
            try:
                user_input = prompt("(fep) ", completer=self.completer)
            except:
                break

            match user_input.split():
                case []:
                    """User pressed enter, lol"""
                    continue

                case [cmd]:
                    """User supplied only a command without
                    arguments. (i.e. exploit)"""
                    self.handle_cmd_with_args(cmd, [])

                case [cmd, *args]:
                    """User supplied a command with multiple
                    arguments. (i.e. exploit --run)"""
                    self.handle_cmd_with_args(cmd, args)
