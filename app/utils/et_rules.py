import requests
import tarfile
import os

ET_RULES_LINK = "https://rules.emergingthreats.net/open/snort-$version/emerging.rules.tar.gz"
filename = ET_RULES_LINK.split('/')[-1]

download_path = './et_rules'
os.makedirs(download_path, exist_ok=True)

with requests.get(ET_RULES_LINK, stream=True) as r:
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                
print(f"파일 다운로드 완료 : {filename}")                

extract_path = './'

