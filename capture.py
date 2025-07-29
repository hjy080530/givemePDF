import os
import time
import pyautogui

screenshot_img = None
click_coords = []
def get_capture_area():
    print("캡쳐할 영역의 좌상단(x1, y1)과 우하단(x2, y2)을 입력해주세요.")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    return x1, y1, x2, y2
def create_save_folder():
    folder_name = input("저장할 폴더 이름을 입력해주세요: ")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def get_capture_settings():
    count = int(input("페이지 수: "))
    interval = float(input("캡쳐 간격(초): "))
    return count // 2, interval

def preview_capture(x1, y1, x2, y2):
    image = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    image.show()
def capture_loop(x1, y1, x2, y2, folder_name, count, interval):
    print("3초 뒤 캡쳐를 시작합니다. 원하는 페이지를 호버해주세요.")
    time.sleep(3)
    for i in range(count):
        img = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        img_path = os.path.join(folder_name, f"capture_{i+1}.png")
        img.save(img_path)
        pyautogui.press('right')
        time.sleep(interval)