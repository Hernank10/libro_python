class Database:
    def __init__(self):
        self.modulos = [
            {"id": 1, "titulo": "Pronombres Personales", "regla_es": "Sujeto de la oración", "regla_en": "Subject pronouns", "ejemplo": "I am a teacher"},
            {"id": 2, "titulo": "Verbo To Be", "regla_es": "Ser o Estar", "regla_en": "Am, Is, Are", "ejemplo": "She is happy"}
        ]
        self.lecciones = []

db = Database()
