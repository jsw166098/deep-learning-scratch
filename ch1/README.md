
# 1. 파이썬 
## 1.1 외부 라이브러리
* 파이썬3
* 넘파이
* matplotlib

> 넘파이는 수치계산용 라이브러리로 행렬 계신시 편리하다.
> matplotlib은 그래프를 글주는 라이브러리로 실험 결과를 시각화하거나 딥러닝 실행 과정의 중간 데이터를 시각적으로 확인하기 위해 필요하다

## 1.2 아나콘다 다운로드
<http://www.continuum.io/downloads>

## 1.3 파이썬 인터프리트
__파이썬대화모드__

### 1.3.1 산술 연산
~~~
#뺄셈
1 - 2
>> -1

#곱셈
4 * 5
>> 20

#나눗셈
7 / 5
>> 1.4

#거듭제곱
3 ** 2
>> 9
~~~


### 1.3.2 자료형
자료형은 데이터의 성질을 의미한다.파이썬에서는 type()함수로 데이터의 자료형을 파악할 수 있다. 자료형과 클래스를 같은 의미로 사용하기도 한다.
~~~
>>>type(10)
<class 'int'>
>>>type(1.356)
<class 'float'>
>>>type("hello")
<class 'str'>
~~~

자료형에 따라 사용할 수 있는 연산자가 다르다.
~~~
숫자 -> +,-,/ 등의 산순 연산자
bool -> and, or, not 등의 논리 연산자
~~~

### 1.3.3 변수
변수는 데이터를 저장하는 그릇이다.

파이썬은 __동적언어__ 이다. 동적 언어란 변수의 자료형을 명시하지 않아도 상황에 __맞게 자동으로 결정__ 하는 것이다. 이를 자동 형변환 이라고 한다.

### 1.3.4 리스트
* 원소 접근시 [] 인덱스 이용
* 스라이싱 사용 가능, 리스트 안의 특정 원소 하나 또는 부분 리스트에 접근 가능
~~~
>>> a = [1,2,3,4,5]  #리스트 생성
>>> print(a)  #리스트 출력
[1,2,3,4,5]

>>>len(a)  #리스트 길이 출력
5

>>> a[0] # 리스트 하나의 원소에 접근
5

>>> a[4] = 99
>>> print(a)
[1,2,3,4,99]

>>>a[0:2]  #인덱스 0에서 부터 하나 앞인 1까지 원소를 꺼낸다.
[1,2]

>>>a[1:]  #인덱스 1부터 끝까지 얻기
[2,3,4,99]

>>>a[:3]  #처음부터 마지막 원소의 1개 앞까지 얻기
[1,2,3,4]

>>>a[:-1]  #-1은 마지막 원소
[1,2,3,4]

>>>a[:-2]  #-2는 마지막 원소에서 한 개 앞의 원소에 해당된다.
[1,2,3]
~~~

### 1.3.5 딕셔너리
* 키와 값으로 한 쌍의 데이터를 저장한다. 반면 리스트는 인덱스 번호 순으로 값을 저장한다.
~~~
>>> me = {'height':100}  #덱셔너리 생성, 딕셔너리 명 = {'키' : 값}
>>> me['height']
180

>>> me['weight'] = 70
>>> print(me)
{'weight' : 70, 'height': 180}
~~~

### 1.3.6 bool
* True(참), False(거짓) 중 하나의 값을 가지는 자료형
* and, or, not 논리 연산자 사용
~~~
>>> hungry = True
>>> sleepy = False
>>> type(hungry)
<class 'bool'>

>>>not hungry
False

>>>hungry and sleepy  # and 연산
False

>>>hungry or sleepy  # or 연산
True

~~~

### 1.3.7 if 문
~~~
>>> hungry = True
>>> if hungry:
...    print('I'm hungry')
...
I'm hungry

>>>hungry = False
>>>if hungry:
...    pirnt("I'm hungry")
...else:
...    print('I'm not hungry')
...    print('I'm sleepy')
I'm not hungry
I'm sleepy
~~~

### 1.3.8 for 문
~~~
>>> for i in[1,2,3]:
...     print(i)
... 
1
2
3
~~~

### 1.3.9 함수
일련의 명령어들을 묶어 하나의 함수로 정의 가능하다

```
>>> def hello():
...     print("Hello World!")
... 
>>> hello()
Hello World!
```
인수를 취할 수 있다.
~~~
>>> def hello(object):
...     print("Hello "+object+"!")
... 
>>> hello("cat")
Hello cat!
~~~

## 1.4 클래스
* 개발자는 직접 클래스를 정의하여 독자적인 자료형을 만들 수 있다. 
* 클래스만의 전용 함수(메서드)와 속성을 정의한다.
* 생성자(__init__ 메서드)는 클래스의 인스턴스가 만들어질 때 한번만 불린다.
~~~
class 클래스 이름:
    def __init__(self, 인수, ...):  #생성자
     ...
    def 메서드 이름 1(self, 인수, ...):  #메서드1
     ...
    def 메서드 이름2(self, 인수, ...):  #메서드2
     ...
~~~

## 1.5 넘파이
딥려닝의 배열, 행렬 계산을 편라하게 해준다.

### 1.5.1 넘파이 가져오기
~~~
import numpy as np
~~~

* numpy를 np 이름을 가져온다.
* numpy에서 제공하는 메서드를 np를 통해 참조할 수 있다. 

### 1.5.2 넘파이 배열 생성

* np.array() 메서드 사용
* np.array()는 리스트를 인수로 받아 넘파이가 제공하는 특수 형태 배열(numpy.ndarray)을 반환한다.

~~~
>>> x = np.array([1.0, 2.0, 3.0])  #넘파이 배열 생성
>>> print(x)
[1. 2. 3.]

>>> type(x)  
<class 'numpy.ndarray'>  #넘파이 배열(numpy.ndarray) 클래스
~~~

### 1.5.3 넘파이 산술 연산
* 원소의 개수가 같은 경우 연산하며 다를 경우 오류 발생
* 원소마다 인덱스 별로 산술 연산 실행

~~~
>>> y=np.array([2.0, 4.0, 6.0])
>>> x+y
array([3., 6., 9.])

>>> x-y
array([-1., -2., -3.])

>>> x*y
array([ 2.,  8., 18.])

>>> x/y
array([0.5, 0.5, 0.5])

>>> x/2.0  #브로드 캐스트 
array([0.5, 1. , 1.5])
~~~

1.5.4 넘피이의 N차원 배열

2차원 배열(행렬)
~~~
>>> A = np.array([[1,2], [3,4]])
>>> print(A)
[[1 2]
 [3 4]]
 
>>> A.shape #배열의 형상(배열의 각 차원의 크기) 
(2, 2)

>>> A.dtype
dtype('int64')  #행렬의 담긴 자료형
~~~

2차원 배열
~~~
>>> B = np.array([[3,0],[0,6]])
>>> A+B
array([[ 4,  2],
       [ 3, 10]])
       
>>> A*B
array([[ 3,  0],
       [ 0, 24]])
       
>>> A*10  #브로드 캐스트
array([[10, 20],
       [30, 40]])
~~~

~~~
1차원 배열-> 벡터
2차원 배열 -> 행렬
벡터와 행렬 일반화 -> 텐서
~~~

### 1.5.5 브로드 캐스트
* 형상이 다른 배열끼리 계산하는 넘파이가 제공하능 기능
* 크기가 작은 배열에서 복제되어 연산이 이루어진다.

~~~
>>> A = np.array([[1,2], [3,4]])
>>> B = np.array([10, 20])  #1열이 2열에 복제되어 연산된다. 
>>> A*B
array([[10, 40],
       [30, 80]])
~~~

### 1.5.6 원소 접근

인덱스로 접근
~~~
>>> X = np.array([[51, 55], [14, 19], [0,4]])
>>> print(X)
[[51 55]
 [14 19]
 [ 0  4]]
 
>>> X[0]
array([51, 55])

>>> X[0][1]
55
~~~

for 문으로 접근
~~~
>>> for row in X:
...     print(row)
... 
[51 55]
[14 19]
[0 4]
~~~

~~~
>>> X = X.flatten()  #1차원 배열로 전환, 평탄화
>>> print(X)
[51 55 14 19  0  4]

>>> X[np.array([0,2,4])]
array([51, 14,  0])

>>> X>15  #넘파이 배열에 부등호 연산자 사용시 결과는 bool 데이터가 담긴 넘파이 배열이다.
array([ True,  True, False,  True, False, False])

>>> X[X>15]
array([51, 55, 19])
~~~

## 1.6 matplotlib
그래프를 그리는 라이브러리로 딥러닝 실험에서 다음과 같은 작업을 하기 위해 사용된다.
* 그래프 그리기
* 데이터 시각화

### 1.6.1 단순한 그래프 그리기

matplotlib의 pyplot 모듈사용
~~~
import numpy as np
import matplotlib.pyplot as plt

#데이터 준비
x = np.arange(0,6,0.1)  #0에서 6까지 0.1 간격으로 생성
y = np.sin(x)

#그래프 그리기
plt.plot(x ,y)
plt.show()
~~~

### 1.6.2 pyplot의 기능
~~~
import numpy as np
import matplotlib.pyplot as plt

#데이터 준비
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#그래프 그리기
plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle="--" ,label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()
~~~

1.6.3 이미지 표시하기
~~~
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png')  #이미지 불러오기

plt.imshow(img)
plt.show()
~~~


