import requests
import json

def get_nvd_data(user_input):
    nvd_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
    nvd_key = "your_api_key"

    search_url = nvd_url + "?cveId=" + user_input
    headers = {
        "nvd_key": nvd_key
    }

    response = requests.get(search_url, headers=headers)
    cve_json = json.loads(response.text)
    
    vulnerabilities = cve_json.get("vulnerabilities", [])
    if vulnerabilities:
        cve = vulnerabilities[0].get("cve", {})
        filtered_data = {
            "cve_id" : cve.get("id", "N/A"),
            "published" : cve.get("published", "N/A"),
            "descriptions_en" : next(
                (desc.get("value") for desc in cve.get("descriptions",[]) if desc.get("lang") == "en"), "N/A"),
            "indent_json" : json.dumps(cve_json, indent=4)        
        }
    else:
        filtered_data = {
            "cve_id" : user_input,
            "published" : "N/A",
            "descriptions_en" : "N/A",
            "indent_json" : "N/A"      
        }

    return filtered_data
    # return filtered_data