import subprocess
import os

def run_backup_finder(domain):
    output_dir = f"output/{domain}"
    backup_file = f"{output_dir}/backup_files.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Searching for backup files...")

    # Common backup extensions
    wordlist = "backup\nbackup.zip\nbackup.tar.gz\nbackup.sql\nsite.zip\nsite.tar.gz\ndatabase.sql\nold.zip"

    cmd = f"echo -e '{wordlist}' | ffuf -u https://{domain}/FUZZ -w - -o {backup_file} -of plain -silent"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Backup file scan results saved to: {backup_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while searching for backup files.")