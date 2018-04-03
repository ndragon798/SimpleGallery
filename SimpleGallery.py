from flask import Flask, render_template, request, redirect, flash, Markup, send_from_directory
import os
app = Flask(__name__)
app.config.from_object(__name__)

users=[]
for root, subdirs, files in os.walk('./static/users'):
	users.append(root)
users.sort()
print(users)
users.pop(0)

@app.route("/<user>")
def userpage(user=''):
	img_loc=[]
	for root,subdirs,files in os.walk('./static/users/'+user):
		print(files)
		img_loc=files
	return render_template('user.html',img_loc=img_loc,user=user)

@app.route("/")
def main():
	print(users)
	return render_template('main.html',users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True,debug=True)