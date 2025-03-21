import requests
import json

NVD_KEYWORD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
def search_keyword(keyword):
    data = []
    params = {
        "keywordSearch": keyword
    }
    response = requests.get(NVD_KEYWORD_API_URL, params=params)

    if response.status_code == 200:
        items = response.json()
        for vuln in items["vulnerabilities"][::-1]:
            cve_id = vuln["cve"]["id"]
            published = vuln["cve"]["published"]
            description = vuln["cve"]["descriptions"][0]["value"]
            data.append([
                cve_id,
                published,
                description
            ])
        return data
    else:
        print(f"Error: {response.status_code}")
        return data