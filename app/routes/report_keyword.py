from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.keyword import search_keyword

# BluePrint 정의
keyword_bp = Blueprint('keyword', __name__, template_folder='../templates/keyword')

# route 정의
@keyword_bp.route('/keyword', methods=['POST'])
def keyword():
    # 사용자 입력
    user_keyword  = request.form.get('keyword_name')

    data_keyword = search_keyword(user_keyword)
    if not data_keyword:
        return render_template('error_keyword.html', data=user_keyword, name=user_keyword)

    return render_template('keyword.html', data=data_keyword, data_len=len(data_keyword), name=user_keyword)