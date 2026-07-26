class ScriptGenerator:
    def __init__(self, tema: str):
        self.tema = tema

    def generar(self):
        print(f"Generando guion modular para el tema: '{self.tema}'...")
        return {
            "tema": self.tema,
            "escenas": [
                {
                    "texto": "La inteligencia artificial está revolucionando la creación de contenido automatizado.",
                    "prompt_imagen": "A futuristic glowing AI brain with digital networks, cinematic lighting, 8k resolution, vertical orientation"
                },
                {
                    "texto": "Con scripts en Python podemos generar videos profesionales directo a tu disco duro.",
                    "prompt_imagen": "A modern developer workspace showing Python code on holographic screens, cyber dark mode style"
                },
                {
                    "texto": "Suscríbete para continuar aprendiendo a monetizar tus proyectos de IA.",
                    "prompt_imagen": "A sleek dark neon background with a glowing blue Play button, digital art, vertical wallpaper"
                }
            ]
        }
