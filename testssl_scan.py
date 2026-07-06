import subprocess
import os

def run_testssl(domain):
    output_dir = f"output/{domain}"
    testssl_file = f"{output_dir}/testssl_results.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Running testssl.sh for SSL/TLS misconfiguration check...")

    cmd = f"testssl.sh https://{domain} > {testssl_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] testssl.sh results saved to: {testssl_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running testssl.sh.")
    except FileNotFoundError:
        print("[!] testssl.sh is not installed or not found in PATH.")