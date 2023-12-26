# 모터 토크, rpm 계산기
# 속도(m/s), 반지름(cm), (출력와트)w
def TorqueAndRpmCalcul(vel, r, w):
    print("입력 값: 속도 %sm/s, 반지름 %scm, 출력 와트 %sw" % (vel, r, w))
    rpm = vel * 60 / (2 * 3.141592 * (r / 100))
    t = (w * 1000) / (1.027 * rpm)  # 와트를 와트초로 변환
    print("rpm:", rpm)
    print("torque:", t)
    print("1초당 회전속도:", rpm / 60)
    print("-------------------")

# 로봇의 무게(kg), 바퀴 반지름(cm), 최대속도 1초당 바퀴 회전속도(rad/s)
def MotorSelect(m, d, vel, t):
    # 관성 모멘트 원판형이기에 / 2
    print("입력 값: 질량 %skg, 반지름 %scm, 최대속도 %srad/s, 가속시간 %ss" % (m, d, vel, t))
    load_moment = m * d * d / 8 
    acc_torque = load_moment / 981 * 2 * 3.141592 * vel / t
    # 0.1 마찰계수
    vel_torque = 0.1 * m * d / 4
    result_torque = acc_torque + vel_torque

    print("부하 관성 모멘트:", load_moment)
    print("가속토크:", acc_torque)
    print("등속 토크:", vel_torque)
    print("최소 토크:", result_torque)
    print("즉, 안전계수 1.5를 곱한", result_torque * 1.5, "kgcm의 토크를 충족하는 모터를 사야합니다.")

# 초당 회전수, 바퀴 반지름, 출력 와트 (여기서는 10 와트로 가정)
TorqueAndRpmCalcul(2.638, 4.5, 10)

# 로봇이 3접점일 경우 m을 3으로 나눈 값을 넣어라
# 질량, 반지름, 초당 회전수, 가속시간 (여기서는 2초로 가정)
MotorSelect(4. , 4.5, 2., .1)
