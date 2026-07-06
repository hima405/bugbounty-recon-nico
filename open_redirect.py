import subprocess
import os

def run_open_redirect(domain):
    output_dir = f"output/{domain}"
    redirect_file = f"{output_dir}/open_redirect.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Testing for Open Redirect / SSRF parameters...")

    # Common vulnerable parameters
    params = "url\nredirect\nnext\nlink\npage\ncontinue\ndest\ndestination\nredir\nredirectUrl"
    param_file = f"{output_dir}/redirect_params.txt"

    # Save parameters to a temp file
    with open(param_file, "w") as f:
        f.write(params)

    cmd = f"ffuf -u https://{domain}/?FUZZ=https://evil.com -w {param_file} -o {redirect_file} -of plain -silent"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"[+] Open Redirect test results saved to: {redirect_file}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while testing open redirect.")