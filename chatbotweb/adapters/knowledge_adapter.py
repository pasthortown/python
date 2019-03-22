from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import requests

class KnowledgeAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(KnowledgeAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        words = ['chiste', 'broma', 'cacho', 'frase', 'célebre', 'celebre', 'cita']
        if any(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement):
        wordsBroma = ['chiste', 'broma', 'cacho']
        esBroma = False
        if any(x in statement.text.split() for x in wordsBroma):
            esBroma = True
        if esBroma:
            response = requests.get('http://192.168.20.10/knowledge/public/joke/getone')
            data = response.json()
            if response.status_code == 200:
                    confidence = 1
            else:
                confidence = 0
            selected_statement = Statement(data['content'])
            selected_statement.confidence = confidence
        else:
            response = requests.get('http://192.168.20.10/knowledge/public/phrase/getone')
            data = response.json()
            if response.status_code == 200:
                    confidence = 1
            else:
                confidence = 0
            selected_statement = Statement('"' + data['content'] + '", ' + data['author'])
            selected_statement.confidence = confidence
        return selected_statement