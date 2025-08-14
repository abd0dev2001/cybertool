from interfaces.cli import start_cli
from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

def print_tool_banner():
    f = Figlet(font='slant')
    banner_text = f.renderText("CYBER")
    print(f"{Fore.GREEN}{banner_text}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_tool_banner()
    start_cli()

