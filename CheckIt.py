#!/usr/bin/env python3

"""
CheckIt v1.0 - Ethical Checking Tool
Developer: Syrox
License: MIT
"""

import os
import colorama
import requests
import random
import time
import platform
import getpass

# System
systemos = platform.system()
systemuser = getpass.getuser()

# Start Clear
def startclear():
    if systemos == 'Windows':
        os.system('cls')
        os.system('title CheckIt')
    else:
        os.system('clear')
startclear()

# Username Clear
def usernameclear():
    if systemos == 'Windows':
        os.system('cls')
        title()
    else:
        os.system('clear')
        title()

# Title
def title():
    print(colorama.Fore.YELLOW + """
_________ .__                   __   .___  __   
\_   ___ \|  |__   ____   ____ |  | _|   |/  |__ 
/    \  \/|  |  \_/ __ \_/ ___\|  |/ /   \   __|
\     \___|   Y  \  ___/\  \___|    <|   ||  |  
 \______  /___|  /\___  >\___  >__|_ \___||__|  
        \/     \/     \/     \/     \/          \n""" + colorama.Fore.RESET)
title()

# Data
options = [1, 2, 3, 4, 5, 96, 97, 98, 99, 00]
platforms = ['github']
answers = ['Y', 'N']
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    }

# Start
start = True
generator = True
checker = True

# Tools
def tools():
    print(colorama.Fore.RESET + """
[01] Account Checker   |   [96] Social
[02] Username Checker  |   [97] Info
[03] Website Checker   |   [98] Help
[04] File Checker      |   [99] Exit
[05] System Checker    |   [00] Clear\n""")

# Help
def usernamehelp():
    print(colorama.Fore.RESET + """\nHelp\n
- Platforms [GitHub]
- Username Length [Length of characters] {MIN 4; MAX 39}
- Delay [Waiting time between requests] {MIN 0}
- Requests [Request number to be sent] {MIN 1; MAX 100}
- Answers [Y = YES, N = N0] {NECESSARY}
- CTRL + C [Stops the running tool]""")

# Info
def info():
    print("""\nInformations\n
[N] Name: CheckIt
[T] Type: Ethical Tool
[V] Version: 1.0
[D] Developer: Syrox""")

# Social
def social():
    print("""\nSocial Network\n
[Y] YouTube: @SyroxModsOfficial {https://youtube.com/@SyroxModsOfficial}
[G] GitHub: 5a1r0x {https://github.com/5a1r0x}
[T] TikTok: syroxmodsofficial {https://tiktok.com/@syroxmodsofficial""")

# Username Checker
def accountchecker():
    print("\nAccount Checker")

    while True:
        try:
            # Platform Input (.com)
            account_checker_platform = str(input(colorama.Fore.YELLOW + "\n[+] Platform: ")).lower()

            # Platform Not In List
            if account_checker_platform not in platforms:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: This platform isn't available")

            # No Platform Entered
            if not account_checker_platform:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a platform" + colorama.Fore.RESET)

            # Platform Exit > (99)
            if account_checker_platform == '99':
                print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                break

            # Username Input
            if account_checker_platform in platforms:
                account_checker_user = str(input(colorama.Fore.CYAN + "[+] Username: "))

                # No Username Entered > Attention, Warning Message > Stop Tool Execution
                if not account_checker_user:
                    print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: No value entered")
                    print(colorama.Fore.RED + "[*] Warning: The tool will be finished because it is impossible to proceed with the request")
                    break

                # Username Exit > (99)
                if account_checker_user == '99':
                    print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                    break

                # Platform, Username > Request > Result
                username_checker_request = requests.get(f'https://{account_checker_platform}.com/{account_checker_user}', headers=headers)
                if username_checker_request.status_code == 200:
                    print(colorama.Fore.GREEN + f"[$] Account Found: https://{account_checker_platform}.com/{account_checker_user}" + colorama.Fore.RESET)
                elif username_checker_request.status_code == 404:
                    print(colorama.Fore.RED + "[-] Account Not Found" + colorama.Fore.RESET)
                else:
                    print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Your request has been blocked or the service is not available at the moment ->", str(username_checker_request.status_code) + colorama.Fore.RESET)

        # Exceptions
        except Exception as exc:
            print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: " + str(exc) + colorama.Fore.RESET)
        except KeyboardInterrupt:
            print(colorama.Fore.LIGHTRED_EX + "\n\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
            break

# Username Generator
def usernamechecker():
    print("\nUsername Checker")

    while True:
        try:
            # Platform Input
            username_checker_platform = str(input(colorama.Fore.YELLOW + "\n[+] Platform: ")).lower()

            # Platform Not In List
            if username_checker_platform not in platforms:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: This platform isn't available")

            # No Platform Entered
            if not username_checker_platform:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a platform\n" + colorama.Fore.RESET)

            # Platform Exit > (99)
            if username_checker_platform == '99':
                print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                break

            # Length Input
            username_checker_length = int(input(colorama.Fore.LIGHTCYAN_EX + "[+] Length: "))

            # Length Exit > (99)
            if username_checker_length == 99:
                print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                break

            # No Length Entered
            if not username_checker_length:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter the length of usernames\n" + colorama.Fore.RESET)
            elif username_checker_length < 4 or username_checker_length > 39:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a value between 4 and 39" + colorama.Fore.RESET)
                print(colorama.Fore.RED + "[*] Warning: The tool will be finished because it is impossible to proceed with the request")
                break

            # Delay Input
            username_checker_sleep = int(input(colorama.Fore.MAGENTA + "[+] Delay: "))

            # File Input
            username_checker_file = str(input(colorama.Fore.LIGHTMAGENTA_EX + "[+] File: ")).upper()

            # No File Entered, Incorrect
            if not username_checker_file or username_checker_file not in answers:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a Y or N value" + colorama.Fore.RESET)

            # File > Y(es) > Attention Message
            if username_checker_platform in platforms and username_checker_file == 'Y':
                print(colorama.Fore.LIGHTBLUE_EX + "[+] Attention: The file will be updated at the end of the tool execution (UsernameCheckerResult.txt)" + colorama.Fore.RESET)

            # Try Names > Request > Delay > Result > File
                while generator:
                    name_try = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=username_checker_length))
                    name_request = requests.get(f'https://{username_checker_platform}.com/{name_try}', headers=headers)
                    time.sleep(username_checker_sleep)
                    print(colorama.Fore.CYAN + "[+] Trying:", name_try + colorama.Fore.RESET + " | " + colorama.Fore.GREEN + "Username Available" + colorama.Fore.RESET if name_request.status_code == 404 else name_try + colorama.Fore.RESET + " | " + colorama.Fore.RED + "Username Not Available" + colorama.Fore.RESET)

                    # File (UsernameCheckerResult.txt)
                    with open('UsernameCheckerResult.txt', 'a') as ucr:
                        ucr.write("\n")
                        ucr.write(f'{name_try}')
                        ucr.close()

            # File > N(o) > Try Names > Requests > Delay > Result
            elif username_checker_platform in platforms and username_checker_file == 'N':
                while generator:
                    name_try = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=username_checker_length))
                    name_request = requests.get(f'https://{username_checker_platform}.com/{name_try}', headers=headers)
                    time.sleep(username_checker_sleep)
                    print(colorama.Fore.CYAN + "[+] Trying:", name_try + colorama.Fore.RESET + " | " + colorama.Fore.GREEN + "Username Available" + colorama.Fore.RESET if name_request.status_code == 404 else name_try + colorama.Fore.RESET + " | " + colorama.Fore.RED + "Username Not Available" + colorama.Fore.RESET)

        # Exceptions
        except Exception as exc:
            print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: " + str(exc) + colorama.Fore.RESET)
        except KeyboardInterrupt:
            print(colorama.Fore.LIGHTRED_EX + "\n\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
            break

# Website Checker
def websitechecker():
    print("\nWebsite Checker")

    while True:
        # Number Of Requests
        n_request = 0
        try:
            # Website Input
            website_checker_website = str(input(colorama.Fore.YELLOW + "\n[+] Website: ")).lower()

            #No Website Entered
            if not website_checker_website:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a website\n" + colorama.Fore.RESET)

            # Website Exit > (99)
            if website_checker_website == '99':
                print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                break

            # Requests Input
            website_checker_requests = int(input(colorama.Fore.LIGHTMAGENTA_EX + "[+] Requests: "))

            # No Requests Input
            if not website_checker_requests:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter number of requests" + colorama.Fore.RESET)
                print(colorama.Fore.RED + "[*] Warning: The tool will be finished because it is impossible to proceed with the request")
                break
            elif website_checker_requests > 100 or website_checker_requests <= 0:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a value between 1 and 100" + colorama.Fore.RESET)
                print(colorama.Fore.RED + "[*] Warning: The tool will be finished because it is impossible to proceed with the request")
                break

            # Delay Input
            website_checker_delay = int(input(colorama.Fore.MAGENTA + "[+] Delay: "))

            # Verify Website, Existence, Service
            website_verify = requests.get(website_checker_website)

            # Website Verify > Result
            if website_verify.status_code == 200:
                print(colorama.Fore.LIGHTCYAN_EX + "[+] Result: The website exists and is operational" + colorama.Fore.RESET)
                # Requests Limit
                if website_checker_requests >= 101 or website_checker_requests < 0:
                    print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Enter a value between 0 and 100\n" + colorama.Fore.RESET)
                    # Delay
                    if website_checker_delay < 0:
                        print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Enter a value greater than or equal to 0" + colorama.Fore.RESET + colorama.Fore.RESET)
                        break

            # Requests, Status > OK > Number Of Requests > Result
            while website_checker_requests < 101 and website_verify.status_code == 200:
                n_request += 1
                time.sleep(website_checker_delay)
                website_checker_request = requests.get(f'{website_checker_website}', headers=headers)
                print(colorama.Fore.CYAN + "[+] Status:", website_checker_request.status_code, "| Request: " + str(n_request) + colorama.Fore.RESET)
                if n_request == website_checker_requests:
                    break
                else:
                    continue

        # Exceptions
        except Exception as exc:
            print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: " + str(exc) + colorama.Fore.RESET)
        except KeyboardInterrupt:
            print(colorama.Fore.LIGHTRED_EX + "\n\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
            break

# File Checker
def filechecker():
    print("\nFile Checker")

    while True:
        try:
            # File Input
            file_checker_directory = str(input(colorama.Fore.YELLOW + "\n[+] File Name: "))

            # No File Entered
            if not file_checker_directory:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a file\n" + colorama.Fore.RESET)

            # Website Exit > (99)
            if file_checker_directory == '99':
                print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                break

            # File Extension Input
            file_checker_extension = str(input(colorama.Fore.LIGHTCYAN_EX + "[+] File Extension: "))

            # No File Entered
            if not file_checker_extension:
                print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Please enter a file extension\n" + colorama.Fore.RESET)

            # File Exit > (99)
            if file_checker_extension == '99':
                print(colorama.Fore.LIGHTRED_EX + "\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
                break

            if os.path.exists(f'{file_checker_directory}.{file_checker_extension}'):
                print(colorama.Fore.GREEN + f"[$] File Found" + colorama.Fore.RESET)
            else:
                print(colorama.Fore.RED + "[-] File Not Found" + colorama.Fore.RESET)

        # Exceptions
        except Exception as exc:
            print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: " + str(exc) + colorama.Fore.RESET)
        except KeyboardInterrupt:
            print(colorama.Fore.LIGHTRED_EX + "\n\n[+] Tool interrupted by the user" + colorama.Fore.RESET)
            break

# System Checker
def systemchecker():
    print("\nSystem Checker")
    print(colorama.Fore.YELLOW + "\n[+] Operating System:", platform.system() + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "[+] Machine:", platform.machine() + colorama.Fore.RESET)
    print(colorama.Fore.MAGENTA + "[+] Platform:", platform.platform() + colorama.Fore.RESET)
    print(colorama.Fore.CYAN + "[+] Processor:", platform.processor() + colorama.Fore.RESET)
    print(colorama.Fore.LIGHTGREEN_EX + "[+] Architecture: " + str(platform.architecture()) + colorama.Fore.RESET)

# CheckIt
class CheckIt:
    # Start
    while start:
        try:
            tools()
            opt = int(input(f"""\n┌──────[{systemuser.lower()}@{systemos.lower()}]
|
└──────[$]: """))
            # Check if the value is valid
            if opt in options:
                # Username Checker
                if opt == 1:
                    accountchecker()
                # Username Generator
                elif opt == 2:
                    usernamechecker()
                # Website Checker
                elif opt == 3:
                    websitechecker()
                # File Checker
                elif opt == 4:
                    filechecker()
                # System Checker
                elif opt == 5:
                    systemchecker()
                # Social
                elif opt == 96:
                    social()
                # Info
                elif opt == 97:
                    info()
                # Help
                elif opt == 98:
                    usernamehelp()
                # Exit
                elif opt == 99:
                    print(colorama.Fore.RED + "\n[-] Exit Complete" + colorama.Fore.RESET)
                    break
                # Clear
                elif opt == 00:
                    usernameclear()
            # Not In Options
            elif opt not in options:
                print(
                    colorama.Fore.LIGHTRED_EX + "\n[!] Attention: The value is not present in the transactions" + colorama.Fore.RESET)

        # Exceptions
        except ValueError:
            print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: Enter a numeric value" + colorama.Fore.RESET)
        except Exception as exc:
            print(colorama.Fore.LIGHTRED_EX + "\n[!] Attention: " + str(exc) + colorama.Fore.RESET)
        except KeyboardInterrupt:
            print(colorama.Fore.RED + "\n\n[-] Exit Complete" + colorama.Fore.RESET)
            break

# Run
if __name__ == "__main__":
    CheckIt()

