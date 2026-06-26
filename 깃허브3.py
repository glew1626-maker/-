import csv
import os
from datetime import datetime

DATA_FILE = "data/sample_activity.csv"

def load_activity_data():
    activities = []

    if not os.path.exists(DATA_FILE):
        return activities

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            activities.append(row)

    return activities


def check_abnormal_behavior():

    activities = load_activity_data()

    if len(activities) == 0:
        return False

    current_hour = datetime.now().hour

    # 밤 12시 ~ 새벽 5시 활동 여부
    if 0 <= current_hour <= 5:
        print("야간 활동 감지")
        return True

    # 활동량 확인
    activity_count = len(activities)

    if activity_count < 3:
        print("활동량 부족")
        return True

    # 기상 시간 확인
    for activity in activities:

        if activity["activity"] == "wake":

            wake_hour = int(activity["time"].split(":")[0])

            if wake_hour >= 12:
                print("기상 시간 이상")
                return True

    # 식사 여부 확인
    meal_count = 0

    for activity in activities:

        if activity["activity"] in ["breakfast", "lunch", "dinner"]:
            meal_count += 1

    if meal_count < 2:
        print("식사 누락 감지")
        return True

    return False


if __name__ == "__main__":

    if check_abnormal_behavior():
        print("이상행동 발생")
    else:
        print("정상 상태")