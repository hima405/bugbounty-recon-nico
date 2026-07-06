import subprocess
import os

def run_nuclei(domain):
    output_dir = f"output/{domain}"
    live_file = f"{output_dir}/live_subdomains.txt"
    nuclei_file = f"{output_dir}/nuclei_results.txt"

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(live_file):
        print("[!] Live subdomains file not found. Run Live Check first.")
        return

    print("[*] Running Nuclei vulnerability scan...")

    cmd = f"nuclei -l {live_file} -o {nuclei_file} -silent"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Nuclei results saved to: {nuclei_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running nuclei.")