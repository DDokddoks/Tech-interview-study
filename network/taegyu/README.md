# Computer Network

### ⚡️ Chapter 1-1, 1-2

- 프로토콜이란?
  > 인터넷 네트워크에서 메시지를 주고 받는 것을 제어하는 일련의 규칙을 말한다. TCP/IP, HTTP, Skype, 802.11 등이 있다.  
  > 프로토콜에선 메시지의 format, 메시지를 주고받는 order, 메시지를 받았을 때 취할 action 등을 정의한다.  

- 패킷이란?
  > Packet Switching 방식에서 사용자의 메시지를 일정한 크기로 쪼개서 link로 보내게 되는데, 이때 쪼개진 메시지의 단위를 packet이라고 한다. packet에는 그 packet이 가야 하는 목적지의 주소가 포함된다.
  
- 네트워크, 인터넷의 개념을 설명해주세요
  > 네트워크란, 두 대 이상의 컴퓨터들이 통신 기술을 통해 그물망처럼 연결되어 서로 통신할 수 있는 형태를 말한다.
  > 인터넷이란, 네트워크로 구성된 네트워크(network of networks)라고 불리는 세계 최대 규모의 네트워크이다. 
    
- ISP란?
  > Internet Service Provider의 약자로, 개인이나 단체에게 인터넷에 접속하는 수단을 제공하는 주체를 의미한다. 우리나라의 SKT, KT, LG U+ 등의 기업이 이에 해당한다.
     
- DSL이란?
  > Digital Subscriber Line의 약자로, 전화 회사에서 제공하는 Access Network를 의미한다.
      
- Ethernet에 대해 설명하세요.
  > ?
    
- LAN에 대해 설명하세요.
  > 집, 사무실, 학교 등 상대적으로 가까운 거리에 위치한 장치들을 서로 연결한 네트워크를 의미한다. 

- TCP/IP 프로토콜과 각 계층 설명하시오.
  > Applicaiton : network application에서 생성한 data를 포장해서 메시지로 만든다.  
  > Transport : source process에서 destination process로 메시지가 잘 전송되도록 한다.
  > Network : source host로부터 destination host로 전송이 잘 이루어지도록 한다.
  > Link : 한 hop 사이의 전송이 잘 이루어지게 하도록 한다.
  > Physical : 실제로 데이터를 실어나르는 역할을 한다.
  

### ⚡️ Chapter 2-1, 2-2, 2-3

- port란 무엇인가요? Well-Known Port에 대해 설명해주세요.
  > IP 내에서 각 프로세스를 구분하기 위해 사용하는 번호이다. Port number를 통해 host 내의 어느 프로세스로 접근할 지를 결정하고 접속할 수 있다.  
  > 대표적인 Well-known Port는 port80 - HTTP server, port25 - Mail server가 있다.

- 클라이언트와 서버의 통신 과정에 대해 설명해주세요.
  > 1. Client와 Server에서 Socket을 create 한다.
  > 2. Server 측에서 Socket에 IP와 port를 bind하고 Client의 연결을 대기한다.
  > 3. Client 측에서 접근하고자 하는 Server의 IP, port number로 connecttion을 한다.
  > 4. Server 측에서 Client의 connection을 accept 하여 서로 연결된다.
  > 5. 약속된 프로토콜에 맞게 데이터를 주고 받는다.
  > 6. 통신이 완료되면 양쪽 모두 socket을 close한다.
  

- HTTP method 4가지를 설명하시오.
  > 1. GET : URL을 통해 파일의 경로를 지정하고, Server에게 전달하여 리소스를 조회하는 용도이다.
  > 2. POST : HTTP request message의 entity body를 통해 데이터를 Server로 전달하여 추가하거나 등록하는 용도이다.
  > 3. PUT : URL에 등록하고자 하는 데이터와 경로를 지정하고, Server에 전달하여 추가하거나 기존에 존재하면 덮어쓰기 하는 용도이다.
  > 4. DELETE : URL을 통해 파일의 경로를 지정하고, Server에게 전달하여 해당 경로의 파일을 삭제하는 용도이다.

- HTTP의 GET 방식과 POST 방식을 비교해주세요.
  > GET 방식은 서버에서 리소스를 조회할 때 사용하고, POST 방식은 서버에 데이터를 추가, 등록할 때 사용한다.  
  > 웹페이지에 form input이 있을 때는 GET과 POST 모두 input을 서버에 업로드하는 용도로 사용하지만, GET 방식은 input이 URL 말단에 연결되어 전달되는 반면 POST 방식은 data가 request message의 body에 담겨 전달된다.

- HTTP 1.0, 1.1, 2.0 차이점은 무엇인가요?
  > HTTP 1.0 : GET,POST,HEAD만 지원한다.
  > HTTP 1.1 : GET,POST,HEAD + PUT,DELETE를 지원한다.
  > HTTP 2.0 : 

- HTTP의 특징에 대해 설명하시오.
  > - Client-Server 구조를 가진다.  
  > - Client/Server가 request/response message를 통해 통신한다.
  > - Stateless이다. 과거의 Client가 보낸 request history를 저장하고 있지 않는다.  
  > - Connectionless이다. Client는 Server로부터 response를 받고나면 연결을 유지하지 않고 끊어버린다.

- HTTP와 HTTPS의 차이에 대해 설명하세요.
  > 
  

- HTTP의 Status Code의 종류는 어떻게 되나요?
  > 200 OK
  > 300 Moved Permanently
  > 400 Bad Request
  > 404 Not Found
  > 505 HTTP Version Not Supported

- HTTP 헤더의 구조에 대해서 설명해 주세요.
  > header field name: value의 형태를 띈다. 예를 들어 Host: www.github.com, Connection: keep-alive 등으로 쓰인다.

- 주소창에 URL을 치고 엔터를 치면 흐름이 어떻게 되나요?
  > 1. Client(browser)가 URL에 해당하는 Server의 port 80을 통해 server process에 TCP connection을 연결하고, Server에서 Client의 연결을 accept한다.
  > 2. Client와 Server가 HTTP request/response message를 통해 데이터를 주고 받는다.
  > 3. 통신이 완료되면 TCP conncection을 종료한다.

- HTTP는 왜 비연결성인가?
  > 동시에 수많은 사용자들이 broswer를 사용하더라도 모든 사용자가 끊임없이 Server에 request를 보내는 것이 아니기 때문에 실제로 Server가 동시에 처리하는 요청은 상대적으로 적다. 따라서 연결을 불필요하게 유지하지 않음으로써 서버 자원을 효율적으로 사용하기 위함이다.

- 프록시와 프록시 서버에 대해 설명해주세요.
  > Server와 Client 사이에서 Web cache의 역할을 하는 서버를 말한다. Server에 요청되는 Client의 request의 일부를 중간에서 처리함으로써 response time과 traffic을 줄이기 위한 용도로 사용된다.

- 클라이언트와 서버는 무엇인가요?
  > 클라이언트는 서버를 사용하는 사용자이며, 서버는 클라이언트에게 네트워크를 통해 서비스를 제공하는 시스템을 말한다.

- cookie와 session에 대해 설명해주세요.
  > 두 가지 모두 Web 통신에서 client의 정보를 유지하기 위해 사용되는 방법이다.  
  > Cookie는 cookie file의 형태로 각 client의 host device에 저장되지만, session은 client가 접속 중인 웹 서버 DB에 저장된다.

- cookie를 쓰는 이유를 설명해주세요.
  > HTTP는 stateless protocol이므로 과거의 client request history를 기억하고 있지 않기 때문에, Server에서 client의 transaction history를 보관하기 위해 사용한다.
  
### ⚡️ Chapter 2-4, 2-5

- 도메인과 DNS가 무엇인지 설명해주세요.  
  > 인터넷 호스트와 라우터는 IP 주소로 식별되는데, 외우기 어려운 IP 주소 대신 '도메인'이라는 사람이 읽기 쉬운 이름으로 구분하기도 한다. 이때 사용자가 도메인 이름을 통해 접근하면 이를 실제 네트워크 상에서 사용하는 IP 주소로 변환하여 접속해야 하는데, 이러한 변환 시스템을 'DNS'라고 한다.

- Domain Name Server의 구조를 설명해주세요.
  > 트리 형태의 3단계 계층 구조로 구성되어 있다.  
  > - 최상단에는 Root DNS Server들이 존재한다. .com, .net, .edu 등 가장 큰 범위의 각 도메인을 담당하고 있는 TLD server들이 누구인지에 대한 정보를 가지고 있다. 
  > - 중간단에는 TLD(Top Level Domain) server들이 존재한다. .com, .net 등의 큰 도메인이나, .kr, .jp 등의 국가 도메인을 하나씩 담당하고 있는 서버이다. 각 도메인 내의 속한 기관, 그룹 도메인들을 담당하는 각 authoritative DNS server들이 누구인지에 대한 정보를 가지고 있다.  
  > - 최하단에는 authoritative DNS server들이 존재한다. 어떤 기관, 그룹 내의 모든 host들에 대한 hostname -> IP 매핑 정보를 보유하고 있다.  
  > - 계층 구조에 속하지 않지만 local DNS name server가 존재한다. host와 DNS 사이에 존재하며 일종의 proxy의 역할을 수행한다.

- Domain Name System 동작과정을 설명해주세요.  
  > - host에서 어떠한 hostname에 대한 IP 주소 변환을 요청한다.
  > - local DNS server는 자신이 해당 hostname에 대한 IP 주소 변환 정보를 이미 가지고 있다면 알려주고, 그렇지 않으면 다른 DNS server에 접근한다.
  > - 이후 단계는 iterated query / recursive query 방식에 따라 나뉜다.  
  > - **iterated query** : "나는 모르니까, 아는 애를 알려줄게."
  > > - local DNS server는 root DNS server에게 요청하여 다음으로 접근할 TLD server 정보를 얻는다.
  > > - TLD server에 접근하여 다음으로 접근할 authoritative 정보를 얻는다.
  > > - authoritative DNS server에 접근하여 실제 hostname -> IP 매핑 정보를 얻는다.
  > > - host에게 정보를 전달한다.  
  > - **recursive query** : "나는 모르니까, 내가 알아올게."  
  > > - local DNS server가 root DNS server에게 정보를 요청한다.
  > > - root DNS server가 다시 TLD server에게 정보를 요청한다.
  > > - TLD server가 다시 authoritative DNS server에 접근하여 실제 hostname -> IP 매핑 정보를 얻는다.
  > > - 차례로 되돌아가서 host에게 정보를 전달한다. 
  
  ### ⚡️ Chapter 2-6, 3-1

- TCP와 UDP의 특징과 차이점을 설명해주세요.
  > TCP : 연결형 서비스(one sender - one receiver, 3-way hand shaking을 통해 연결하고 4-way handshaking을 통해 해제) / 높은 신뢰성(in-order byte stream) / UDP보다 느린 전송 속도 / Full duplex / 흐름 제어, 혼잡 제어 있음
  > UDP : 비연결형 서비스(client와 server 사이에 connection 불필요) / 낮은 신뢰성(손실 발생, out-of-order delivery) / TCP보다 빠른 전송 속도 / 흐름 제어, 혼잡 제어 없음
- TCP/UDP 헤더 구조
  > **TCP header**  
  > - source port number / destination port number
  > - sequence number : application data field의 첫 번째 data byte가 이번 connection에서 몇 번째로 읽는 data byte인지를 의미
  > - acknowedgement number : 상대방이 보낸 데이터에 대한 ack
  > - head len : header만의 길이 (TCP header는 길이가 가변적)
  > - receive window : receiver로부터 ack을 받지 않아도 일방적으로 보내도 되는 데이터의 제한 크기 (receiver의 buffer 사이즈)
  > - checksum : header fields를 포함한 segement 전체 contents의 오류가 있는 지를 확인하기 위한 field
  > - flags
  >   - R, S, F flag : connection establish에 대한 비트 (Reset, Sync, Final)
  >   - A flag : acknowledgement number field에 확인해야 할 ack 값이 있는 지에 대한 여부
  >   - U, P flag : urgent한 segment인지 여부(즉시 다음 계층으로 보냄) / 바로 push해야 하는지 여부(해당 segment를 포함하여 버퍼에 있는 모든 segment를 즉시 다음 계층으로 push)  
  > - urgent pointer : urgent한 데이터의 위치 (U flag가 설정된 경우에만 유효)
  > - options : 가변적인 fields  
  > **UDP header**  
  > - source port number / destination port number
  > - length : header를 포함한 UDP segment 길이
  > - checksum : header fields를 포함한 segement 전체 contents의 오류가 있는 지를 확인하기 위한 field  
  
- TCP를 사용하는 대표적인 프로토콜은 무엇인가요?
  > 

- TCP 연결 끊김 탐지에는 무엇이 있는지 설명하시오.
  > 

- UDP에서 신뢰도를 보장하는 방법을 설명해주세요.
  > application layer에 reliablility를 추가한다.

- UDP 서버의 특징에 대해서 설명하세요.
  > - Connection이 불필요하기 때문에 서버 소켓과 클라이언트 소켓의 구분이 없다.
  > - 크기가 고정된 datagram 단위로 전송되며, 크기를 초과하면 잘라서 보낸다.
  > - 서버와 클라이언트가 1:1, 1:N, N:M 으로 연결될 수 있다.
  > - 신뢰성이 요구되는 서비스보다 성능이 중요한 서비스를 위해 사용된다.

- UDP는 어느 상황에서 사용하는지 설명하세요.
  > - 손실에 대한 내성이 있고, 전송률이 중요한 streaming multimedia app
  > - 한번만 request/response를 주고받으면 되는 DNS
