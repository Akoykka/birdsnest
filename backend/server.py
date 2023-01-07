from flask import Flask
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

@app.route('/data')

def get_time():

		#Returning an api for showing in reactjs
		return {
			'Name':"Skoge","Phone":"0400123","Email":"email@gmail.com",
			"closest dist":"9m","Timestamp":"14:12"
		}
if __name__ == '__main__':
	app.run(debug=True)