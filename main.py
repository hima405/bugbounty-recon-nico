from modules import start_ai_assistant
from modules import generate_report
from modules import (
    run_subdomain_enum,
    run_live_check,
    run_wayback,
    run_gau,
    run_directory_bruteforce,
    run_nuclei,
    run_nmap,
    run_whatweb,
    run_gowitness,
    run_arjun,
    run_robots_check,
    run_headers_check,
    run_cors_test,
    run_backup_finder,
    run_git_exposure,
    run_open_redirect,
    run_asn_discovery,
    run_theharvester,
    run_testssl
)

def show_menu():
    print("\n" + "="*55)
    print("          BUG BOUNTY recon by NiCO")
    print("="*55)
    print(" 1.  Subdomain Enumeration (subfinder)")
    print(" 2.  Live Subdomain Check (httpx)")
    print(" 3.  Wayback Machine URLs")
    print(" 4.  Gau URL Collection")
    print(" 5.  Directory Brute-force (ffuf)")
    print(" 6.  Nuclei Vulnerability Scan")
    print(" 7.  Nmap Port Scan")
    print(" 8.  Technology Detection (whatweb)")
    print(" 9.  Screenshot Subdomains (gowitness)")
    print("10. Parameter Discovery (arjun)")
    print("11. Robots.txt & Sitemap Check")
    print("12. HTTP Security Headers Check")
    print("13. CORS Misconfiguration Test")
    print("14. Backup File Discovery")
    print("15. Git Directory Exposure Check")
    print("16. Open Redirect / SSRF Parameter Hunt")
    print("17. ASN & IP Range Discovery")
    print("18. Email & Credential Harvesting (theHarvester)")
    print("19. SSL/TLS Misconfiguration (testssl)")
    print("20. Full Basic Recon (Run 1-5 together)")
    print("21. AI Auto Report Generator")
    print("22. AI Recon Assistant (Chat)")
    print(" 0.  Exit")
    print("="*55)

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            domain = input("Enter target domain: ")
            run_subdomain_enum(domain)
        elif choice == "2":
            domain = input("Enter target domain: ")
            run_live_check(domain)
        elif choice == "3":
            domain = input("Enter target domain: ")
            run_wayback(domain)
        elif choice == "4":
            domain = input("Enter target domain: ")
            run_gau(domain)
        elif choice == "5":
            domain = input("Enter target domain: ")
            run_directory_bruteforce(domain)
        elif choice == "6":
            domain = input("Enter target domain: ")
            run_nuclei(domain)
        elif choice == "7":
            domain = input("Enter target domain: ")
            run_nmap(domain)
        elif choice == "8":
            domain = input("Enter target domain: ")
            run_whatweb(domain)
        elif choice == "9":
            domain = input("Enter target domain: ")
            run_gowitness(domain)
        elif choice == "10":
            domain = input("Enter target domain: ")
            run_arjun(domain)
        elif choice == "11":
            domain = input("Enter target domain: ")
            run_robots_check(domain)
        elif choice == "12":
            domain = input("Enter target domain: ")
            run_headers_check(domain)
        elif choice == "13":
            domain = input("Enter target domain: ")
            run_cors_test(domain)
        elif choice == "14":
            domain = input("Enter target domain: ")
            run_backup_finder(domain)
        elif choice == "15":
            domain = input("Enter target domain: ")
            run_git_exposure(domain)
        elif choice == "16":
            domain = input("Enter target domain: ")
            run_open_redirect(domain)
        elif choice == "17":
            domain = input("Enter target domain: ")
            run_asn_discovery(domain)
        elif choice == "18":
            domain = input("Enter target domain: ")
            run_theharvester(domain)
        elif choice == "19":
            domain = input("Enter target domain: ")
            run_testssl(domain)
        elif choice == "20":
            domain = input("Enter target domain: ")
            print("[+] Running Full Basic Recon (1-5)...")
            run_subdomain_enum(domain)
            run_live_check(domain)
            run_wayback(domain)
            run_gau(domain)
            run_directory_bruteforce(domain)

        elif choice == "21":
            domain = input("Enter target domain: ")
            generate_report(domain)
        
        elif choice == "22":
            domain = input("Enter target domain: ")
            start_ai_assistant(domain)    

        elif choice == "0":
            print("Exiting tool. Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()