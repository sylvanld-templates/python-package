import re

PACKAGE_NAME_PATTERN = re.compile("^[a-z\-_]+$")


def input_package_name():
    print('new input')
    package_name = ""
    while len(package_name) == 0 or not PACKAGE_NAME_PATTERN.match(package_name):
        package_name = input("package name: ")
    return package_name


def input_package_description():
    description = input("package description: ")
    description = description[0].upper() + description[1:]
    if description[-1] != ".":
        description += "."
    return description


environment = {
    "package_name": input_package_name(),
    "package_description": input_package_description(),
    "package_version": "0.0.0"
}
