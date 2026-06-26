import cv2
from fall_detection import detect_fall
from abnormal_behavior import check_abnormal_behavior
from alert import send_alert

print("===================================")
print(" AI 기반 고령자 낙상 감지 시스템 ")
print("===================================")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

print("프로그램이 시작되었습니다.")
print("ESC 키를 누르면 종료됩니다.")

while True:

    ret, frame = cap.read()

    if not ret:
        print("카메라 오류")
        break

    # 낙상 감지
    fall = detect_fall(frame)

    # 이상행동 감지
    abnormal = check_abnormal_behavior()

    if fall:
        print("낙상 감지!")

        send_alert(
            user_name="홍길동",
            danger_type="낙상",
            location="거실"
        )

    if abnormal:
        print("이상행동 감지!")

        send_alert(
            user_name="홍길동",
            danger_type="이상행동",
            location="침실"
        )

    cv2.imshow("AI Elder Care System", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("프로그램이 종료되었습니다.")