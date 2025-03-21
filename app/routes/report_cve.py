from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.nvd import get_nvd_data
from app.utils.poc import search_poc
import re

# BluePrint 정의
report_bp = Blueprint('report', __name__, template_folder='../templates/report')

# route 정의
@report_bp.route('/report', methods=['GET', 'POST'])
def report():
    # 사용자 입력
    if request.method == 'POST':
        user_input = request.form.get('cve_num')
    else:
        user_input = request.args.get('cve')

    # CVE-YYYY-NNNN 형식 유효성 검사
    if not re.match(r'^CVE-\d{4}-\d{4,}$', user_input):  # 정규식으로 형식 확인
        return render_template('error.html', data=user_input)
    
    cve_data = get_nvd_data(user_input)
    if not cve_data:
        return render_template('error_cve.html', data=user_input)

    poc_data = search_poc(user_input)
    
    return render_template('report.html', data=cve_data, github_data=poc_data[:5])
