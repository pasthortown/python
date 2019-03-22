from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import requests

class MyLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyLogicAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        words = ['cedula']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement):
        identificacion = statement.text.split('cedula')[1].strip().split(' ')[0]
        response = requests.get('http://www.yavirac.edu.ec/ignug/server/persona/leer_filtrado?columna=identificacion&tipo_filtro=coincide&filtro='+identificacion)
        data = response.json()
        if response.status_code == 200:
                confidence = 1
        else:
            confidence = 0
        selected_statement = Statement('La cédula pertenece a: ' + data[0]['nombre1'] + ' ' + data[0]['nombre2'] + ' ' + data[0]['apellido1'] + ' ' + data[0]['apellido2'])
        selected_statement.confidence = confidence

        return selected_statement