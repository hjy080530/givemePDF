import subprocess
from PIL import Image

def capture_with_macos_tool():
    path = "/tmp/drag_capture.png"
    subprocess.run(["screencapture", "-i", path])
    return Image.open(path)