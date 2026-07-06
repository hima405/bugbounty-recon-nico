import subprocess
import os

def run_subdomain_enum(domain):
    output_dir = f"output/{domain}"
    subdomains_file = f"{output_dir}/subdomains.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Running Subdomain Enumeration using subfinder...")

    cmd = f"subfinder -d {domain} -o {subdomains_file} -silent"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Subdomains saved to: {subdomains_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running subfinder.")