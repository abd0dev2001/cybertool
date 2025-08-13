from domain.scan_result import ScanResult, ScanFinding
r = ScanResult.new("https://example.com", "web")
r.add_finding(ScanFinding.create("high", "SQL Injection", "Blind SQL injection found", location="/login", tool="sqlmap"))
r.finish()
p = r.save("reports")
print("Saved to:", p)
