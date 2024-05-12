from flask import Flask, abort, render_template, redirect, url_for, flash, request, abort , jsonify
from flask_bootstrap import Bootstrap5
# from flask_ckeditor import CKEditor
# from flask_gravatar import Gravatar
# from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required, current_user
# from flask_sqlalchemy import SQLAlchemy
from functools import wraps
# from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy.orm import relationship, mapped_column, DeclarativeBase, Mapped
# from sqlalchemy import ForeignKey, Integer
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, ValidationError, RadioField, IntegerField
from wtforms.validators import DataRequired, Email, length
from time import sleep
import requests
import json 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
Bootstrap5(app)

answer_question_dict = {}


# files = [
#     ('file', ('file', open('1.0.pdf', 'rb'), 'application/octet-stream'))
# ]

api_key = "sec_qZYPzLfgwv2bapxOVP6vXnE9gzULdL9z"

# headers = {
#     'x-api-key': api_key
# }

# response = requests.post(
#     'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)


# source_id = str(response.json()['sourceId'])
source_id = "src_N5oWn6hEUfsIjWu0YtYOC"
class chat_form(FlaskForm):
    query = StringField(validators=[DataRequired()])
    submit = SubmitField("Ask")
    
anser_dict = {}

@app.route("/", methods = ["POST", "GEt"])
def home():
    form = chat_form()
    if request.method == 'POST':
        if request.form.get("query") != "":
            d = request.form.get("query")
            headers = {
            'x-api-key': api_key,
            "Content-Type": "application/json",
            }
            sr_id = "src_3iUmYHzF4AFnzL6libjq6"
            data = {
                'sourceId': source_id,
                'messages': [
                    {
                        'role': "user",
                        'content': str(d),
                    }
                ]
            }
            response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)
            
            # d = "HEllO"
            # answer_question_dict[d] = "Do you have any specific questions or information you would like me to find for you?"
            answer_question_dict[d] = response.json()['content']
            # {'hello': 'Do you have any specific questions or information you would like me to find for you?'}
            # print("Answer Set",answer_question_dict)
            # print(response.json()['content'])
            # sleep(3)
            # return jsonify(response.json()['content'])
            return jsonify(answer_question_dict[d])
    return render_template("index.html", form = form, data_list = answer_question_dict)

if __name__ == "__main__":
    app.run(debug= True, port=5002)

