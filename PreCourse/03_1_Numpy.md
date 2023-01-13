- numpy

  - Numerical Python
  - 파이썬의 고성능 과학 계산용패키지
  - Matrix와 Vector와 같은 Array 연산의 사실상의 표준

  - 일반 List에 비해 빠르고, 메모리 효율적
  - 반복문 없이 데이터 배열에 대한 처리를 지원
  - 선형대수와 관련된 다양한 기능 제공

  - `immport numpy as np`

    - numpy의 호출 방법
    - 일반적으로 np라는 alias(별칭) 사용

  - array creation
    - np.array 함수를 활용 배열을 생성 -> ndarray
    - 하나의 데이터 type만 배열에 넣울 수 있음
      - dynamic typing not supported

- shape

  - numpy array의 dimension 구성을 반환
  - array의 RANK에 따라 불리는 이름이 있음
    - 0 : scalar
    - 1 : vector
    - 2 : matrix
    - n : n-tensor

- ndim

  - number of dimensions

- size

  - data의 개수

- dtype

  - numpy array의 데이터 type을 반환
  - ndarray의 single element가 가지는 data type
  - 각 element가 차지하는 memory의 크기가 결정됨

- nbytes

  - ndarray object의 메모리 크기를 반환

- reshape

  - array의 shape의 크기를 변경
  - element의 갯수는 동일
  - -1 : size를 기반으로 row 개수 선정

- flatten

  - 다차원 array를 1차원 array로 변환

- indexing

  - list와 달리 이차원 배열에서 [0,0] 표기법을 제겅
  - matrix일 경우 앞은 row 뒤는 column을 의미

- slicing

  - list와 달리 행과 열 부분을 나눠서 slicing이 가능
  - matirx의 부분 집합을 추출할 때 유용

- arange

  - array의 범위를 지정하여 값의 list를 생성하는 명령어
  - `(시작, 끝, step)`
  - reshape과 함께 사용 가능

- zeros, ones

  - 0, 1로 가득찬 ndarray 생성
  - `(shape, dtype, order)`

- empty

  - shape만 주어지고 비어있는 ndarray 생성
  - memory initialization이 되지 않음

- something_like

  - 기존 ndarray의 shape 크기 만큼 1, 0 또는 empty array를 반환
  - something은 ones, zeros, empty

- identity

  - 단위 행렬을 생성

- eye

  - 대각선이 1인 행렬
  - k값으로 시작 index 변경 가능

- diag

  - 대각 행렬의 값을 추출

- random sampling

  - 데이터 분포에 따른 sampling으로 array를 생성

- sum

  - ndarray의 element들 간의 합을 구함
  - list의 sum 기능과 동일
  - axis값으로 기준 설정 가능
  - mean
    - 평균 반환
  - std
    - 표준 편차 반환

- axis

  - 모든 operation function을 실행할 때 기준이 되는 dimension 축

- mathematical functions

  - 그 외에도 다양한 수학 연산자 제공
  - np.something 호출

- concatenate

  - numpy array를 합치는(붙이는) 함수
  - axis값으로 기준 설정 가능
  - vstack
    - vertical 기준
  - hstack
    - horizontal 기준

- Operations b/t arrays

  - numpy는 array 같의 기본적인 사칙 연산을 지원

- Element-wise operations

  - array간 shape이 같을 때 일어나는 연산

- Dot product

  - matrix의 기본 연산
  - dot 함수 사용

- transpose

  - transpose 또는 T attribute 사용

- broadcasting

  - shape이 다른 배열 간 연산을 지원
  - scalar-vector 외에도 vector-matrix 간의 연산도 지원

- all, any

  - array의 데이터 전부(and) 혹은 일부(or)가 조건에 만족 여부 반환

- comparison operation

  - numpy는 배열의 크기가 동일할 때 element간 비교의 결과를 boolean type으로 반환
  - logical_and
    - and 조건의 condition
  - logical_not
    - not 조건의 condition
  - logical_or
    - or 조건의 condition

- np.where

  - where(condition, TRUE, FALSE)
  - TRUE, FALSE 생략시 index 값 반환
  - isnan
    - not a number
  - isfinite
    - is finite number

- argmax, argmin

  - array내 최대값 또는 최소값의 index를 반환
  - axis값으로 기준 반환

- boolean index

  - 특정 조건에 따른 값을 배열 형태로 추출
  - comparison operation 함수들도 모두 사용 가능

- fancy index

  - numpy는 array를 index value로 사용해서 값 추출
  - take
  - matrix 형태의 데이터도 가능

- loadtxt, savetxt

  - text type의 데이터를 읽고, 저장하는 기능
