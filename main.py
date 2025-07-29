from capture import get_capture_area, create_save_folder, get_capture_settings, preview_capture, capture_loop
from pdf_converter import convert_to_pdf

def main():
    x1, y1, x2, y2 = get_capture_area()
    folder = create_save_folder()
    count, interval = get_capture_settings()
    preview_capture(x1, y1, x2, y2)

    input("확인하셨다면 enter를 눌러주세요.")
    capture_loop(x1, y1, x2, y2, folder, count, interval)
    convert_to_pdf(folder)
    print("PDF로 변환되었어요.")

if __name__ == "__main__":
    main()