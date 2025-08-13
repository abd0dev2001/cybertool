import json
from pathlib import Path
from domain.scan_result import ScanResult

REPORTS_DIR = Path(__file__).parent.parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

def generate_report(scan_result: ScanResult, format: str = "json"):
    if format == "json":
        file_path = REPORTS_DIR / f"{scan_result.scan_type}_{scan_result.target}.json"
        with open(file_path, "w") as f:
            json.dump(scan_result.__dict__, f, default=lambda o: o.__dict__, indent=4)
        print(f"[+] JSON report saved to {file_path}")
    elif format == "txt":
        file_path = REPORTS_DIR / f"{scan_result.scan_type}_{scan_result.target}.txt"
        with open(file_path, "w") as f:
            f.write(f"Scan Type: {scan_result.scan_type}\n")
            f.write(f"Target: {scan_result.target}\n\n")
            for finding in scan_result.findings:
                f.write(f"- [{finding.severity}] {finding.description} (Tool: {finding.tool})\n")
        print(f"[+] TXT report saved to {file_path}")
    else:
        raise ValueError("Unsupported format")
