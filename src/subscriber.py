import requests

# End point to POST message
API : str = 'http://127.0.0.1:8080/message'

class Subscriber():
    def __init__(self) -> None:
        # Here goes the subscriber parameters
        pass
    
    def get_messages(self, topic: str):
        API_ENDPOINT = f'{API}/{topic}'

        response = requests.get(url = API_ENDPOINT)

        return response.content

if __name__ == '__main__':
    subscriber = Subscriber()
    topic = input('Topic:')
    
    messages = subscriber.get_messages(topic)

    print(messages)
