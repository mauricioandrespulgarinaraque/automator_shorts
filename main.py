import os
import shutil
from moviepy import concatenate_videoclips
from config import TEMP_DIR, OUTPUT_DIR, FPS
from core.script_generator import ScriptGenerator
from core.tts_engine import TTSEngine
from core.ai_image_fetcher import AIImageFetcher
from core.compositor import Compositor

class MainPipeline:
    def __init__(self, tema: str):
        self.tema = tema
        self.script_gen = ScriptGenerator(tema)
        self.tts = TTSEngine()
        self.image_fetcher = AIImageFetcher()
        self.compositor = Compositor()

    def ejecutar(self):
        print("==================================================")
        print("🤖 PIPELINE MODULAR DE SHORTS (AUTOMATOR_SHORTS)")
        print("==================================================")

        datos = self.script_gen.generar()
        escenas = []

        for i, escena in enumerate(datos["escenas"]):
            print(f"\n--- Procesando Escena {i+1}/{len(datos['escenas'])} ---")
            r_audio = os.path.join(TEMP_DIR, f"audio_{i}.mp3")
            r_imagen = os.path.join(TEMP_DIR, f"imagen_{i}.jpg")

            self.tts.generar_audio(escena["texto"], r_audio)
            self.image_fetcher.descargar_imagen(escena["prompt_imagen"], r_imagen)

            clip = self.compositor.crear_escena(r_imagen, r_audio, escena["texto"])
            escenas.append(clip)

        ruta_final = os.path.join(OUTPUT_DIR, "short_modular_ia.mp4")
        print(f"\n🎬 Uniendo escenas y renderizando video final hacia HDD...")
        video_final = concatenate_videoclips(escenas, method="compose")
        video_final.write_videofile(ruta_final, fps=FPS, codec='libx264', audio_codec='aac', threads=6)

        print("\n🧹 Limpiando archivos temporales locales del NVMe...")
        shutil.rmtree(TEMP_DIR)
        os.makedirs(TEMP_DIR, exist_ok=True)

        print(f"\n✅ ¡PROCESO MODULAR FINALIZADO EXITOSAMENTE!")
        print(f"📂 Archivo de video disponible en:\n👉 {ruta_final}\n")

if __name__ == "__main__":
    pipeline = MainPipeline(tema="Monetización Automática Modular con Python")
    pipeline.ejecutar()
