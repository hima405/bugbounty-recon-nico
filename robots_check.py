import subprocess
import os

def run_robots_check(domain):
    output_dir = f"output/{domain}"
    robots_file = f"{output_dir}/robots.txt"

    os.makedirs(output_dir, exist_ok=True)

    print("[*] Checking robots.txt and sitemap.xml...")

    try:
        # robots.txt
        cmd1 = f"curl -s https://{domain}/robots.txt -o {robots_file}"
        subprocess.run(cmd1, shell=True, check=True)

        # sitemap.xml (optional)
        sitemap_file = f"{output_dir}/sitemap.xml"
        cmd2 = f"curl -s https://{domain}/sitemap.xml -o {sitemap_file}"
        subprocess.run(cmd2, shell=True)

        print(f"[+] robots.txt and sitemap saved in: {output_dir}")
    except subprocess.CalledProcessError:
        print("[!] Error occurred while checking robots.txt.")