(정리 도움받음)

#1

A* 알고리즘

    다익스트라보다 발전된 길찾기 알고리즘!
    대부분의 인공지능 길찾기 알고리즘에서 사용 중이다.

노드의 4가지 State

    Close : 가본 곳
    Open : 발견된 곳 (Close와 인접한 곳)
    Empty : 발견되지 않음 (못 가봄)
    Block : 못 가는 곳

이하 3개 과정을 반복한다!

    도착한 노드는 Close
    주변 노드 4가지 상태에 따라
        Empty는 Open으로
        Block과 Close는 유지
        Open은 (도착 노드에서 계산한) G가 더 작으면 부모 노드를 바꾸고, 더 크면 유지
    최소 F값인 노드로 이동
        G = 출발지로부터의 거리
        H = 도착지까지의 거리
        F = G + H
    이상의 과정을 도착한 노드가 목표 노드가 될 때까지 반복하면 끝
        Open 노드가 하나도 남지 않으면 길이 막혀있다(or 실패했다)는 의미

실제 코드로 만들려면?

    각 노드가 4가지 상태와 부모 노드, G 값을 들고 있어야 함
    새로 열린 Open 노드들을 계속 Push, Pop 해 줄 우선순위 큐가 필요함
        우선순위 기준은 F 값이 가장 작은 것부터 Pop!
        주로 힙을 사용해서 구현
    다양한 문제에 적용하려면 H값을 어떻게 계산 하느냐가 가장 큰 관건!

못 쓰는 경우도 있을까?

    목적지가 어디인지를 모르거나, 목적지까지 남은 거리를 구할 수 없다면 사용 불가
        H값을 알 수 있는 경우에만 사용 가능
    but 그런 경우는 꽤 드물다고 한다!

#2

A-star Algorithm
4-State node

    Block 은 변하지 않음 : 한번 block 은 영원한 block
    나머지 노드는 Empty → Open → Close 순서로 변경됨

Steps
Step1(S1): 도착한 Node 는 Close
Step2(S2): 주변 Node 4가지 상태에 따라

    Leave 는 아무것도 하지 않는다는 의미
    Empty → OPEN
    BLOCK → Leave
    CLOSE → Leave
    OPEN → G가 작다 → 부모 Node 바꿈
    OPEN → G가 크다 → Leave

Step3(S3): 최소 F값 Node 로 이동

    G : 출발지로부터의 거리
    H : 도착지까지의 거리
    F = G + H
    최소 F값 Node 로 이동

실패 경우

    사방이 벽으로 막혀있는 경우 길울 찾을 수 없음
    Open Node 와 Empty 로만 이뤄지게 되는 경우 실패로 간주

Source Code

https://github.com/sweetchild222/vanilla-algorithm
from classes.node import Node
from classes.openList import OpenList
from classes.point import Point
from classes.map import Map
import classes.drawer as drawer

def aStar(start, stop, nodeMap):

    openList = OpenList()

    node = map.getNode(start)

    while True:

        node.setClose()

        drawer.draw(map, start, stop)

        if node.getPoint() == stop:
            return node

        childList = lookAround(node, nodeMap)

        openList.append(childList)

        node = openList.minCostFNode()

        if node is None:
            return None

def neighborBlock(node, deltaPoint, map):

    x = deltaPoint.x
    y = deltaPoint.y

    neighborList = []

    if (abs(x) + abs(y)) == 2:
        neighborList = [Point(x, 0), Point(0, y)]

    for point in neighborList:

        neighborPoint = node.getPoint() + point
        neighbor = map.getNode(node.getPoint() + point)

        if neighbor is None:
            continue

        if neighbor.isBlock() is True:
            return True

    return False

def lookAround(node, map):

    childDelta = [Point(1, 0), Point(1, -1), Point(0, -1), Point(-1, -1),
                 Point(-1, 0), Point(-1, 1), Point(0, 1), Point(1, 1)]

    openList = []

    for delta in childDelta:

        childPoint = node.getPoint() + delta
        childNode = map.getNode(childPoint)

        if childNode is None:
            continue

        if neighborBlock(node, delta, map) is True:
            continue

        if childNode.isBlock():
            continue
        elif childNode.isClose():
            continue
        elif childNode.isEmpty():
            childNode.setParent(node)
            childNode.setOpen()
            openList.append(childNode)
        elif childNode.isOpen():
            currentCostG = childNode.costG()
            newCostG = childNode.calcCostG(node)
            if currentCostG > newCostG:
                childNode.setParent(node)
        else:
            print('error!')

    return openList

"""
data = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]
"""

"""
data = [
    0, -1, -1, -1, 0, 0, 0, 0,
    -1, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, -1, 0, 0, -1, 0, 0, 0,
    0, 0, 0, -1, 0, 0, 0, 0]
"""

data = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]

width = 8
height = 6

start = Point(2, 3)
stop = Point(6, 3)

map = Map(data, width, height, stop)
node = aStar(start, stop, map)

while node:
    print(node.getPoint())
    node = node.getParent()

#3

A_star 알고리즘 이란?

    최단 경로 찾기
    네비게이션, 게임, 자율 주행 등 많은 분야에서 활용한다.
    경로 찾기에서 다잌스트라 보다 더 최적화 된 알고리즘이다.
    맨해튼 거리로 출발지,Node 와 도착지 사이의 거리 값을 계산한다.

맨해튼 거리(Manhattan distance)

    두 점 사이의 거리를 대각선 거리가 아닌 세로, 가로 값의 합으로 계산한다.
    ex) 시작점 : (x1, y1) , 도착점 : (x2, y2)
    맨해튼 거리 d = | x1 - x2 | + | y1 - y2 | 

4-State node

    close : 이미 가본 node, 확인 한 곳open : 발견된 node, 앞으로 가봐야 할 후보지Empty : 미 발견된 node, 영역Block : 갈 수 없는 곳. ex) 벽

알고리즘 진행 과정

    도착한 Node는 Close 한다.주변 노드는 다음과 같은 조건으로 State를 변화한다.
        Empty : Open으로 바꾼다.BLOCK, Close 는 그대로Open : G가 더 작으면 부모노드를 바꾸고 그렇지 않으면 그대로 둔다.최소 F 값으로 이동
        F = G(출발지로 부터의 거리) + H(도착지까지의 거리)
    도착 경로까지 1~3 반복A_star 도착 노드에서 부모경로를 따라 가면 완성된 최단 경로를 알 수 있다.

A_star 알고리즘 코드를 알고 싶다면?

→ https://github.com/sweetchild222/vanilla-algorithm

    시작, 종료 노드, 맵 생성

map= [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, -1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]

# -1 : BLOCK(벽)

start = Point(2, 3)
stop = Point(6, 3)

map = Map(data, width, height, stop)

    a* 알고리즘

def aStar(start, stop, nodeMap):

    openList = OpenList()

    node = map.getNode(start)

    while True:

        node.setClose()

        drawer.draw(map, start, stop)

        if node.getPoint() == stop:
            return node

        childList = lookAround(node, nodeMap)

        openList.append(childList)

        node = openList.minCostFNode()

        if node is None:
            return None

def neighborBlock(node, deltaPoint, map):

    x = deltaPoint.x
    y = deltaPoint.y

    neighborList = []

    if (abs(x) + abs(y)) == 2:
        neighborList = [Point(x, 0), Point(0, y)]

    for point in neighborList:

        neighborPoint = node.getPoint() + point
        neighbor = map.getNode(node.getPoint() + point)

        if neighbor is None:
            continue

        if neighbor.isBlock() is True:
            return True

    return False

def lookAround(node, map):

    childDelta = [Point(1, 0), Point(1, -1), Point(0, -1), Point(-1, -1),
                 Point(-1, 0), Point(-1, 1), Point(0, 1), Point(1, 1)]

    openList = []

    for delta in childDelta:

        childPoint = node.getPoint() + delta
        childNode = map.getNode(childPoint)

        if childNode is None:
            continue

        if neighborBlock(node, delta, map) is True:
            continue

        if childNode.isBlock():
            continue
        elif childNode.isClose():
            continue
        elif childNode.isEmpty():
            childNode.setParent(node)
            childNode.setOpen()
            openList.append(childNode)
        elif childNode.isOpen():
            currentCostG = childNode.costG()
            newCostG = childNode.calcCostG(node)
            if currentCostG > newCostG:
                childNode.setParent(node)
        else:
            print('error!')

    return openList

    완성된 경로 확인

while node:
    print(node.getPoint())
    node = node.getParent()

→ 도착Node부터 시작 Node까지 순서로 탐색해서 경로를 생성한다.
