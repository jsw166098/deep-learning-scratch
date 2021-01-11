import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)  ##(60000, 784)
print(t_train.shape)  ##(60000, 10)

print(x_train.shape[0])  ##60000

# 미니배치
train_size = x_train.shape[0]
batch_size = 10  ## 훈련 데이터 10개를 뽑아서 미니 배치 학습
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

