from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

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
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
#######
@app.route("/js")
def js():
   return render_template("js.html")
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
