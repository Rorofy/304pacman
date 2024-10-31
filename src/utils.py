from genericpath import isfile


def checkFile(path: str) -> None:
    if isfile(path) is False:
        raise IOError("File not found!")


def checkArgumentFormat(arg1: str, arg2: str) -> None:
    if (len(arg1) != 1 or len(arg2) != 1) or arg1 == arg2:
        raise RuntimeError("Wrong arguments entered!")
