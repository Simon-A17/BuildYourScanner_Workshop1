def generate_report(results):
    print("=" * 40)
    print("           RECONNAISSANCE REPORT        ")
    print("=" * 40)

    target = results.get("target", "Unknown Target")
    print(f"Target IP / Host: {target}")

    ports = results.get("ports", [])
    if ports:
        ports_str = ", ".join(map(str, ports))
        print(f"Open Ports Found: {ports_str}")
    else:
        print("Open Ports Found: None")

    print("-" * 40)
    print("Identified Services:")

    services = results.get("services", [])
    if services:
        for entry in services:
            port = entry.get("port", "N/A")
            service = entry.get("service", "Unknown")

            # Safe formatting check for integers vs fallback strings
            if isinstance(port, int):
                print(f"  - Port {port:5d} : {service}")
            else:
                print(f"  - Port {port:>5} : {service}")
    else:
        print("  - No service information available.")

    print("=" * 40)