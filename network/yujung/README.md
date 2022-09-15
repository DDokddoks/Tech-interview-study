# Computer Network

### ⚡️ Chapter 1-1, 1-2

- 프로토콜이란?

네트워크에서 data를 주고받기 위한 통신 규약! 프로토콜이 존재하지 않는다면 회사 or 개인마다 data 형식이 달라지기 때문에 제대로 전달하기가 힘들기 때문에 프로토콜은 네트워크에서 꼭 필요한 존재이다.

- 패킷이란?

Data를 일정한 chunck로 나눈 것을 의미한다.

- 네트워크, 인터넷, 프로토콜의 개념을 설명해주세요

네트워크는 data를 전송하기 위한 하나의 망이라고 생각하면 된다. 인터넷은 네트워크의 네트워크이며, 프로토콜은 네트워크내에서 data를 주고받기 위한 통신 규약이다.

- 네트워크란 무엇인가? 네트워크 종류는? 인터넷이란?

네트워크는 data를 전송하기 위한 하나의 망이라고 생각하면 되고, 네트워크의 종류에는 LAN, WAN등이 존재한다. 인터넷은 network’s network이다.

- ISP란?

ISP는 internet service provider의 약자이다. 기존에는 다른 user에게 data를 전송하려면 user가 access network에 연결되는 망이 일일이 존재해야 했지만, 회사에서 제공하는 ISP가 존재한다면 user가 ISP에 존재하는 하나의 router에만 연결이 되면 다른 end system으로 전송이 가능하다는 장점이 존재한다. 

- DSL이란?

Digital subscriber line으로 전화회사에서 제공해주는 network를 의미하며 DSL modem이 존재하고 dedicated하기 때문에 다른 사용자와 공유하지 않는다. 실제로 downloading할 일이 uploading할 일보다 많기 때문에 DSL에서 제공하는 bandwidth는 upstream이 1Mbps이고, downloading은 10Mbps정도이다. 

- Ethernet에 대해 설명하세요.

네트워크 기술이다.(잘 모르겠음)

- LAN에 대해 설명하세요.

LAN은 local area network로 좁은 범위내에서 네트워크가 연결된 것을 의미한다. 반대로, WAN이라는 wide area network가 존재하기도 한다.

### ⚡️ Chapter 2-4, 2-5

- 도메인과 DNS가 무엇인지 설명해주세요.

ip는 사람이 이해하기 어렵기 때문에 각각의 ip에 이름을 부여할 수 있게 했는데 이것을 도메인이라고 한다. 예를 들어 114.108.157.19처럼 되어있는 실제 ip주소를 daum.net으로 하는 것과 같은 것이다. DNS는 Domain Name System의 약자로 도메인 이름을 IP주소로 변환하거나 반대의 경우를 수행할 수 있도록 개발된 데이터베이스 시스템이다. 그 시스템 안에서 이어주는 역할을 하는 서버가 DNS Server인 것이다. 

- Domain Name 구조를 설명해주세요.

Hierarchy구조를 가지고 있는데 제일 상위에 root Domain이 존재하고, 그 아래에 Domain Namekr처럼 국가를 나타내는 국가코드 도메인과 com처럼 사용되는 일반도메인이 존재하는 TLD가 있다. 그 아래에는 authoratitive domain이 있고 가장 하위에 host가 존재하게 된다. 각 네임 서버가 계층의 일부 영역을 담당하게 되고 해당 영역에 속한 domain을 관리하게 된다. 최상위 계층인 root name server는 모든 DNS Server가 등록해서 관리하고 있다.

- Domain Name System 동작과정을 설명해주세요.

User가 www.google.com을 입력하면 host는 DNS Server에게 IP주소를 request하게 된다. DNS Server가 IP 주소를 알고있는 root name server에 다시 IP 주소를 물어보게 되면, com 정보를 등록하고 있는 root name server가 해당 IP주소는 com 네임 서버에 문의하라고 com 네임서버의 IP주소를 알려주게 되고, 다시 DNS Server가 com 네임서버에게 IP주소를 질의해서 google.com의 네임서버의 IP주소를 얻게 된다. 해당 과정을 반복하다보면 DNS Server가 알고자하는 IP주소를 알고 있는 name 주소에 도달해서 IP주소를 얻을 수 있게 된다. 하지만 이 과정은 굉장히 복잡하고 root에 overhead가 많이 발생할 수 있기 때문에 DNS Server가 일부를 Caching하여 root name server까지 가지 않고도 바로 IP주소를 알려줄 수 있게 한다.

- 도메인 이름으로 실제 IP를 어떻게 찾을 수 있는지 흐름을 설명해 주세요.

처리 순서는, 만약 브라우저 창에 naver.com을 입력하면, DNS에서 매칭되는 IP주소인 125.209.222.142를 찾게 되고, 해당하는 웹 서버로 요청을 전달하여 client와 server가 통신할 수 있도록 하는 방식으로 동작한다.  
