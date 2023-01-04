- class 선언

  - `class ClassName(object):`
  - 클래스명은 CamelCase 사용

- attribute 추가

  - `def __init__(self, a): self.a = a`
  - 객체 초기화 예약 함수
  - `__`는 특수한 예약 함수나 변수, 함수명 변경(맨글링)으로 사용

- method 구현

  - `def MethodName(self, a):`
  - self는 생성된 인스턴스 자신을 의미함

- OOP특성

  - 상속(Inheritance)

    - 부모클래스로 부터 속성과 Methode를 물려받은 자식 클래스를 생성
    - `class Korean(Person)`
      - Korean이 Person으로부터 상속
      - super()는 부모 클래스를 의미

  - 다형성(Polymorphism)

    - 같은 이름 메소드의 내부 로직을 다르게 생성
    - Dynamic Typing 특성으로 인해 파이썬에서는 같은 부모클래스의 상속에서 주로 발생

  - 가시성(Visibility)

    - 객체의 정보를 볼 수 있는 레벨을 조절
    - 누구나 객체 안에 모든 변수를 볼 필요 없음
    - 캡슐화(Encapsulation)
      - 정보 은닉

- decorate

  - First-class objects

    - 일등함수, 일급 객체
    - 변수나 데이터 구조에 할당이 가능한 객체
    - 파라메터로 전달이 가능, 리턴 값으로 사용

  - Inner function

    - 함수 내에 또 다른 함수가 존재
    - closures
      - inner function을 return값으로 반환

  - decorator function

    - 복잡한 클로져 함수를 간단하게
