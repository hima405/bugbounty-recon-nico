import subprocess
import os

def run_headers_check(domain):
    output_dir = f"output/{domain}"
    headers_file = f"{output_dir}/security_headers.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Checking HTTP Security Headers...")

    cmd = f"curl -sI https://{domain} > {headers_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Security headers saved to: {headers_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while checking headers.")