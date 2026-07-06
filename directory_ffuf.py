import subprocess
import os

def run_directory_bruteforce(domain):
    output_dir = f"output/{domain}"
    live_file = f"{output_dir}/live_subdomains.txt"
    dir_file = f"{output_dir}/directories.txt"

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(live_file):
        print("[!] Live subdomains file not found. Run Live Check first.")
        return

    print("[*] Running Directory Brute-force using ffuf...")

    wordlist = "/usr/share/wordlists/dirb/common.txt"

    cmd = f"ffuf -u https://FUZZ.{domain} -w {wordlist} -o {dir_file} -of plain -silent"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Directory brute-force results saved to: {dir_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running ffuf.")