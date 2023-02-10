class AI:
    def __init__(self):
        self.questions = {
            "wie geht es dir?": "Mir geht es gut, danke der Nachfrage!",
            "was machst du?": "Ich bin ein Chatbot mit Künstlicher Intelligenz, ich helfe Benutzern bei Fragen.",
            "wie ist das Wetter heute?": "Das Wetter ist heute schön.",
            "was ist dein Lieblingsbuch?": "Ich bin ein KI-Modell und habe keine Emotionen oder Vorlieben, aber eines der bekanntesten Bücher ist '1984' von George Orwell.",
            "was ist deine Lieblingsfarbe?": "Ich bin ein KI-Modell und habe keine Emotionen oder Vorlieben, aber blau ist eine beliebte Farbe.",
        }

    def respond(self, query):
        query = query.lower()
        if query in self.questions:
            return self.questions[query]
        else:
            return "Entschuldigung, ich verstehe die Frage nicht."

ai = AI()

while True:
    query = input("Sie: ")
    response = ai.respond(query)
    print("AI: ", response)
