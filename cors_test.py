import subprocess
import os

def run_cors_test(domain):
    output_dir = f"output/{domain}"
    cors_file = f"{output_dir}/cors_test.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Testing CORS misconfiguration...")

    cmd = f'''curl -s -I -H "Origin: https://evil.com" https://{domain} | grep -i "Access-Control" > {cors_file}'''

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] CORS test results saved to: {cors_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while testing CORS.")