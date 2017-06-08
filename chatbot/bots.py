import os
from chatterbot import ChatBot


def load_chatbot(botname, servername, port, workdir):
    """
    Load chatbot, three kinds available:
    - English: a standard bot trained on english corpus
    - Zen: telling Python Zen
    - Math: can calculate simpple math
    """
    db_path = os.path.join(workdir, "{}_{}_database.db".format(servername, port))
    if botname == "English":
        bot = ChatBot('English',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            silence_performance_warning=True,
            database=db_path)
        bot.train("chatterbot.corpus.english")
    elif botname == "Zen":
        bot = ChatBot(
            'Python Zen',
            storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
            logic_adapters=[
                { 'import_path': 'chatterbot.logic.BestMatch'},
                { 'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                   'threshold': 0.2,
                   'default_response': 'I am sorry, but I do not understand.'}
                ],
            trainer='chatterbot.trainers.ListTrainer',
            silence_performance_warning=True,
            database=db_path
            )
        bot.train([
            "Beautiful is better than ugly.",
            "Explicit is better than implicit.",
            "Simple is better than complex.",
            "Complex is better than complicated.",
            "Flat is better than nested.",
            "Sparse is better than dense.",
            "Readability counts.",
            "Special cases aren't special enough to break the rules.",
            "Although practicality beats purity.",
            "Errors should never pass silently.",
            "Unless explicitly silenced.",
            "In the face of ambiguity, refuse the temptation to guess.",
            "There should be one-- and preferably only one --obvious way to do it.",
            "Although that way may not be obvious at first unless you're Dutch.",
            "Now is better than never.",
            "Although never is often better than *right* now.",
            "If the implementation is hard to explain, it's a bad idea.",
            "If the implementation is easy to explain, it may be a good idea.",
            "Namespaces are one honking great idea -- let's do more of those!"
            ])
    elif botname == "Math":
        bot = ChatBot(
            "Math & Time Bot",
            logic_adapters=[
                "chatterbot.logic.MathematicalEvaluation",
            ],
            input_adapter="chatterbot.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.output.OutputAdapter",
            silence_performance_warning=True,
            database=db_path
            )
    else:
        raise ValueError("Unknown bot {}".format(botname))
    return bot
