from database import connector
from flask import Flask, request, session, render_template
from flask.wrappers import Response
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/create_message', methods = ['GET'])
def create_test_message():
    db_session = db.getSession(engine)
    message = entities.Message(
            message = "Final exam in progress",
            topic = "SE",
            )
    db_session.add(message)
    db_session.commit()

    return "¡Message created!"

@app.route('/message', methods = ['POST'])
def create_message():
    try:
        message = json.loads(request.data)
        message = entities.Message(
            message=message['message'],
            topic=message['topic']
        )
        session = db.getSession(engine)
        session.add(message)
        session.commit()

        return Response(status=200, mimetype='application/json')
    except Exception:
        return Response(status=401, mimetype='application/json')

@app.route('/message/<topic>', methods = ['GET'])
def get_messages(topic):
    db_session = db.getSession(engine)
    
    db_response = db_session.query(entities.Message).filter(entities.Message.topic == topic)
    messages = db_response[:]

    if len(messages) > 0:
        return Response(json.dumps(messages, cls=connector.AlchemyEncoder), mimetype='application/json')
    else:
        message = {'status': 404, 'message': 'Not Found'}

        return Response(message, status=404, mimetype='application/json')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug=True,port=8080, threaded=True, host=('127.0.0.1'))
