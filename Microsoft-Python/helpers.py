from pip._vendor.colorama import init, Fore


def display(content):
    print(Fore.WHITE + str(content))
