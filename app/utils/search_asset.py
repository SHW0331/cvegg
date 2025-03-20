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

        configurations = cve.get("configurations", {})
        if configurations:
            nodes = configurations[0].get("nodes", {})
            if nodes:
                cpe_match = nodes[0].get("cpeMatch", {})
                if cpe_match:
                    # versionEndIncluding	해당 버전까지 포함하여 영향을 받음
                    # versionEndExcluding	해당 버전까지 제외하고 영향을 받음
                    # versionStartIncluding	해당 버전부터 포함하여 영향을 받음
                    # versionStartExcluding	해당 버전부터 제외하고 영향을 받음
                    match = cpe_match[0]
                    version_start_including = match.get("versionStartIncluding")
                    version_start_excluding = match.get("versionStartExcluding")
                    version_end_including = match.get("versionEndIncluding")
                    version_end_excluding = match.get("versionEndExcluding")

                    # 결과 출력
                    if version_start_including:
                        print(f"versionStartIncluding: {version_start_including} (Affected starting from this version)")
                    if version_start_excluding:
                        print(f"versionStartExcluding: {version_start_excluding} (Affected excluding this version onward)")
                    if version_end_including:
                        print(f"versionEndIncluding: {version_end_including} (Affected up to and including this version)")
                    if version_end_excluding:
                        print(f"versionEndExcluding: {version_end_excluding} (Affected up to but excluding this version)")

                    # 만약 아무 조건도 없을 경우
                    if not (version_start_including or version_start_excluding or 
                            version_end_including or version_end_excluding):
                        print("No version range information available.")             

    else:
        filtered_data = {
            "cve_id" : user_input,
            "published" : "N/A",
            "descriptions_en" : "N/A",
            "indent_json" : "N/A"      
        }
    print(filtered_data["indent_json"])
    return filtered_data
    # return filtered_data

user_value = input()
nvd_data = get_nvd_data(user_value)
