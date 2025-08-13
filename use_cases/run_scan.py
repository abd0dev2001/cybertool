from typing import Dict, Optional
from domain.scan_result import ScanFinding, ScanResult
from infrastructure.scan_tools.network import run_nmap
from use_cases.select_tools import select_tools

def scanner_runner(tool_id: str, target: str, context: dict) -> ScanResult:
    """
    Routes execution to the right infrastructure adapter based on tool_id.
    """
    if tool_id == "nmap":
        return run_nmap(target)

    # TODO: Add more tool adapters here (e.g., bandit, nikto...)

    # fallback simulated result for unknown tools
    dummy_result = ScanResult.new(target=target, scan_type=context.get("scan_type", "unknown"))
    dummy_result.add_finding(ScanFinding.create("info", f"simulated:{tool_id}", f"Simulated run for {tool_id}", tool=tool_id))
    dummy_result.finish()
    return dummy_result


def run_scan(scan_type: str, target: str, language: Optional[str] = None, profile: Optional[str] = None) -> Dict[str, str]:
    """
    Selects tools based on scan_type, language and profile, then runs them via scanner_runner.
    Returns a dict mapping tool_id to human-readable summary string.
    """
    tools = select_tools(scan_type, language=language, profile=profile) or []

    results = {}
    for tool_id in tools:
        scan_result = scanner_runner(tool_id, target, {"scan_type": scan_type, "language": language})
        if scan_result.findings:
            summary_lines = [f"{f.severity.upper()}: {f.title} @ {f.location or 'n/a'}" for f in scan_result.findings]
            results[tool_id] = "\n".join(summary_lines)
        else:
            results[tool_id] = "No findings"
    return results

