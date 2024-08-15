# Blind SQL Injection Tool

This tool is designed to check for SQL Injection vulnerabilities in web applications. It iterates over URLs and payloads, testing each combination for potential SQL Injection vulnerabilities.

## Features

- Tests multiple URLs against a wordlist of payloads.
- Detects potential vulnerabilities based on response times.
- Designed for penetration testers and bug bounty hunters.

## Disclaimer

This tool is intended for educational purposes only. The author is not responsible for any misuse or damage caused by this tool. Please use responsibly and only on systems you have permission to test.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jamaal001/blind_sqli.git
   cd blind_sqli
   

2. **usage**
3. ``` bash
   paramspider -d testphp.vulnweb.com
   cat urls.txt | sed 's/FUZZ//g' > final.txt
   python3 main.py -t final.txt -w xor.txt
   
