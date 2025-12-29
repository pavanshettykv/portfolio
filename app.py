from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

def to_csv(data):			#writing data to excel sheet
	with open('database.csv', mode='a', newline='') as database2:
		email=data['email']
		subject=data['subject']
		message=data['message']
		# names = ['email', 'subject','message']
    	# csv_writer = csv.DictWriter(database2, fieldnames=names)
    	# csv_writer.writeheader()
   	 # 	csv_writer.writerow({'email': email, 'subject': subject, 'message':message}
		csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data=request.form.to_dict()
		to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'error ,,,try again'

# def to_database(data):#writing data to the notepad
# 	with open('database.csv',mode='a') as database2:
# 		email=data['email']
# 		subject=data['subject']
# 		message=data['message']
# 		file= database.write(f'email:{email}subject:{subject}messages:{message}')


# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


#to run flask app
#FLASK_APP=app.py
#flask run