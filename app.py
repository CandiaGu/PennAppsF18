from flask import Flask
from yattag import Doc
from flask import request, render_template
import base64
import json
# from imgproc import convertImgtoInfo
# from selenium import webdriver

app = Flask(__name__)
driver = webdriver.Chrome()

def format_style(d):
	s = ""
	for key in d: s = s+key+':'+d[key]+';'
	return s

def generate_code():
    # with open('example.json') as f:
    # 	data = json.load(f)    

    convertBase64toJPG()


    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('body'):
            for ui_element in data:
	            element = ui_element['element']
	            style = format_style(ui_element['style'])
	            klass = ui_element['class'] if ('class' in ui_element) else  'default'
	            with tag(element, style = style, klass = klass):
	                if('text' in ui_element): text(ui_element['text'])

    print(doc.getvalue())
    f = open("static/index.html", "w")
    f.write(doc.getvalue())
    f.close()


@app.route('/',methods=["GET"])
def index():
    generate_code()
    return app.send_static_file('index.html')

@app.route('/disp',methods=["GET"])
def disp():
    return render_template('test.html')


@app.route('/getRequest',methods=["POST"])
def handle_request():
    imgencoded = request.get_json()
    imgencoded = imgencoded['base64']
    imgencoded = imgencoded.encode()
    imgencoded = base64.decodestring(imgencoded) 
    image_result = open('static/img_2_proccess.jpg', 'wb') 
    image_result.write(imgencoded)
    return "yes"


    # driver.get("http://pennappsuiapp.herokuapp.com/disp");  

    # return render_template('pic.html', txt = imgencoded)
    # image_result = open('image.jpg', 'wb')
    # image_result.write(img)
    # return str(request.headers)

