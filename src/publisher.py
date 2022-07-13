import requests

# End point to POST message
API_ENDPOINT = 'http://127.0.0.1:8080/message'

class Publisher():
    def __init__(self) -> None:
        pass
    
    def send_message(self, message: str, topic: str):
        data = {
                'message': message,
                'topic': topic
                }

        response = requests.post(url = API_ENDPOINT, json = data)

        print(response)

if __name__ == '__main__':
    publisher = Publisher()
    message = input('Message:')
    topic = input('Topic:')
    publisher.send_message(message, topic)
