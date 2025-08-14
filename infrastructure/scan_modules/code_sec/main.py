from code_sec.vars import lang_map as LM, hint_lang_map as HLM
from interfaces.cli import profile_menu, profile

target = None
fw_lang_choice = None

def start_code_security():
    print("\nSelect Project Language/Framework:")
    lang_map = LM

    for key, value in HLM.items():
        print(f"{key}) {value}")

    choice = input("Enter choice: ").strip()
    fw_lang_choice = lang_map.get(choice)

    if fw_lang_choice is not None:
        print(f"\nFramework/Language Selected: {fw_lang_choice}")
        profile_menu()

    else:
        print(f"\nError, {choice} is not supported option\n")
        return
    
    

    
def select_target():
    target = input("Enter target (IP, domain, file path, etc.): ").strip()

    print("\n[+] Running scan...")

