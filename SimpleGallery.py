from flask import Flask, render_template, request, redirect, flash, Markup, send_from_directory
import cv2
import os
app = Flask(__name__)
app.config.from_object(__name__)

users=[]
for root, subdirs, files in os.walk('./static/users'):
	users.append(root)
users.sort()
print(users)
users.pop(0)



def getposter(filename):
	cap = cv2.VideoCapture(filename)
	count = 0
	ret,frame = cap.read()
	print(filename,filename[:-4])
	cv2.imwrite(filename[:-4]+".jpg", frame)
	cap.release()
	cv2.destroyAllWindows()  # destroy all the opened windows


@app.route("/<user>")
def userpage(user=''):
	img_loc=[]
	for root,subdirs,files in os.walk('./static/users/'+user):
		print(files)
		img_loc=files
	for i in img_loc:
		if i[-4:]=='.mp4' and i[:-4]+'.jpg' not in img_loc:
			getposter('./static/users/'+user+'/'+i)
		if i[:-4]+'.jpg' in img_loc:
			del img_loc[img_loc.index(i[:-4]+'.jpg')]
	return render_template('user.html',img_loc=img_loc,user=user)

@app.route("/")
def main():
	print(users)
	return render_template('main.html',users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True,debug=True)