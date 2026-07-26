from moviepy import ImageClip, AudioFileClip, TextClip, CompositeVideoClip
from config import VIDEO_WIDTH, VIDEO_HEIGHT

class Compositor:
    def _aplicar_ken_burns(self, clip_imagen, duracion):
        return clip_imagen.resized(lambda t: 1 + 0.05 * (t / duracion)).with_duration(duracion)

    def crear_escena(self, ruta_imagen: str, ruta_audio: str, texto_subtitulo: str):
        # 1. Cargar audio y duración
        audio_clip = AudioFileClip(ruta_audio)
        duracion = audio_clip.duration

        # 2. Cargar imagen a pantalla completa (Cover)
        img_clip = ImageClip(ruta_imagen)
        w, h = img_clip.size
        factor = max(VIDEO_WIDTH / w, VIDEO_HEIGHT / h)
        
        img_base = img_clip.resized(factor).cropped(
            x_center=img_clip.resized(factor).w / 2,
            y_center=img_clip.resized(factor).h / 2,
            width=VIDEO_WIDTH,
            height=VIDEO_HEIGHT
        )

        video_animado = self._aplicar_ken_burns(img_base, duracion)

        # 3. Configurar subtítulos (sin 'align' para evitar errores de versión)
        ruta_fuente = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

        subtitulo = TextClip(
            text=texto_subtitulo,
            font_size=46,  # Tamaño optimizado para que las palabras largas respiren
            color='yellow',
            stroke_color='black',
            stroke_width=3,
            font=ruta_fuente,
            method='caption',
            size=(VIDEO_WIDTH - 300, None)  # Margen lateral seguro ampliado (150px a cada lado) para el borde negro
        ).with_duration(duracion).with_position(('center', 0.75))

        # 4. Componer escena
        escena_visual = CompositeVideoClip(
            [video_animado, subtitulo], 
            size=(VIDEO_WIDTH, VIDEO_HEIGHT)
        ).with_duration(duracion)

        return escena_visual.with_audio(audio_clip)
