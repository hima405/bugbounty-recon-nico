# bug bounty recon by NiCO

A powerful **Bug Bounty Reconnaissance Tool** built with Python and AI integration.  
It automates reconnaissance, analyzes results using AI, and helps generate professional bug bounty reports.

---

## Features

- **20+ Reconnaissance Modules** (Subdomain enumeration, Live hosts, Wayback, Gau, ffuf, Nuclei, Nmap, etc.)
- **AI Auto Report Generator** – Automatically generates clean bug bounty reports using AI
- **AI Recon Assistant** – Interactive chat to analyze targets and get testing suggestions
- Clean and simple menu-based interface
- Well-organized output structure
- Secure API key management using `.env` file

---

## Tech Stack

- **Python 3**
- **OpenRouter API** (for AI features)
- External Tools: `subfinder`, `httpx`, `nuclei`, `ffuf`, `gau`, `waybackurls`, `gowitness`, `amass`

---

Installation

1. Clone the Repository
```bash
git clone https://github.com/hima405/bugbounty-recon-nico.git
cd bugbounty-recon-nico

2. Create Virtual Environment
Bash

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
3. Install Python Dependencies
Bash

pip install -r requirements.txt
4. Setup Environment Variables
Create a .env file in the root directory and add your OpenRouter API key:

env

OPENROUTER_API_KEY={xx-xx-xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
5. Install Required Tools
Make sure the following tools are installed and available in your system PATH:

subfinder
httpx
nuclei
ffuf
gau
waybackurls
gowitness
amass
Usage
Run the tool using:

Bash

python main.py
You will see a menu with the following options:

Option	Feature	Description
1–20	Recon Modules	Various reconnaissance tools
21	AI Auto Report Generator	Generate AI-powered bug bounty reports
22	AI Recon Assistant	Chat with AI for analysis and ideas
0	Exit	Exit the tool
Project Structure
text

recon-tool/
├── main.py
├── modules/
│   ├── ai_helper.py
│   ├── auto_report.py
│   ├── ai_assistant.py
│   └── ...
├── output/
├── venv/
├── .env
├── .gitignore
└── README.md
Disclaimer
This tool is developed for educational purposes and authorized security testing only.
Do not use it on any target without explicit permission. The author is not responsible for any misuse or illegal activity.

Future Improvements
Add a full Vulnerability Scanner module
Support for multiple AI providers
Better reporting and visualization
More advanced bug detection modules
Author
NiCO

If you find this tool helpful, consider giving it a ⭐ on GitHub!