import subprocess
ffmpeg_path = 'C:\\ffmpeg-6.1.1-essentials_build\\bin\\ffmpeg.exe'
io_path = "../files/"

# Schritt 1: Halbieren der Auflösung von input.mp4 und Speichern als new.mp4
subprocess.run([
    ffmpeg_path,
    '-i', io_path + 'input.mp4',
    '-vf', 'scale=iw/2:ih/2', # Video-Filter zum Halbieren der Auflösung
    '-af', 'volume=0.60',  # Lautstärke auf 60% reduzieren
    '-c:v', 'libx264',  # Beibehaltung des H.264 Video-Codecs
    '-preset', 'medium',  # Ein guter Ausgleich zwischen Geschwindigkeit und Qualität
    '-crf', '23',  # Standard CRF-Wert für libx264, niedrigere Werte für bessere Qualität
    '-c:a', 'aac',  # Beibehaltung des AAC Audio-Codecs
    '-strict', '-2',  # Manchmal notwendig, um AAC zu aktivieren
    io_path + 'new.mp4'
])

# Schritt 2: Konvertieren von new.mp4 zu output.webm
subprocess.run([
    ffmpeg_path,
    '-i', io_path + 'new.mp4',
    '-c:v', 'libvpx-vp9',  # Video-Codec für VP9
    '-crf', '30',  # CRF-Wert für VP9, anpassbar für Qualität, (15-35) niedriger ist bessere Q
    '-b:v', '0',  # Bitrate, '0' für CRF-gesteuerte Bitrate
    '-c:a', 'libvorbis',  # Audio-Codec für WebM
    io_path + 'output.webm'
])

# Schritt 3: Konvertieren von new.mp4 zu output.ogv
subprocess.run([
    ffmpeg_path,
    '-i', io_path + 'new.mp4',
    '-c:v', 'libtheora',  # Video-Codec für Theora
    '-q:v', '6',  # Qualitätslevel für Theora, anpassbar, (0-10) höher ist bessere Q
    '-c:a', 'libvorbis',  # Audio-Codec für OGV
    io_path + 'output.ogv'    
])