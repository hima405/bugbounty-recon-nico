import subprocess
import os

def run_git_exposure(domain):
    output_dir = f"output/{domain}"
    git_file = f"{output_dir}/git_exposure.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Checking for .git directory exposure...")

    cmd = f"curl -s -I https://{domain}/.git/HEAD > {git_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Git exposure check saved to: {git_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while checking .git exposure.")