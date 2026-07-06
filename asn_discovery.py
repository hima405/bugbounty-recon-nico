import subprocess
import os

def run_asn_discovery(domain):
    output_dir = f"output/{domain}"
    asn_file = f"{output_dir}/asn_info.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Discovering ASN and IP range information...")

    cmd = f"amass intel -d {domain} > {asn_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] ASN information saved to: {asn_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while running ASN discovery.")