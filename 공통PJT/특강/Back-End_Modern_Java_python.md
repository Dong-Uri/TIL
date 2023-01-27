(정리 도움받음)

#1

Back-End: Modern Java와 Python ##모던 자바란?
함수형 프로그래밍 도입으로 큰 변화가 있었던 Java8 이후

오늘 다룰 내용
함수형과 스트림
고수준 병렬/동시성 지원
그리고 파이썬...
그리고 그리고 그리고...

Java 간략한 역사
Java1 : 1996년
가급적 LTS버전을 사용하기를 권장

Python 간략한 역사
Python 1994년

예제
문자열 리스트에서 길이가 5~10인것만 대문자로 출력하시게나
-> 단 반복문, 조건문 없이
옛날 자바 : 안될 것 같은데...
모던 자바

list.stream().filter(s -> s.length() >= 5 && s.length() <= 10).map(s -> s.toUpperCase()).forEach(System.out::println);
파이썬

[s.upper() for s in str_lst if len(s) in range(5, 11)]
함수형
함수를 일급 시민(first class citizen)에 포함 -> 사실은...
익명 클래스의 번거로움을 람다로 간편하게, 메서드 참조로 재사용
코드 블록을 주입(동작 파라미터화)하고 조합(pipeline)할 수 있게 됨
스트림의 기반, 병렬처리와 조화

주요 패키지, 클래스

@FunctionallInterface
java.util.function
Consumer, Supplier, Function, Predicate,...
Operator
기본형 Int, Long, Double
함수형 - 람다, 메서드 참조
람다(lambda) = 익명 함수, 익명 클래스를 대체
함수형 인터페이스(이름 있는 람다) : 하나의 추상 메서드를 가진 인터페이스
메서드 참조 : 메서드나 생성자를 참조하기 (::slightly_smiling_face:

예시 (문자열 리스트를 길이에 따라 정렬)
Collections.sort(words, new Comparator<String>() {
public int compare(String o1, String o2) {
return Integer.compare(o1.length(), o2.length());
});
Collections.sort(words, (o1, o2) -> Integer.compare(o1.length(), o2.length()));
Collections.sort(words, Comparator.comparingInt(String::length));
words.sort(Comparator.comparingInt(String::length));
스트림
컬렉션 + 함수형, 데이터 처리 연산을 지원하도록 소스에서 추출된 연속된 요소

외부 순환(for, while,...) VS 내부 순환(VM아 이것 좀 해줘...)
SQL처럼 선언형 스타일로 데이터를 처리
쉽게 병렬처리 적용: parallelStream 메서드
주요 패키지, 클래스, 메서드

java.util.stream
BaseStream, Stream
map(), filter(), reduce(), min() ...
C.stream(), C.parallelStream()
스트림 - 주요 개념
Predicate Function Collector/consumer
collection -> stream —-> filter —-> map ——---> collect ——-—————-> Collection

                  ——————————————————| close

중간 연산과 최종 연산
중간 연산은 스트림을 반환, 여러 연산을 조합할 수 있음
최종 연산을 스트림을 모두 소비하고 닫음
스트림은 1회용(최종 연산 이후 사용불가)
스트림 예제
직원 리스트 → 부서별 직원 리스트

Map<Department, List<Employee>> byDept = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment));
직원 리스트 → 부서별 급여 합계

Map<Department, Integer> totalByDept = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment, Collectors.summingInt(Employee::getSalary)));
좋은 직원, 안 좋은 직원 나누기

Map<Boolean, List<Employee>> byGood = employees.stream().collect(Collectors.partitioningBy(Employee::isGood));
한편 파이썬은…
원래 함수형(v1.0, since1994)

내장 컬렉션 = 리스트, 맵(딕셔너리), 튜플, 세트,…

lambda, itertools, functools, generator

예제
map, filter, reduce

from functools import reduce
reduce(lambda x, y: x + y, a)
파이썬스럽다 : List Comprehension
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

sum([m for m in [
a[i] \* b[i] for i in range(0, len(a))]
if m % 2 == 0])
병렬/동시성 concurrent
병렬이 참 좋은데.. 쉽게 할 방법이 없네…

저수준 병렬 처리의 어려움 : Thread, Lock, synchronized,…

안전하고 쉬운 병렬처리 방법 제공 → 마법은 아니야~

많이 사용되는 패턴들을 언어 차원에서 API로 지원

고수준 추상화, Thread Safety, 비동기 지원

주요 패키지, 클래스
java.util.concurrent

Executor(s), ExecutorService

xxThreadPool, ForkJoinPool

Future, CompletableFuture

Runnable, Callable

비동기 지원 Async
동기 / 비동기 and 블록 / 넌블록

작업이 끝날 때 까지 기다리기 VS 하고있어 나중에 물어볼게

Future: 비동기 연산 지원, 완료확인/대기/결과조회/취소

CompletableFuture: Future 작업 연결, 순서정의 등

면접 다수 출제 : 동기(blocking) 비동기(non block) 싱크
예제… 스프링에서
상황: 하나에 3초 정도 걸리는 API 5개를 호출해야 함

문제 → 10초 이상 대기하게 되면 사용자가 도망감

병렬이를 모르는 개발자
api.callApi(someParam); 3초
api.callApi(someParam); 3초
api.callApi(someParam); 3초
api.callApi(someParam); 3초
api.callApi(someParam); 3초
api.callApi(someParam); 3초
병렬이를 아는 개발자
여러 API 호출을 병렬로 실행

for (ApiService api : apis) {
apiResults.add(api.callApi(param));
}

for (CompletableFuture<Void> future : apiResult) {
future.get();
}
@Async
public CompletableFuture<Void> callApi(String param) {
// api를 호출
return new CompletableFuture<>();
}
한편 파이썬은… multiprocessing
파이썬은 느려요..? 일부만 맞는 얘기

GIL 문제: 스레드 활용을 제한하는 요소

multiprocessing

asyncio, coroutine

future, executors, ThreadPoolExecutor… 어? 앞에서 봤는데??

✓ future, executors, ThreadPoolExecutor.. 어 앞어서 봤는데?

with futures.ThreadPoolExecutor(max_workers=4) as executor:
future_list = []
for paramm in sorted(param_list):
future = executor.submit(single_function, paramm)
future_list.append(future)
results = []
for future in futures.as_completed(future_list):
res = future.result()
한편 파이썬은 … asyncio
✓ Asyncio로 I/O를 효율적으로 처라하자

import asyncio
import aiohttp
async def slow_api_call(client, time=3):
url = "https://httpbin.org/delay/{time}"
async with client get(url) as resp:
result await resp.text()

    return result

async def runner (params):
async with aiohttp.ClientSession() as session:
tasks = [slow_api_call(session, t) for t in params]
resp = ""

        for future in asyncio.as_completed (tasks):
            data = await future
            resp += data
    return resp

마지막으로 오늘 못 다룬 것들
✓ Reactive (Flow API)
✓인터페이스에 구현을 포함
√ 모듈화
√ try-with resources(AutoCloseable)
✓ Optional
✓ http client
√ 타입 추론(var)
향상된 switch 문
√ 컬렉션 API 개선
√ 새로운 GC 알고리즘
√ 날짜와 시간 API 개선
√ Fork-Join 프레임워크
✓ Spliterator
√ 성능 개선
√ 각종 데코레이터
√ match-case (Structural Pattern Matching)
√ 상세한 에러 메시지
√ 안쓰는 기능들 정리(deprecated)
✓ Context Manager
√ 예외 처리 강화
√타입 안정성 강화(타입 힌트)
✓제너레이터
✓ etc...

마지막으로…3
✓ Java Support Tools
✓ visualVM, jconsole
✓jps/jstack/jstat/jhat/jmap
✓ jshell
✓ flight recorder, jmx, Spring Actuator
✓ Python Tools
✓ profile(cProfile), memory_profiler, vProf
snakeviz

#2

모던자바와 파이썬
함수형과 스트림
고수준 병렬/동시성 지원
파이썬
모던 자바
함수형 프로그래밍 도입으로 큰 변화가 있었던 Java 8 이후
모던 자바의 특징
함수형 패러다임 도입
쉬운 동시성(병렬처리) 도입
모듈형 강화
개발자 편의 API 추가
함수형
함수를 일급시민에 포함
익명 클래스의 번거로움을 람다로 간편하게, 메서드 참조로 재사용
코드 블록을 주입(동작 파라미터화)하고 조합할 수 있게 됨
스트림의 기반, 병렬처리와 조화
주요 패키지, 클래스
@FunctionalInterface
java.util.function
Consumer, Supplier, Function, Predicate
Operator
기본형 Int, Long, Double
함수형 - 람다
람다 = 익명함수, 익명 클래스를 대체
함수형 인터페이스(이름 있는 람다) : 하나의 추상 메서드를 가진 인터페이스
메서드 참조 : 메서드나 생성자를 참조하기(::slightly_smiling_face:
스트림
컬렉션 + 함수형, 데이터 처리 연산을 지원하도록 소스에서 추출된 연속된 요소
외부 순환(for, while, ..) VS 내부 순환(VM아 이거 해줘~)
SQL 처럼 선언형 스타일로 데이터를 처리
쉽게 병렬처리 적용 : parallelStream 메서드
주요 패키지, 클래스, 메서드
java.util.stream
BaseStream, Stream
map(), filter(), reduce(), min(), ...
C.stream(), C.parallelStream()
스트림 - 주요 개념
중간 연산과 최종 연산
중간 연산은 스트림을 반환, 여러 연산을 조합할 수 있음
최종 연산을 스트림을 모두 소비하고 닫음
스트림은 1회용(최종 연산 이후 사용불가)
Collection - Stream - filter - map collect - Collection

Stream : collect 끝날 때 close
filter : Predicate
map : Function
collect : collector/Consumer

```

파이썬
원래부터 함수형으로 시작(v1.0, 1994)
내장 컬렉션 = 리스트, 딕셔너리, 튜플, 세트, ..
lambda, itertools, functools, generator
병렬/동시성
병렬은 좋으나 사용이 어려움
저수준 병렬 처리의 어려움 : Thread, Lock, synchronized, ...
안전하고 쉬운 병렬처리 방법 제공
많이 사용되는 패턴들을 언어 차원에서 API로 지원
고수준, 추상화, Thread Safety, 비동기 지원
주요 패키지, 클래스
java.util.concurrent
Executor(s), ExecutorService
xxThreadPool, ForkJoinPool
Future, CompletableFuture
Runnable, Callable
Executor / Service / Etc
Thread를 직접 생성, 관리하지 않고 ExecutorService에서 스레드 관리
작업(Runnable, Callable)을 Executor 서비스에 요청하고 결과 받기
작업 스케줄링(cron, at)기능 : ScheduledExecutorService\
Concurrent Collection : Thread Safe List / Map 제공
Atomic Variable : 변수 자체가 원자성을 보장
Lock 객체 : 동기화 패턴에 따라 사용할 수 있는 유틸리티
비동기 지원
동기 vs 비동기 & 블록(block) vs non-block
작업이 끝날 때까지 기다리기 vs 하고서 나중에 물어보기
Future : 비동기 연산 지원, 완료 확인/대기/결과 조회/취소
CompletableFuture : Future 작업 연결, 순서 정의 등
파이썬
파이썬은 느리다 : 일부만 맞는 얘기
GIL 문제 : 스레드 활용을 제한하는 요소
multiprocessing
asyncio, coroutine
future, executors, ThreadPoolExecutor
ETC
Java
Reactive(Flow API)
모듈화
Optional
타입 추론(var)
컬렉션 API 개선
날짜와 시간 API 개선
Fork-Join 프레임워크
Spliterator
인터페이스에 구현을 포함
try-with resources(AutoCloseable)
http client
향상된 switch 문
새로운 GC 알고리즘
etc...
Python
성능 개선
match-case(Structural Pattern Matching)
Context Manager
예외 처리 강화
타입 안정성 강화(타입 힌트)
제너레이터
각종 데코레이터
상세한 에러 메시지
안 쓰는 기능들 정리(deprecated)
etc...
안쓰는 기능
Java Support Tools
jps / jstack / jhat / jmap
jshell
flight recoder, jmx, Spring Actuator
Python Tools
profile(cProfile), memory_profiler, vProf
snakeviz
```

#3

모던 Java with Python
모던 Java
모던 자바의 특징
✔ 함수형 패러다임 도입 ✔ 쉬운 동시성(병렬처리) 도입 ✔ 모듈성 강화 ✔ 개발자 편의 API 추가
ex
✔ 반복문 / 조건문 없이 문자열 리스트에서 길이가 5~10인 것만 대문자로 출력하기
list.stream()(filter(s -> s.length() >= 5 &&& s.length() <= 10))<br/> .map(s -> s.toUpperCase()).forEach(System.out::println);
[s.upper() for s in str_lst if len(s) in range(5, 11)]
함수형
✔ 함수를 일급 시민(First Class Citizen)에 포함

자바는 객체 지향 기반이 탄탄해서 완전한 함수형 패러다임은 x
✔ 익명 클래스의 번거로움을 람다로 간편하게, 메서드 참조로 재사용 ✔ 코드 블럭을 주입(동작 파라미터화)하고 조합(Pipeline)할 수 있게 됨 ✔ 스트림의 기반, 병렬처리와 조화 ✔ 주요 패키지, 클래스

@FunctionalInterface
java.util.function
Operator
Consumer, Suuplier, Function, Predicate
람다, 메서드 참조
✔ 람다(lambda) = 익명함수 ✔ 함수형 인터페이스(이름있는 람다): 하나의 추상 메서드를 가진 인터페이스 ✔ 메서드 참조: 메서드나 생성자를 참조하기(::slightly_smiling_face:
예시 (문자열 리스트를 길이에 따라 정렬)
Collections.sort(words, (o1, o2) -> Integer.compare(o1.length(), o2.length()));
Collections.sort(words, Comparator.comparingInt(String::length));
// java 9 버전 이후<br/>words.sort(Comparator.comparingIng(String::length));
스트림
✔ 컬렉션 + 함수형, 데이터 처리 연산을 지원하도록 소스에서 추출된 연속된 요소

외부순환 vs 내부순환
SQL처럼 선언형 스타일로 데이터 처리
쉽게 병렬처리 적용: parallelStream
✔ 주요 패키지, 클래스, 메서드

java.util.stream
map(), filter(), reduce(), min()
C.stream(), C.parallelStream()
BaseStream, Stream
주요 개념
✔ 중간연산과 최종연산

중간 연산(filter, map)은 스트림을 반환, 여러 연산을 조합할 수 있다
최종 연산(collect)은 스트림을 모두 소비하고 닫음
스트림은 1회용(최종 연산 이후 사용 불가)

스코프를 최대한 짧게 쓰고 끝!
✔ 스트림 중간에 collection 가급적이면 내부 값 변경하지 않기
예제
✔ 직원 리스트 -> 부서별 직원 리스트
Map<Department, List<Employee>> byDept = employees.stream()<br/> .collect(Collectors.groupingBy(Employee::getDepartment));
✔ 직원 리스트 -> 부서별 급여 합계
Map<Department, Integer> totalByDept = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment, Collectors.summingInt(Employee::getSalary)));
✔ 좋은 직원, 안 좋은 직원 나누기
Map<Boolean, List<Employee>> byGood = employees.stream().collect(Collectors.partitioningBy(Employee::isGood));

파이썬
✔ 파이썬은 1버전부터 함수형 ✔ 내장 컬렉션 = 리스트, 맵(딕셔너리), 튜플, 세트 ✔ lambda, itertools, functools, generator ✔ List comprehension
병렬/동시성 (concurrent)
✔ 저수준 병렬 처리의 어려움: Thread, Lock, synchronized... ✔ 안전하고 쉬운 병럴처리 방법 제공 (만능은 아니다!)

많이 사용되는 패턴들을 언어 차원에서 API로 지원
고수준, 추상화, Thread Safedty, 비동기 지원
✔ 주요 패키지, 클래스

java.util.concurrent
Executor(s), ExecutorService
xxThreadPool, ForkJoinPool
Runnable, Callable
Executor / Service / Etc
✔ Thread를 직접 생성, 관리하지 않고, ExecutorService에서 스레드 관리 ✔ 작업(Runnable, Callable)을 Executor 서비스에 요청하고 결과 받기 ✔ 작업 스케줄링 기능 ✔ Concurrent Collection

Thread safe list/map 제공
✔ Atomic Variable ✔ lock 객체

동기화 패턴에 따라 사용할 수 있는 유틸리티
비동기 지원 (Async)
✔ 동기 vs 비동기 / 블록(block) vs 논블록(non-block) ✔ Future: 비동기 연산 지원, 완료 확인/대기/결과조회/취소 ✔ CompletableFuture: Future 작업 연결, 순서 정의 등
ex(Spring)
✔ 하나에 3초 걸리는 API 5개 호출 ✔ 병럴, 비동기 x
api1.callApi(param)<br/>api2.callApi(param)<br/>api3.callApi(param)<br/>api4.callApi(param)<br/>api5.callApi(param)
✔ 병렬, 비동기 o
for (ApiService api : apis) {<br/> apiResults.add(api.callApi(param));<br/>}<br/>for (CompletableFuture<Void> future : apiResult) {<br/> future.get();<br/>}
@Async<br/>public CompletableFuture<Void> callApi(String param) {<br/> // api를 호출<br/> return new CompletableFuture<>();<br/>}
Multiprocessing in Python
✔ GIL (Global Interpreter Lock): thread 활용을 제한하는 요소

점점 개선중
✔ multiprocessing

프로세스를 통한 병렬처리 ✔ asyncio, coroutine
✔ future, executors, ThreadPoolExecutor
with futures.ThreadPoolExecutor(max_workers=4) as executor:<br/> future_list = []<br/> for paramm in sorted(param_list):<br/> future = executor.submit(single_function, paramm)<br/> future_list.append(future)<br/> results = []<br/>for future in futures.as_completed(future_list):<br/> res = future.result()
asyncio
import asyncio<br/>import aiohttp
async def slow_api_call(client, time=3):<br/> url = "https://httpbin.org/delay/{time}" <br/> async with client get(url) as resp:<br/> result await resp.text()<br/> return result
async def runner (params):<br/> async with aiohttp.ClientSession() as session:<br/> tasks = [slow_api_call(session, t) for t in params]<br/> resp = ""<br/> for future in asyncio.as_completed (tasks):<br/> data = await future<br/> resp += data<br/> return resp

#4

모던 자바
함수형 프로그래밍 도입 이후 큰 변화가 있던 java8 이후

특징
함수형 패러다임 도입
쉬운 동시성 도입
모듈성 강화
개발자 편의 API 추가

함수형
함수를 일급 시민에 포함
자바는 객체 지향이라 순수 함수형은 아니고 객체 지향으로 함수를 쓸 수 있게 한 것
익명 클래스 -> 람다 -> 재사용

스트림
컬렉션 + 함수형, 데이터 처리 연산을 지원하도록 소스에서 추출된 연속된 요소
중간 연산은 스트림을 반환, 연산 조합 가능
최종 연산 스트림을 모두 소비하고 닫음

병렬/동시성
저수준 병렬 처리의 어려움(Thread, Lock, sysnchronized)
-> 많이 사용되는 패턴을 API로 지원
ExecutorService에서 스레드 관리

비동기 지원
Future: 비동기 연산 지원, 완료 확인/대기/결과 조회/취소
CompletabelFuture: Future 작업 연결
