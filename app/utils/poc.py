import requests
import json

# GITHUB API
GITHUB_API_URL = "https://api.github.com/search/repositories"

def search_poc(cve_id):
    data = []
    params = {
        "q": f"{cve_id}",
        "sort": "stars", # 인기순
        "order": "desc" # 내림차순
    }
    response = requests.get(GITHUB_API_URL, params=params)

    if response.status_code == 200:
        items = response.json().get("items", [])
        for repo in items:
            data.append([
                repo['name'],
                repo.get('description', "No description"),
                repo['html_url']
                # data[count][0] = repo['name']
                # data[count][1] = repo.get('description', 'No description')
                # data[count][2] = repo['html_url']
            ])
        return data
    else:
        return data