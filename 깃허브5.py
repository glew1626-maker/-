import random
from datetime import datetime


def read_pir_sensor():
    """
    PIR 모션 센서 데이터
    True : 움직임 감지
    False : 움직임 없음
    """
    return random.choice([True, False])


def read_accelerometer():
    """
    가속도 센서(X, Y, Z)
    """
    x = round(random.uniform(-2.0, 2.0), 2)
    y = round(random.uniform(-2.0, 2.0), 2)
    z = round(random.uniform(8.5, 10.5), 2)

    return x, y, z


def read_smartwatch():
    """
    스마트워치 데이터
    """

    heart_rate = random.randint(55, 120)

    steps = random.randint(0, 10000)

    return heart_rate, steps


def get_sensor_data():

    pir = read_pir_sensor()

    x, y, z = read_accelerometer()

    heart_rate, steps = read_smartwatch()

    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "motion": pir,
        "acc_x": x,
        "acc_y": y,
        "acc_z": z,
        "heart_rate": heart_rate,
        "steps": steps
    }


if __name__ == "__main__":

    sensor = get_sensor_data()

    print("===== 센서 데이터 =====")
    print(f"시간 : {sensor['time']}")
    print(f"움직임 : {sensor['motion']}")
    print(f"가속도 X : {sensor['acc_x']}")
    print(f"가속도 Y : {sensor['acc_y']}")
    print(f"가속도 Z : {sensor['acc_z']}")
    print(f"심박수 : {sensor['heart_rate']} bpm")
    print(f"걸음 수 : {sensor['steps']}")