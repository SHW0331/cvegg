import requests
import json

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
params = {
    "keywordSearch": "Juniper"
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    count = 1
    for vuln in data["vulnerabilities"][::-1]:
        cve_id = vuln["cve"]["id"]
        description = vuln["cve"]["descriptions"][0]["value"]
        print(f"{count} : {cve_id}")
        count += 1
else:
    print(f"Error: {response.status_code}")