from flask import Flask,render_template,request,redirect
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/' , methods=['GET','POST'])
def root():
   return redirect('/login')
    

@app.route('/login' , methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return render_template('registration/login.html')
    
    else:
        return render_template('registration/login.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        return redirect('/login')
    else:
        return render_template('registration/signup.html')
    
    
@app.route('/passwordlost', methods=['GET','POST'])
def password():
    if request.method == 'POST':
        return redirect('/login')
    else:
        return render_template('registration/passwordlost.html')
    
@app.route('/home')
def home():
    return render_template('home.html')
