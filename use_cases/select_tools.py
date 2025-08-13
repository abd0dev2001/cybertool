import yaml
from pathlib import Path

CONFIG_DIR = Path(__file__).parent.parent / "config"

def load_yaml(filename: str):
    with open(CONFIG_DIR / filename, "r") as f:
        return yaml.safe_load(f)

def select_tools(scan_type: str, language: str = None, profile: str = None):
    settings = load_yaml("settings.yaml")
    profile = profile or settings.get("default_profile", "quick")

    profiles = load_yaml("scan_profiles.yaml")
    tools_for_profile = profiles.get(profile, {})

    # For code scans, select tools based on language mapping
    if scan_type == "code" and language:
        tool_map = load_yaml("tool_mapping.yaml")
        return tool_map.get(language.lower(), [])

    # For other scan types, use profile tools list
    return tools_for_profile.get(scan_type, [])

