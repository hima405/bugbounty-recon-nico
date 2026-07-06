import subprocess
import os

def run_arjun(domain):
    output_dir = f"output/{domain}"
    live_file = f"{output_dir}/live_subdomains.txt"
    arjun_file = f"{output_dir}/arjun_params.txt"

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(live_file):
        print("[!] Live subdomains file not found. Run Live Check first.")
        return

    print("[*] Discovering parameters using Arjun...")

    cmd = f"arjun -u https://{domain} -oT {arjun_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Arjun results saved to: {arjun_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running arjun.")