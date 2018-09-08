from flask import Flask
from yattag import Doc
from flask import request, render_template
import base64
import json
from imgproc import convertImgtoInfo

app = Flask(__name__)

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

def convertBase64toJPG(base64):
    image_64_encode = image_64_encode.encode()
    image_64_decode = base64.decodestring(image_64_encode) 
    image_result = open('fuckme.jpg', 'wb') 
    image_result.write(image_64_decode)
    return 


@app.route('/',methods=["GET"])
def index():
    generate_code()
    return app.send_static_file('index.html')

@app.route('/disp',methods=["GET"])
def disp():
    return app.send_static_file('test.html')


@app.route('/getRequest',methods=["POST"])
def handle_request():
    # img = base64.decodestring(request.headers[b'Base64']) 
    # doesnt work for some reason?
    imgencoded = request.get_json()
    imgencoded = imgencoded['base64']
    f = open("static/test.html", "w")
    f.write(imgencoded)
    f.close()
    return imgencoded
    # return render_template('pic.html', txt = imgencoded)
    # image_result = open('image.jpg', 'wb')
    # image_result.write(img)
    # return str(request.headers)