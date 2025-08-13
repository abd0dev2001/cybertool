from use_cases.run_scan import run_scan

def main_menu():
    print("\n=== CyberSec Multi-Scanner ===")
    print("Select scan type:")
    print("1) Network Scan")
    print("2) Web Application Scan")
    print("3) Code Security Scan")
    print("4) Container Security Scan")
    print("5) SSL/TLS Scan")
    print("0) Exit")

    choice = input("Enter choice: ").strip()
    return choice

def code_security_menu():
    print("\nSelect Project Language/Framework:")
    print("1) Python")
    print("2) JavaScript/Node.js")
    print("3) Java")
    print("4) Go")
    print("5) PHP")
    print("6) Ruby")
    print("7) C/C++")
    print("8) Multiple Languages")

    lang_map = {
        "1": "python",
        "2": "javascript",
        "3": "java",
        "4": "go",
        "5": "php",
        "6": "ruby",
        "7": "cpp",
        "8": "multi"
    }

    choice = input("Enter choice: ").strip()
    return lang_map.get(choice)

def profile_menu():
    print("\nSelect scan profile:")
    print("1) Quick")
    print("2) Deep")
    print("0) Default")

    choice = input("Enter choice: ").strip()
    profile_map = {
        "1": "quick",
        "2": "deep",
        "0": None
    }
    return profile_map.get(choice)

def start_cli():
    while True:
        choice = main_menu()

        if choice == "0":
            print("Exiting. Goodbye!")
            break

        scan_type_map = {
            "1": "network",
            "2": "webapp",
            "3": "code",
            "4": "container",
            "5": "ssl"
        }

        scan_type = scan_type_map.get(choice)
        if not scan_type:
            print("Invalid choice, try again.")
            continue

        target = input("Enter target (IP, domain, file path, etc.): ").strip()

        language = None
        if scan_type == "code":
            language = code_security_menu()
            if not language:
                print("Invalid language choice.")
                continue

        profile = profile_menu()

        print("\n[+] Running scan...")
        results = run_scan(scan_type, target, language=language, profile=profile)

        print("\n=== Scan Results ===")
        for tool, output in results.items():
            print(f"\n--- {tool} ---")
            print(output)

        report_file = f"scan_report_{scan_type}.txt"
        with open(report_file, "w") as f:
            for tool, output in results.items():
                f.write(f"\n--- {tool} ---\n")
                f.write(output)
                f.write("\n")

        print(f"\n[+] Report saved to {report_file}")

if __name__ == "__main__":
    start_cli()

