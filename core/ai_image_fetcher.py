import urllib.parse
import urllib.request
from config import VIDEO_WIDTH, VIDEO_HEIGHT

class AIImageFetcher:
    def descargar_imagen(self, prompt: str, salida: str):
        print(f"🖼️ Descargando imagen IA vertical...")
        prompt_codificado = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{prompt_codificado}?width={VIDEO_WIDTH}&height={VIDEO_HEIGHT}&nologo=true&seed=101"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(salida, 'wb') as out_file:
            out_file.write(response.read())
