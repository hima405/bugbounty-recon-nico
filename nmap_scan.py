import subprocess
import os

def run_nmap(domain):
    output_dir = f"output/{domain}"
    nmap_file = f"{output_dir}/nmap_scan.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Running Nmap port scan on the domain...")

    cmd = f"nmap -sV -sC {domain} -oN {nmap_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Nmap scan results saved to: {nmap_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running nmap.")