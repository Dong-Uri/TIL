(정리 도움받음)

#1

스마트홈 20230125
스마트 홈 IOT 서비스 이용 과정
제품구매 - 구매한 제품 설치 - 환경설정(앱 설치) - IOT 디바이스/서비스 간 연동

매터(matter)란?
2019년 Zigbee Alliance에 의해 project CHIP 시작

2021년 Zigbee Alliance는 CSA로 Project CHIP는 Matter로 명칭 변경

여러 플랫폼에서 공통으로 활용할 수 있는 통합 프로토콜

매터의 특징
단순성 - 구매 및 사용이 간편
상호 운용성 - 여러 브랜드 장치가 함께 작동
신뢰서 - 일관되고 반응이 빠른 로컬 연결
보안 - 강력하지만 간소화
메터 구조
스레드(Thread) 프로토콜
IEEE 802.15.4

저전력

Mesh Network - 그물망처럼 촘촘히 연결된 부분이 각각의 환경에서 동작할 수 있도록 해준다

IPv6 기반

메터의 구성
클라우드가 인터넷을 통해 연결되고 메터가 있는 디바이스들이 스레드라는 기술을 만나게 되면 mesh 네트워크가 서로 연결이 되어 각각의 네트워크를 구성하게 된다. 보더 라우터는 네트워크가 끊기게 되면 다른 네트워크를 찾게 된다. 또 다른 네트워크를 자동으로 찾아 IoT장치를 사용할 수 있게 된다. 다양한 장치로 연결이 가능하고 IP, 메터를 지원하지 않는 장치도 메터지원하는 허브로 모든 디바이스 연동이 가능한 구조를 가지게 된다.

매터에 대한 전망
2023년부터 2030년 사이에 55억개의 매터 지원 스마트홈 제품 출시 전망

향후 5년 내에 스마트홈 디바이스 제조사의 절반 이상 메터 지원 예정

메터 최신 동향
메터 Spec 1.0이 2022년 10월 발표되어 10여종의 디바이스 유형 지원

삼성전자의 smart things hub가 최초로 메터 인증 획득

최신 매터 지원 기기
삼성전자 Smart Things station 2023년 CES에서 공개

140억개의 커넥티드 기기들을 연결하기 위한 기술 비전

메터 참고 사이트
오픈 소스 : https://github.com/project-chip/connectedhomeip

CSA의 매터 정보: https://csa-iot.org/all-solutions/matter

#2

# 스마트 홈 IoT 연동 표준 매터(Matter)

- 매터(Matter)란?
- 매터의 특징
- 매터의 구조
- 매터에 대한 전망

## Keyword

- Matter
- THREAD
- CSA

# 스마트 홈 IoT 서비스 이용 과정

- 제품구매
- 구매한 제품 설치
- 환경설정(앱 설치)
- IoT 디바이스 / 서비스간 연동

# 매터(Matter)란?

![매터로고](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAX4AAACECAMAAACgerAFAAAAkFBMVEX///8jHyAAAAAZFBUeGhsPBwlnZWUMAAX8/PzX19c9OjshHB6ZmJilpKTx8fHPz8/l5OQ3NDVRTk8YExS8u7sIAACQj5AuKivr6+uura3My8u0s7MdGBr39/dHREXq6uqJh4h5d3jCwcFvbW6XlpaEg4NcWVpgXl8wLS5YVlZzcXHf3t6hoKAoJCVNS0w4NTWp0KFfAAAKcUlEQVR4nO2ca3uqvBKGZSCg4gEb4xEUtVat1fX//91OwhmCxSL1dXfua31YAsbwZJhMJkNbLQRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBXp/ZYTd4dh/+LO0JUAq9Z3fjj+JZROMw/dkd+ZsMQJPAszvyN0H5nwrK/1RQ/qeC8j8VlP+poPxP5YXl73fUxxfL3+1HHV5W/uEKlPI7JvR/uy8/51Xl98FVyj8GaqH8jWNSTSl/n2kof/OYeon8Fsr/C6D8T+Wl5d960f+K8s8WT+nSnbyw/OcTHIfh/wvyL2wwnSd17A5eVn5vA7pmwCZ4AHLyz0wwNAp++4kdrMSryv8FcntLI+CvWzn5zxugwUn6X185vqb8HR1sLYTA29zxYvnP/VUoPseG4w89kNPfjRiQ1X6bOzGYf44ASHez/GZjf9jbjSgY1/04mqG8xXCYaM0/DDsnV7PmwwIdn2rU74SfFl6xdWfpb8zd5n37TS9m802XgvtYN9A2QUtwGfdDIRQsN3UK/B+1v72CRQ0+fC4F8p7qu/MJTJ4wKAOzJFvDmfkuEGrYsgXYBRd2AOAjvgUQiL5aUITKW4nIm9B6MgVGqE4pAbjOy7UdfvDuurZxfLQXniTmX47xs7zJ7AOCIZQ/YTMtmuC5y6PJCa7PRn1bbR+InblQ1sB0QNPN+BoodLeMnPyDDRBDNi5bd8EouUtvF5qlMX34JDi26I0eS4hdbp43GJLQ9ogLwHQxivPgzA6CExZ/3sQJjYxmigY6FzEv6dyqKYXwQn1RkJ9whIyUFBHf0aMPWfnHhAS9AF12RbjYrsrFno3wQuY+3Pq5ERzAuCW+G0VFd7IQzXLD3s7abc9ZnsSTEOhvMmnI47UnThyEaem0qP8yaODU73i8hfPSFFGCAcus/K1Jr9f7WvEAbd8rwqdk3Yw+TNL+fS8ee8J7cRatd/pv4oF0YVzoxpkZcXcbiQC30/IBcKE7/L4FBY64Pdgkd3xecdVFePLObR/MRG7njR/Qj/kG5iDs8TNljwNfDuHWycgv2fHI56zoxbws8hEPIIVeyrCcHVfBhnyMN9DdbHcbYDkFqpgDbArdfMRSlS636Zwt7YF7z9YZoqcgZsIPkU32+1sxJm5u6J0uEa2ygvz3Bp570YmPXLQz1KgY3ezBD3Gs8dh1sSN8IkoNge0S0Dc/cvoCYbv5O2ntmca+eIyYUz98IDK/NWO2RrtFr8cdl+hkTfmXoAzmvCvhEcI6fWhbNJZm8Lb+SufzC7MsxoAH2pNFDVenGZo1KRxduRrl/zaFEyddoxlFudHpXdXvH+QysZ78Ymyh2DvOla8TTvkef6qurIlymeE522W/358vF45yuq1c+rwAbqRF9Toi5LFZsRlHGFnKv4rvE6W/bR+N2vLvaG6wYzzbyLhM0WH4UeTxDcfT8s5mB/3V6furAvZUI6oy6Tc+j9G94sSB65ea9bjRFSbBEDmEteTnY20bJTfPx934l3x8J+ru1oYvocnmjkzCeccYOVS9mpuoMhLhcmigCqWWLO2T+PTsrsraNmlN+ffkhjsXLSU59g9d3d3adA0R2HxWdCeOKcJivbL8wveo7Kv0YRaCv8WfJiQfNeXaqCU/se1LWeOi9ZQd8NuARoL9rgz1KXxVuXgSJAkqyz/jj7DSekVGVbmT5mUe+q5h6+WucWTUkp8LTJTzbvzbVvxBmFH5pTXohistWH27ojgfWXBtZfmdjC2nGPC40VV+hd9onFHxeGD/obxK4pNa8vNjcGMLz6dJcqjNjWJUfmkNIvk1nX2zslpClPt8gPyWZtvKr6Tl556IvJe3Pi6ueu+Rn4cF9qU8yXJJLVh+QX6+0L65qEvlRB8jv6H8Slr+IWjsxlJnWE9+HmRxGyiF32f8483Jf0wlOm+9SrdPJXRJ1cCzpvx8qVk+8+YyngH3yM+DWs24SaxHc/KPu6k8W/kEnFLfhbeqVQ815efBN7uxvVlTfrH26N7k2Lz1cxsbsUT/EmP7itW3YVU9AVRTfhGb3IjItvXk52teUjGYbFL+VquXPADKRZIww8jtk3t222vKz+NWurvR7XqRj1hUKO+2SLPytzrTaAYwLgqDGJBo1iWrdfF0OTXl56sdY1re+smtJT8PnKpWPzQsv0yxhgIX05CtQzQ4TJ2gKqWu/Bt6Y60/qLnqHdzKaGRpWv5W+xoVNxTvdxy5HnLDEyipK//2lvd5JzWTDnzurZjIaVz+VjuSv2AR7Wk4M9zfg7ryt7jXU7+tItMTNeVfVjb/xuUfduNynnz000/m3VPFqSqitvw84nK76rZFwrNmvp/bVbW/GtKw/GszFfwb2ftta8nWo35ntUNt+VsXQzkbRaFwPfnHqp3QgLmZzgE3Kn97Apkan2wiapmpXyLsnu3m+vKLkBcUGx1iD1kvyv9J1Wm0OVNmN01SstQZA4X3xNKalH9pWFqG7Gz35mZO2jCqXvRQX/6WL8tR8tGwPOrTgvx8KaDYQS5sXkV4U1E9UhwXseVvpKqxmpO/syqWF7J02UuheM+AQ9Up4AHyy2IscsmY6FCWCu0VdT5yG0exMPQsW7MUD5EjqnfYv6xBDVdS/ZQTa0r+2SekjdsuTr59K3MqeDxgX20KeIT8LVOK0e2HxrheXmWV1U7ko/PyyzwamMuxJHXc5wPGrvPgeNq6LlS0Puqdwx915rJ5NxOSNiT/e8bpU/IvLGFNPb8fQUBqd5OqZzEF6JVqXh4if2si4gLXgsvVNE9TYLIMc69MuQVFdZQF5c6p4+2pLtsoVDh7J/ENg4DRPezM60U2r7FRZvu7EfnHNkvZtAs7bx4k34xUpV9U6L9Yn9IliHwKqJD2fIz8reFF/rTt6roremwTIixbJT/38nH+JFOvuNaidX2+wnnOpAy2odOweZovvWpA/vM17fSDRGbk6CGOujrBEZvyB3Z7hMxwHb7N/zhAoGSvlxBLdaIFxLKLaaf5NK694+KQSTvoG4Hixs/6A5gsZLayu7PtDYCqwpmf+dKSyj6DAtvk911F+fSN5NMP2GecvqUF89XRCG09uixMOLhX+emLkNSXvv9LhwN/MlFmjD1+Qr3NzU+8q9LAQ7+rS89xMcfh+TW/VuUDnfn7RJDfpxyMe/K4XyzrGE5WhmydjD7HxXmtvff9G7vy99O+GGkdJ+EdmYGDTzY5JuErX354B5v0FFA1Y/UgPKczPDdWYuytnU7H+aU/Xdo+xvK7YMZeJFI7HupN4EmTLddzagoInwnkbmL57UzhfhhmJgV14eOQXppvpwzlr0lbC+QnVsZ7LgNlk8jzFMqfScz2wuhC/13n8/9EX7yio+fflC7K7yrkbw3kao3oN8oQkNt4PBA75Gtr53n5D3ouFArpXCGer5Ef0Snmzr6ygU4y9RbzKOMX+BMPr4YfLKyS8g5fjscPX+hF7mUpX15NAh0ZCrEpOvlfQu69JPUvC6iwuEUeyPoASen9ACq/eoE8iEVqu+v043dKEQRBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBEARBnsn/AOe4n45qAD0sAAAAAElFTkSuQmCC)

## 매터의 역사

- 2019년 Zigbee Alliance에 의해 Project CHIP 시작
- 2021년 Zigbee Alliance는 CSA로, Project CHIP는 Matter로 명칭 변경

## 매터

- 여러 플랫폼에서 공통으로 활용할 수 있는 통합 프로토콜
- 하나의 디바이스로 여러 플랫폼에 연결하여 이용 가능

## 매터의 특징

- IPv6기반 홈IoT 통신 표준
- 이더넷, 와이파이, 스레드 등 지원

1. 단순성 : 구매 및 사용이 간편
2. 상호 운용성 : 여러 브랜드 장치가 함께 작동
3. 신뢰성 : 일관되고 반응이 빠른 로컬 연결
4. 보안 : 강력하지만 간소화

## 매터의 구조

- Ecosystems and Cloud
- Application Layer - `Matter`
- Network/Transport Layer
- Radio:Physical/Link Layer(MAC/PHY)

## 스레드(Thread) 프로토콜

- IEEE 802.15.4
- 저전력
- `Mesh Network`
- IPv6기반

## 매터에 대한 전망

- 2023년부터 2030년 사이에 55억 개의 매터 지원 스마트홈 제품 출시 전망
- 향우 5년 내에 스마트홈 디바이스 제조사의 절반 이상 매터 지원 예정

## 매터 최신 동향

- 매터 Spec.1.0이 2022년 10월 발표되어 10여 종의 디바이스 유형 지원
- 삼성전자의 SmartThings Hub가 최초로 매터 인증 획득
  - 삼성전자 '스마트싱스 스테이션' 2023년 CES에서 공개, 중요하게 생각하고 있음
- Devices supported by Matter at launch
  - Lighting and Electrical
  - HVAC Controls
  - Access Control Products
  - Safety and security Sensors
  - Window Coverings and shades
  - TVs
  - Access Pointer

## 매터 참고 사이트

- [오픈소스](https://github.com/project-chip/connectedhomeip)
- [CSA의 매터 정보](https://csa-iot.org/all-solutions/matter)
