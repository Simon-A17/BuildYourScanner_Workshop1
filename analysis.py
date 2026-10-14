COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt",
}


def analyse_results(results):
    if "services" not in results:
        results["services"] = []

    for port in results.get("ports", []):
        service = COMMON_SERVICES.get(port, "Unknown Service")
        results["services"].append({"port": port, "service": service})

    return results