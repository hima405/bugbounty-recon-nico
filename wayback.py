import subprocess
import os

def run_wayback(domain):
    output_dir = f"output/{domain}"
    wayback_file = f"{output_dir}/wayback_urls.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Collecting URLs from Wayback Machine using waybackurls...")

    cmd = f"waybackurls {domain} > {wayback_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Wayback URLs saved to: {wayback_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running waybackurls.")