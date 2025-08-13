from use_cases import ScanOrchestrator, default_scanner_runner, ReportGenerator
from domain.scan_types import ScanType

orch = ScanOrchestrator(default_scanner_runner)
result = orch.run(scan_type="code", target="~/projects/myrepo", profile="quick", language="python")
print("Findings count:", len(result.findings))
rg = ReportGenerator()
outs = rg.generate(result)
print("Generated reports:", outs)
