
import numpy as np

# 최소 제곱 오차
def mean_sqared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t = [0, 0, 1, 0,0,0,0,0,0,0]  #정답 레이블(원-핫 인코딩)-> 2

## 첫번째 그림 2가 가장 높음
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]  ## 출력값(소프트맥스 결과값)
mean_sqared_error(np.array(y), np.array(t))

## 두번째 그림 7이 가장 높음
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]  ## 출력값(소프트맥스 결과값)
mean_sqared_error(np.array(y), np.array(t))

