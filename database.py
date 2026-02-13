# app/database.py
# Lógica de datos para el Centro de Innovación Pedagógica (C.I.P.A.I.)

class CIPAI_Database:
    def __init__(self):
        # 10 Módulos de Gramática Comparada (Castellano - Inglés)
        self.modulos = [
            {"id": 1, "titulo": "Ser vs. Estar | To Be", "regla_es": "Cualidades permanentes vs temporales.", "regla_en": "One verb for both states.", "ejemplo": "Soy alto / I am tall."},
            {"id": 2, "titulo": "Artículos | Articles", "regla_es": "El, La, Los, Las.", "regla_en": "The, A, An.", "ejemplo": "La casa / The house."},
            {"id": 3, "titulo": "Subjuntivo | Modals", "regla_es": "Deseos y dudas.", "regla_en": "May, Might, Should.", "ejemplo": "Espero que vengas."},
            {"id": 4, "titulo": "Por vs Para | For & To", "regla_es": "Causa vs Propósito.", "regla_en": "Duration vs Destination.", "ejemplo": "Para aprender / For learning."},
            {"id": 5, "titulo": "Voz Pasiva | Passive Voice", "regla_es": "Se impersonal o ser+participio.", "regla_en": "To be + past participle.", "ejemplo": "Se habla español / Spanish is spoken."},
            {"id": 6, "titulo": "Gerundio | Gerund", "regla_es": "Infinitivo como sujeto.", "regla_en": "-ing as a noun.", "ejemplo": "Nadar es bueno / Swimming is good."},
            {"id": 7, "titulo": "Pronombres | Pronouns", "regla_es": "Antes del verbo.", "regla_en": "After the verb.", "ejemplo": "Te lo di / I gave it to you."},
            {"id": 8, "titulo": "Tiempos Perfectos | Perfect Tenses", "regla_es": "He comido.", "regla_en": "I have eaten.", "ejemplo": "He ido al cine / I have gone."},
            {"id": 9, "titulo": "Adjetivos | Adjectives", "regla_es": "Concordancia de género.", "regla_en": "Invariant form.", "ejemplo": "Casas blancas / White houses."},
            {"id": 10, "titulo": "Falsos Amigos | False Cognates", "regla_es": "Similitud engañosa.", "regla_en": "Deceptive similarity.", "ejemplo": "Embarazada vs Embarrassed."}
        ]
        # Generación de 100 lecciones con Niveles de Gamificación
        self.lecciones = self._generar_100_lecciones()

    def _generar_100_lecciones(self):
        lecciones = []
        for m_id in range(1, 11):
            for i in range(1, 11):
                # Lógica de niveles: 4 básicos, 3 intermedios, 3 avanzados por módulo
                if i <= 4: 
                    nivel = "Básico"
                elif i <= 7: 
                    nivel = "Intermedio"
                else: 
                    nivel = "Avanzado"
                
                lecciones.append({
                    "id": len(lecciones) + 1,
                    "modulo_id": m_id,
                    "nivel": nivel,
                    "titulo": f"Lección {i}: Módulo {m_id}",
                    "tipo": "Interactivo",
                    "idioma": "Bilingüe"
                })
        return lecciones

# Instancia global de la base de datos
db = CIPAI_Database()