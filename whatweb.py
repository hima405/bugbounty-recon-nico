import subprocess
import os

def run_whatweb(domain):
    output_dir = f"output/{domain}"
    whatweb_file = f"{output_dir}/whatweb_results.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Detecting technologies using WhatWeb...")

    cmd = f"whatweb https://{domain} > {whatweb_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] WhatWeb results saved to: {whatweb_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running whatweb.")