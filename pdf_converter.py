import os
from PIL import Image
from fpdf import FPDF

def convert_to_pdf(folder_name):
    pdf = FPDF()
    image_files = sorted([f for f in os.listdir(folder_name) if f.endswith(".png")])

    for file in image_files:
        path = os.path.join(folder_name, file)
        image = Image.open(path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        image_path_temp = path.replace(".png", "_temp.jpg")
        image.save(image_path_temp, "JPEG")
        pdf.add_page()
        pdf.image(image_path_temp, x=10, y=10, w=190)
        os.remove(image_path_temp)

    pdf_path = os.path.join(folder_name, "result.pdf")
    pdf.output(pdf_path, "F")