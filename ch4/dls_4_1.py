
import numpy as np

#교차 엔트로피 오차

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))  ##로그 정의역에 0을 대입하면 음의 무한대가 계산된다 이는 계산이 불가능하다. 따라서 작은 값을 더해준다.

t = [0, 0, 1, 0,0,0,0,0,0,0]  #정답 레이블(원-핫 인코딩)-> 2

## 첫번째 그림 2가 가장 높음
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]  ## 출력값(소프트맥스 결과값)
cross_entropy_error(np.array(y), np.array(t))

## 두번째 그림 7이 가장 높음
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]  ## 출력값(소프트맥스 결과값)
cross_entropy_error(np.array(y), np.array(t))


