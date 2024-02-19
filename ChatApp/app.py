from flask import Flask, request, redirect, render_template, session, flash, abort
from datetime import timedelta
import hashlib
import uuid
import re

from models import dbConnect


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days = 30)


# # サインアップページの表示
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('registration/signup.html')

# # サインアップ処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    pattern = "^[a-z0-9_+-]+(\.[a-z0-9_+-]+)*[a-z0-9_+-]+@[a-z]+(\.[a-z]+)*\.[a-z]+$" 
    
    if name == '' or email =='' or password == '':
        flash('からのふぉーむがあるようです')
    elif re.match(pattern, email) is None: 
        flash('正しいめーるあどれすの形式ではありません')
    else:
        uid = uuid.uuid4() 
        password = hashlib.sha256(password.encode('utf-8')).hexdigest() 
        DBuser = dbConnect.getUser(email) 

        if DBuser != None: 
            flash('このめーるあどれすはすでに登録されているようです')
        else:
            dbConnect.createUser(uid, name, email, password)
            UserId = str(uid) 
            session['uid'] = UserId 
            return redirect('/') 
    return redirect('/signup') 


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
