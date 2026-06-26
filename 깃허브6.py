import os
import csv
from datetime import datetime


def get_current_time():
    """
    현재 시간을 문자열로 반환
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_folder(folder_name):
    """
    폴더가 없으면 생성
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def save_csv(file_path, data):

    folder = os.path.dirname(file_path)

    if folder != "":
        create_folder(folder)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(data.keys())

        writer.writerow(data.values())


def write_log(file_path, message):

    folder = os.path.dirname(file_path)

    if folder != "":
        create_folder(folder)

    with open(file_path, "a", encoding="utf-8") as file:

        file.write(f"[{get_current_time()}] {message}\n")


def print_title(title):

    print("=" * 50)
    print(title.center(50))
    print("=" * 50)


def calculate_average(values):

    if len(values) == 0:
        return 0

    return sum(values) / len(values)


def danger_level(score):

    if score >= 90:
        return "매우 위험"

    elif score >= 70:
        return "위험"

    elif score >= 40:
        return "주의"

    else:
        return "정상"


if __name__ == "__main__":

    print_title("AI 기반 고령자 안전관리 시스템")

    print(get_current_time())

    data = {
        "time": get_current_time(),
        "activity": "walking",
        "heart_rate": 72
    }

    save_csv("data/test.csv", data)

    write_log("logs/system.log", "프로그램 시작")

    print("평균 :", calculate_average([80, 90, 85]))

    print("위험도 :", danger_level(92))