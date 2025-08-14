import sys
from infrastructure.scan_modules.code_sec.main import start_code_security
from config.methods import print_other_options
module = None
profile = None
result = None

main_menu_options = {
    "1": "Network Scan",
    "2": "Web Application Scan",
    "3": "Code Security Scan",
    "4": "SSL/TLS Scan",
    "5": "Container Security Scan"
}

def main_menu():
    while module is None:
        print("\n=== CyberSec Multi-Scanner ===")
        print("Select scan type:")
        print("1) Network Scan")
        print("2) Web Application Scan")
        print("3) Code Security Scan")
        print("4) Container Security Scan")
        print("5) SSL/TLS Scan")
        
        print_other_options()

        choice = input("Enter choice: ").strip()
        return choice

def profile_menu():
    while profile is None:
        print("\nSelect scan profile:")
        print("1) Quick")
        print("2) Deep")
        print("0) Default")
        print_other_options()
        choice = input("Enter choice: ").strip()
        profile_map = {
            "1": "quick",
            "2": "deep",
            "0": None
        }
        profile = profile_map.get(choice)
        if profile is None:
            print("\nInvalid choice, try again.\n")

def start_cli():
    module = main_menu()
    result = select_module(module)
    

    # results = run_scan(scan_type, target, language=language, profile=profile)

    if result:
        print("\n=== Scan Results ===")
        for tool, output in result.items():
            print(f"\n--- {tool} ---")
            print(output)

        report_file = f"scan_report_{tool}.txt"
        with open(report_file, "w") as f:
            for tool, output in result.items():
                f.write(f"\n--- {tool} ---\n")
                f.write(output)
                f.write("\n")

        print(f"\n[+] Report saved to {report_file}")


def select_module(choice):
    match choice:
        case "1":
            print("OK")
        case "2":
            print("Not Found")
        case "3":
            result = start_code_security()
        case "4":
            print("Internal Server Error")
        case "5":
            print("Internal Server Error")  
        case "0":
            sys.exit()
            print("Exiting. Goodbye!")      
        case _:
            print("Invalid choice, try again.")





if __name__ == "__main__":
    start_cli()