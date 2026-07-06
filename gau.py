import subprocess
import os

def run_gau(domain):
    output_dir = f"output/{domain}"
    gau_file = f"{output_dir}/gau_urls.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Collecting URLs using gau...")

    cmd = f"gau {domain} > {gau_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Gau URLs saved to: {gau_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running gau.")