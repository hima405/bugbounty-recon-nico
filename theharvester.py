import subprocess
import os

def run_theharvester(domain):
    output_dir = f"output/{domain}"
    harvester_file = f"{output_dir}/theharvester_results.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Running theHarvester for email and credential harvesting...")

    cmd = f"theHarvester -d {domain} -b all -f {harvester_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] theHarvester results saved to: {harvester_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running theHarvester.")