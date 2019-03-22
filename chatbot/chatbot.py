from chatterbot import ChatBot
import cool_adapter

chatbot = ChatBot(
    "Experto_ignug",

    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://localhost:27017/',
    database='chatterbot_ignug',
    
    input_adapter="chatterbot.input.TerminalAdapter",
    
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",

    logic_adapters=[
        {
            'import_path': 'cool_adapter.MyLogicAdapter'
        },
    ],
    
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    
    read_only=True,
)
DEFAULT_SESSION_ID = 1

from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("./conocimiento.yml")

while True:
    print("\nTu: ")
    input_statement = chatbot.input.process_input_statement()
    statement, response = chatbot.generate_response(input_statement, DEFAULT_SESSION_ID)
    print("\nTocayo:\n%s\n" % response)