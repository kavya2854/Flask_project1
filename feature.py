from flask import Flask

FAI = Flask(__name__)
@FAI.route('/stringResponse')
def stringResponse():
    return 'This is the first Flask Project'
if __name__ == '__main__':
    FAI.run(debug=True)