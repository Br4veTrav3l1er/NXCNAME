import subprocess

# Define the input file containing the list of domains
input_file = "subdomains.txt"

# Read the list of domains from the input file
with open(input_file, "r") as file:
    domains = [line.strip() for line in file]

# Loop through each domain and check for NXDOMAIN and CNAME
for domain in domains:
    process = subprocess.Popen(
        ["dig", domain, "CNAME"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    result, _ = process.communicate()
    
    process = subprocess.Popen(
        ["dig", domain],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    status, _ = process.communicate()

    if "NXDOMAIN" in status and result:
        print(f"Domain: {domain} CNAME: {result}")

