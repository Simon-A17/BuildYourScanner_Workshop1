from analysis import analyse_results
from recon import run_recon
from report import generate_report


def main():
    target = input("Enter the target IP or hostname to scan: ").strip()

    if not target:
        target = "127.0.0.1"

    results = {"target": target, "ports": [], "services": []}

    print(f"\n[*] Starting reconnaissance on {target}...")

    # Safe call - uses default range 1 to 1024
    results = run_recon(target, results)

    print("[*] Recon complete. Analyzing discovered ports...")

    results = analyse_results(results)

    print("[*] Analysis complete. Generating report...\n")

    generate_report(results)


if __name__ == "__main__":
    main()