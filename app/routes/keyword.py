from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.search_keyword import *

# BluePrint 정의
keyword_bp = Blueprint('keyword', __name__, template_folder='../templates/keyword')

# route 정의
@keyword_bp.route('/keyword', methods=['POST'])
def keyword():
    # 사용자 입력
    user_keyword  = request.form.get('input_keyword') 