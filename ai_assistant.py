import os
from modules.ai_helper import ask_ai

def start_ai_assistant(domain):
    output_dir = f"output/{domain}"

    print(f"\n[+] Starting AI Recon Assistant for: {domain}")
    print("Type 'exit' to quit the assistant.\n")

    context = f"Domain: {domain}\n\n"

    live_file = os.path.join(output_dir, "live_subdomains.txt")
    if os.path.exists(live_file):
        with open(live_file, "r", encoding="utf-8", errors="ignore") as f:
            context += "Live Subdomains:\n" + f.read()[:2000] + "\n\n"

    nuclei_file = os.path.join(output_dir, "nuclei_results.txt")
    if os.path.exists(nuclei_file):
        with open(nuclei_file, "r", encoding="utf-8", errors="ignore") as f:
            context += "Nuclei Results:\n" + f.read()[:1500] + "\n\n"

    print("[*] AI is ready. You can now ask questions about this target.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("[+] Exiting AI Assistant.\n")
            break

        if not user_input:
            continue

        prompt = f"""
You are a professional bug bounty assistant.

Target Domain: {domain}

Recon Data:
{context}

User Question: {user_input}

Answer helpfully and professionally. Suggest testing ideas if relevant.
"""

        print("\nAI: ", end="")
        response = ask_ai(prompt)
        print(response)
        print("\n" + "-"*50)