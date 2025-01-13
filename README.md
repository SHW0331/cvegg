# CVE 조회 및 PoC 링크 검색기

이 프로젝트는 CVE(Common Vulnerabilities and Exposures) 정보를 검색하고 관련 PoC(Proof of Concept) 링크를 간편하게 확인할 수 있는 기능을 제공합니다.  
NVD(National Vulnerability Database) API를 활용하여 사용자가 입력한 CVE ID에 대한 상세 정보를 가져오고, 관련 GitHub PoC 링크를 함께 출력합니다.

## 주요 기능
- **CVE 조회**: CVE ID를 입력하면 NVD API를 통해 해당 취약점의 상세 정보를 확인할 수 있습니다.
- **PoC 링크 검색**: 입력된 CVE와 관련된 GitHub PoC(Proof of Concept) 링크를 자동으로 출력합니다.
- **웹 인터페이스**: Flask 프레임워크를 활용하여 직관적이고 간단한 웹 UI를 제공합니다.

## 사용 기술
- **Python**: API 연동에 사용.
- **Flask**: 웹 인터페이스 구축에 사용.
- **NVD API**: CVE 정보를 제공하는 데이터 소스.
- **GitHub API**: 관련 PoC 링크를 검색하기 위한 소스.

## 사용 예시
![cvegg 실행 화면](https://github.com/SHW0331/cvegg/blob/f5acfd0d57b6bdaf281db2fe72885c419e7367bf/images/search.png)
*사용자가 CVE ID를 입력한 후 출력된 결과 화면*


## 사용 방법
1. 리포지토리를 클론합니다:
   ```bash
   git clone https://github.com/SHW0331/cvegg.git

## 실행 환경
- Python 3.12.4
- Flask 3.1.0
- requests 2.32.3

## 실행 방법
1. **프로젝트 폴더 이동**
   ```bash
   # 저장 폴더로 이동
   cd cvegg

2. **api key 설정**
   -  
   ```bash
   # \cvegg\app\utils\nvd.py
   
   
2. **가상환경 실행**
   ```bash
   .\.venv\Scripts\activate

3. **flask 실행**
   ```bash
   python run.py

4. **127.0.0.1:5000 Home Page 접속 및 CVE 입력 (CVE-2025-0282)**
   ![cvegg 실행 화면](https://github.com/SHW0331/cvegg/blob/e7bea043499911783845d15bcade2dd95ed3a5cf/images/home.png)

4. **가상환경 종료**
   ```bash
   deactivate

