import asyncio
import edge_tts
from config import VOZ_TTS

class TTSEngine:
    async def _generar_async(self, texto: str, salida: str):
        communicate = edge_tts.Communicate(texto, VOZ_TTS)
        await communicate.save(salida)

    def generar_audio(self, texto: str, salida: str):
        print(f"🎙️ Generando locución neuronal: '{texto[:35]}...'")
        asyncio.run(self._generar_async(texto, salida))
