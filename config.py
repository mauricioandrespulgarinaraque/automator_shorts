import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")

# Ruta simétrica exacta en tu disco duro SATA de 1 TB
OUTPUT_DIR = "/media/ninguno/HDD-1TB-SATA/Proyectos/01_Monetizacion_IA/automator_shorts_output"

# Asegurar directorios
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parámetros técnicos de video (Shorts / Vertical 9:16)
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 24
VOZ_TTS = "es-ES-AlvaroNeural"
FUENTE_TEXTO = "DejaVu-Sans-Bold"
