import subprocess
import os

def run_live_check(domain):
    output_dir = f"output/{domain}"
    subdomains_file = f"{output_dir}/subdomains.txt"
    live_file = f"{output_dir}/live_subdomains.txt"

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(subdomains_file):
        print("[!] Subdomains file not found. Please run Subdomain Enumeration (Option 1) first.")
        return

    print("[*] Checking live subdomains using httpx...")

    cmd = f"httpx -l {subdomains_file} -o {live_file} -silent -status-code -title"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Live subdomains saved to: {live_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running httpx.")