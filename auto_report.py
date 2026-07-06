import os
from modules.ai_helper import ask_ai

def generate_report(domain):
    output_dir = f"output/{domain}"
    report_file = f"{output_dir}/AI_Report_{domain}.md"

    if not os.path.exists(output_dir):
        print("[!] No recon data found for this domain. Run some scans first.")
        return

    print("[*] Reading recon results...")

    # Collect data from existing files
    data_summary = ""

    files_to_check = [
        "live_subdomains.txt",
        "nuclei_results.txt",
        "directories.txt",
        "wayback_urls.txt",
        "gau_urls.txt"
    ]

    for file in files_to_check:
        file_path = os.path.join(output_dir, file)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                data_summary += f"\n\n=== {file} ===\n{content[:3000]}"  # Limit to avoid too much data

    if not data_summary.strip():
        print("[!] No useful recon data found to generate a report.")
        return

    print("[*] Sending data to AI for report generation...")

    prompt = f"""
You are a professional bug bounty hunter. Based on the following reconnaissance data, generate a clean and professional bug bounty report.

Domain: {domain}

Recon Data:
{data_summary}

Please generate the report in this format:

1. Target Overview
2. Key Findings (list important subdomains, technologies, endpoints, vulnerabilities)
3. Potential Attack Surfaces
4. Recommended Next Steps / Testing Areas
5. Summary

Keep the report professional, concise, and useful for bug bounty reporting.
"""

    ai_response = ask_ai(prompt)

    # Save the report
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(ai_response)

    print(f"[+] AI Report generated and saved to: {report_file}")