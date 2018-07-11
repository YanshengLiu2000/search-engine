from webapp import app
import os
"""
This is the entrance of our website project. 
"""
if __name__ == '__main__':
    os.environ['PYTHONHASHSEED']='0'
    """we can set the listening port number and the host ip here."""
    app.run(host = '0.0.0.0',port=8080)
