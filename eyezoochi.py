import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

import json

from unmo import Unmo

#bp = Blueprint('eyezoochi', __name__, url_prefix='/eyezoochi')
bp = Blueprint('eyezoochi', __name__)

@bp.route('/What', methods=('GET', 'POST'))
def what():
    input_text=''
    if request.method == 'POST':
        input_text= request.form['input_text']
        print('input is {}'.format(input_text))

    return render_template('what.html', output_text=input_text)

@bp.route('/eyezoochi/', methods=('GET', 'POST'))
def eyezoochi():
    input_text=''
    response=''
    if request.method == 'POST':
        proto = Unmo('proto')
        input_text= request.form['input_text']
        print('input is {}'.format(input_text))
        response = proto.dialogue(input_text)

    return render_template('eyezoochi.html',
        previous_text=input_text, output_text=response)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/eyezoochi_spa', methods=('GET', 'POST'))
def eyezoochi_spa():

# GETデータからパラメター取得
    input_text = request.args.get('text')
    callback = request.args.get('callback')

# 人工無脳Unmoで回答文生成
    proto = Unmo('proto')
    response_text = proto.dialogue(input_text)

# 回答メッセージの生成
    response = callback + '(' + json.dumps({
        "output":[
            {
                "type":"text",
                "value":response_text
            }
        ]
    }) + ')'

    return response
