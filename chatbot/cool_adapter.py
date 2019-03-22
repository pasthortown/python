from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import requests

class MyLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyLogicAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        response = requests.get('http://www.yavirac.edu.ec/ignug/server/persona/leer?id='+statement.text)
        data = response.json()

        # Randomly select a confidence between 0 and 1
        confidence = 1
        # For this example, we will just return the input as output
        selected_statement = Statement(data[0]['identificacion'])
        selected_statement.confidence = confidence

        return selected_statement