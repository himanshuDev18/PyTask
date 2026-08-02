import os
import importlib

NAME = "help"
DESCRIPTION = "Show all available commands"

REQUIRED_ATTRIBUTES = (
    "NAME",
    "DESCRIPTION",
    "execute",
)

def execute(arguments):
    print("Available Commands:")

    files = os.listdir("plugins")

    for file in files:
        if not file.endswith(".py") or file == "__init__.py":
            continue

        module_name = file[:-3]
        module = importlib.import_module(f"plugins.{module_name}")

        if all(hasattr(module, attr) for attr in REQUIRED_ATTRIBUTES):
            print(f"{module.NAME:<10} - {module.DESCRIPTION}")