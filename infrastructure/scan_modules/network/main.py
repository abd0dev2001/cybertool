import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List
from domain.scan_result import ScanFinding, ScanResult
from domain.scan_types import ScanType
import datetime
import uuid

NMAP_BIN = "nmap"  # Assumes nmap is in PATH


def run_nmap(target: str, extra_args: List[str] = None) -> ScanResult:
    """
    Runs nmap against the target and parses XML output.
    Returns a ScanResult with ScanFindings.
    """
    extra_args = extra_args or ["-sV", "-oX", "-"]  # -sV: service/version detection, -oX -: output XML to stdout

    cmd = [NMAP_BIN] + extra_args + [target]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    xml_output = proc.stdout

    # Create ScanResult container
    result = ScanResult(
        id=str(uuid.uuid4()),
        target=target,
        scan_type=ScanType.NETWORK.value,
        started_at=datetime.datetime.utcnow().isoformat() + "Z",
        findings=[]
    )

    # Parse XML
    try:
        root = ET.fromstring(xml_output)
        for host in root.findall("host"):
            addr = None
            for addr_el in host.findall("address"):
                if addr_el.attrib.get("addrtype") == "ipv4":
                    addr = addr_el.attrib.get("addr")
            for port in host.findall(".//port"):
                portid = port.attrib.get("portid")
                state = port.find("state").attrib.get("state")
                service_el = port.find("service")
                service_name = service_el.attrib.get("name") if service_el is not None else "unknown"
                if state == "open":
                    finding = ScanFinding.create(
                        severity="medium",
                        title=f"Open port {portid} ({service_name})",
                        description=f"Port {portid} is open and running {service_name}",
                        location=f"{addr}:{portid}",
                        tool="nmap",
                    )
                    result.add_finding(finding)
    except Exception as e:
        finding = ScanFinding.create(
            severity="error",
            title="nmap output parsing error",
            description=str(e),
            tool="nmap",
        )
        result.add_finding(finding)

    result.finished_at = datetime.datetime.utcnow().isoformat() + "Z"
    return result
