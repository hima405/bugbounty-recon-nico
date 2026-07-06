import subprocess
import os

def run_gowitness(domain):
    output_dir = f"output/{domain}"
    live_file = f"{output_dir}/live_subdomains.txt"
    screenshot_dir = f"{output_dir}/screenshots"

    os.makedirs(screenshot_dir, exist_ok=True)

    if not os.path.exists(live_file):
        print("[!] Live subdomains file not found. Run Live Check first.")
        return

    print("[*] Taking screenshots using Gowitness...")

    cmd = f"gowitness file -f {live_file} -P {screenshot_dir}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Screenshots saved in: {screenshot_dir}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running gowitness.")