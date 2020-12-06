from flask import Flask, render_template, request
import os
import sys

sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('../../../'))
sys.path.append(os.path.abspath('../../../../'))

app = Flask(__name__)


def get_action_for_drop_down(drop_down_item):
    return render_template('home.html', drop_downs=get_drop_downs(),message = f"you entered '{drop_down_item}'")

def get_drop_downs():
    drop_downs = [c for c in 'abcd']
    return drop_downs


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('actions')
        return get_action_for_drop_down(action)
    return render_template('home.html', drop_downs=get_drop_downs(),message=None)
