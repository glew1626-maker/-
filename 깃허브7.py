"""
AI 기반 고령자 낙상 및 이상행동 감지 시스템
환경설정 파일(config.py)
"""

# ===============================
# 카메라 설정
# ===============================

CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# ===============================
# 낙상 감지 설정
# ===============================

FALL_HEIGHT_THRESHOLD = 0.12
NO_MOVEMENT_SECONDS = 3

# ===============================
# 이상행동 설정
# ===============================

WAKE_UP_LIMIT = 12          # 오후 12시 이후 기상
MIN_ACTIVITY_COUNT = 3      # 최소 활동 횟수
MIN_MEAL_COUNT = 2          # 최소 식사 횟수

# ===============================
# 알림 설정
# ===============================

GUARDIAN_NAME = "보호자"

ALERT_LOCATION = "거실"

ALERT_ENABLE = True

# ===============================
# 로그 설정
# ===============================

LOG_FOLDER = "logs"

DETECTION_LOG = "logs/detection.log"

ALERT_LOG = "logs/alert.log"

# ===============================
# 데이터 저장 위치
# ===============================

DATA_FOLDER = "data"

ACTIVITY_DATA = "data/sample_activity.csv"

FALL_DATA = "data/sample_fall.csv"

# ===============================
# 화면 설정
# ===============================

WINDOW_NAME = "AI Elder Care System"

FONT_SCALE = 1

TEXT_THICKNESS = 2

# ===============================
# 위험도 기준
# ===============================

LOW_RISK = 40

MEDIUM_RISK = 70

HIGH_RISK = 90

# ===============================
# 시스템 정보
# ===============================

PROJECT_NAME = "AI 기반 고령자 낙상 및 이상행동 감지 시스템"

VERSION = "1.0.0"

AUTHOR = "정은우"

UNIVERSITY = "동의대학교"

MAJOR = "컴퓨터공학과"

# ===============================
# 디버그
# ===============================

DEBUG = True