from fep.ui import Ui

from rich.table import Table
from rich.box import SIMPLE

from modules import *

MODULES = ()

ui = Ui()

list(map(ui.add_module, MODULES))


@ui.add_command
def vars(args):
    """Display variables (syntax: `vars`)"""

    if len(args):
        yield "Usage: `vars`"
        return

    table = Table(box=SIMPLE)

    table.add_column("Name")
    table.add_column("Value")

    for k, v in ui.env.items():
        table.add_row(k, str(v))

    yield table


@ui.add_command
def help(args):
    """Display help (syntax: `help`)"""
    if len(args):
        yield "Usage: `help`"
        return

    table = Table(box=SIMPLE)

    table.add_column("Command")
    table.add_column("Description")

    for cmd in ui.commands.values():
        table.add_row(cmd.__name__, cmd.__doc__)

    yield table


@ui.add_command
def rm(args: list[str]):
    """Remove a variable from the env (syntax: `rm <name>`)"""

    match args:
        case []:
            yield "Usage: `rm <name>`"

        case [name]:
            del ui.env[name]

        case [name, *_]:
            yield f"Usage: `rm {name}`"


@ui.add_command
def run(args: list[str]):
    """Run a module (syntax: `run <module>`)"""

    match args:
        case []:
            yield "Usage: `run <module>`"

        case [name]:
            module = ui.modules.get(name)

            if module is None:
                yield f"Module `{name}` not found."
            else:
                module.execute()

        case [name, _]:
            yield f"Usage: `run {name}`"


@ui.add_command
def modules(args):
    """List all modules (syntax: `modules`)"""
    if len(args):
        yield "Usage: `module`"
        return

    table = Table(box=SIMPLE)

    table.add_column("Name")
    table.add_column("Description")
    table.add_column("Author")

    for module_name, module_instance in ui.modules.items():
        table.add_row(
            module_name, module_instance.data["desc"], module_instance.data["author"]
        )

    yield table


@ui.add_command
def set(args: list[str]):
    """Set a new variable (syntax: `set <name> <value>`"""
    match args:
        case []:
            yield "Usage: `set <name> <value>`"

        case [name]:
            yield f"Usage: `set {name} <value>`"

        case [name, value]:
            yield f"{name} <- {value}"

            ui.env[name] = value

            for instance in MODULES:
                instance.env = ui.env

                list(map(ui.add_module, MODULES))

        case [name, value, *_]:
            yield f"Usage: `set {name} {value}`"


if __name__ == "__main__":
    ui.run()
