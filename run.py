from flask import Flask
from app import create_app

if __name__ == '__main__':
    myapp = create_app()
    myapp.run(debug=True)
    # app.run(host='0.0.0.0',debug=False, port=80)