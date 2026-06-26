from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "alert.log")


def create_log_folder():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def save_log(message):
    create_log_folder()

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")


def send_alert(user_name, danger_type, location):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
========================================
응급 알림 발생
========================================
사용자 : {user_name}
위험 유형 : {danger_type}
발생 시간 : {current_time}
발생 위치 : {location}

보호자에게 알림을 전송했습니다.
========================================
"""

    print(message)

    save_log(
        f"{current_time}, {user_name}, {danger_type}, {location}"
    )

    return True


if __name__ == "__main__":

    send_alert(
        user_name="홍길동",
        danger_type="낙상",
        location="거실"
    )