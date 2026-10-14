import socket


def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        s.connect((target, port))
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
    finally:
        s.close()


# Default arguments added so run_recon(target, results) works seamlessly
def run_recon(target, results, start_port=1, end_port=1024):
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            results["ports"].append(port)

    return results