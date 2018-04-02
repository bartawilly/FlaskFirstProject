from flask import Flask, redirect, url_for, request, render_template,make_response,session
from werkzeug import secure_filename
app = Flask(__name__)
app.secret_key = 'sfkdngkshfgjlshfgjkshg'
@app.route('/')
def hello_world():
   return 'hello word'
#######
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID
#######
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'
#######
@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest
#######
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
#######
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
#######
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
#######
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)
#######
@app.route('/score/<int:score>')
def score(score):
   return render_template('score.html', marks = score)
#######
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method=='POST':
       result=request.form
   return render_template('result.html', result = result) 
#######
@app.route("/degree")
def degree():
    return render_template("degree.html")
#######
@app.route("/js")
def js():
   return render_template("js.html")
#######
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
       user = request.form['nm']
       resp = make_response(render_template('readcookie.html'))
       resp.set_cookie('userID', user)
   return resp
########  
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'
########
@app.route('/cookies')
def cookies():
   return render_template('cookies.html')
########
@app.route('/defualt')
def defualt():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
      "<b><a href = '/logout2'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login2'></b>" + \
      "click here to log in</b></a>"
########
@app.route('/login2', methods = ['GET', 'POST'])
def login2():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('defualt'))
   return '''
   <form action = "/login2" method = "POST">
      <p><input type = text name = username/></p>
      <p><input type = submit value = login></p>
   </form>
   '''
#######
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('defualt'))
#######
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
#######	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
#######	
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
