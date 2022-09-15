# Computer Network

### ⚡️ Chapter 1-1, 1-2

- 프로토콜이란?
    > 인터넷 네트워크 통신에서 메시지를 주고 받는 format, order 또는 메시지를 받았을 때의 action을 정의하고 제어하는 표준화 규칙이다.

- 패킷이란?
    > 네트워크에서 Hosts 간에 데이터를 주고 받을 때 전송되는 데이터의 단위(조각)이다. packet에는 그 packet이 가야 하는 목적지의 주소가 포함된다.

- 네트워크란? 
    > 네트워크란, 여러 개의 host들이 통신 기술을 통해 그물망처럼 연결되어 서로 통신할 수 있는 형태를 의미한다. 네트워크의 종류에는 LAN, WAN등이 존재한다.

- 인터넷이란?
    > 인터넷이란, network of networks이며 Host, Router, Communication Link로 이루어져 있다.

- ISP란?
    > ISP는 Internet Service Provider의 약자이다. 인터넷 서비스 제공자로, 개인이나 단체에게 인터넷에 접속하는 수단을 제공하는 주체를 의미한다.

- DSL이란?
    > DSL은 Digital Subscriber Line의 약자로, 전화 회사에서 제공하는 Access network이다. 다른 network와 데이터를 공유하지 않는 Dedicated network이다.

- Ethernet에 대해 설명하세요.
    > 기업이나 학교 등의 대규모 host들을 인터넷에 연결할 때 사용하는 네트워크 구조로, 각각의 host가 ethernet switch에 연결되고, 이러한 switch들을 하나로 뭉치는 학교 전체의 institutional Router가 ISP가 직접 연결되어 인터넷에 연결되는 구조가 많다. (내용 보충 필요)

- LAN에 대해 설명하세요.
    > LAN은 Local Area Network의 약자로, 집, 사무실, 학교 등 좁은 범위 내에서 네트워크가 연결된 것을 의미한다. 예를 들어 Wifi가 있다.

- TCP/IP 프로토콜과 각 계층 설명하시오.
    > TCP/IP 프로토콜은 전송 조절 프로토콜인 TCP와 인터넷 프로토콜인 IP가 합쳐진 프로토콜으로, 주로 5계층으로 나뉜다.  
Applicaiton : network application에서 생성한 data를 캡슐화하여 메시지로 만든다.  
Transport : source process에서 destination process로 메시지를 전송한다.  
Network : source host로부터 destination host로 전송한다.  
Link : 데이터를 한 hop씩 전송한다.  
Physical : 실제로 데이터를 실어나른다.  

### ⚡️ Chapter 2-1, 2-2, 2-3

- port란 무엇인가요? Well-Known Port에 대해 설명해주세요.  
    > port란 host 안에서 실행되고 있는 process를 정의해주는 identifier number이다. Well-Known Port는 잘 알려진 포트라는 의미로 0~1023까지의 포트번호를 의미하며, HTTP server(port 80), Mail server(port25)가 있다.  
    
- 클라이언트와 서버를 정의하시오.
    > client는 request하는 host이고, server는 request에 대한 response을 해주는 host이다. 
    
- HTTP method 4가지를 설명하시오.  
    > 1) GET (Read): resource를 얻는다. 브라우저를 이용해서 서버로부터 웹 페이지, 이미지 등을 가져올 때 사용한다. 요청 파라미터는 Head에 위치하게 되어 URL에 그대로 노출된다.  
    > 2) POST (Create): resource를 생성하고 resource의 데이터를 추가한다. 요청 파라미터는 Body에 위치하게 되어 URL에 보여지지 않는다.  
    > 3) PUT (Update): URL에 등록하고자 하는 경로를 지정하고, server에 전달하여 resource(파일)을 추가/수정한다.  
    > 4) DELETE (Delete): URL을 통해 파일의 경로를 server에게 전달하여 해당 경로의 resource(파일)을 삭제한다.  
    
- HTTP의 GET 방식과 POST 방식을 비교해주세요.  
    > GET은 서버의 리소스에서 데이터를 요청할 때, POST는 서버에 리소스를 새로 생성하거나 추가/업데이트할 때 사용한다. 또한, GET은 URL 파라미터에 요청하는 데이터를 담아 보내기 때문에 HTTP 메시지에 body가 없다. 반면에 POST는 body 에 데이터를 담아 보내기 때문에 HTTP 메시지에 body가 존재한다.
    
- HTTP의 특징에 대해 설명하시오.  
    > 1) Client-Server 구조를 가진다.  
    > 2) Client/Server가 request/response message를 통해 통신한다.  
    > 3) Stateless이다. 과거의 Client가 보낸 request history를 저장하고 있지 않는다.  
    > 4) Connectionless이다. Client는 Server로부터 response를 받고나면 연결을 유지하지 않고 끊어버린다.  
    
- HTTP 1.0, 1.1, 2.0 차이점은 무엇인가요?  
    > 1) HTTP 1.0는 서버에게 웹페이지를 요청하는 메소드인 GET, HEAD, POST가 사용되며, response 직후 connection이 종료되는 비연결성을 갖고 있다.  
    > 2) HTTP 1.1는 HTTP 1.0과 다르게 데이터의 pipelining이 일어나기 때문에 requst-response 이후로도 동일한 연결을 재사용할 수 있다. method로는 GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS이 있다.  
    > 3) HTTP 2.0은 HTTP 1.1에서 request를 순차적으로 처리하면서 앞의 delay가 뒤의 request에게 영향을 끼치는 HOL blocking 문제를 해결하기 위해 multi-streaming을 사용하여 하나의 connection에서 동시에 여러 개의 stream을 생성하고, 들어온 request들을 병렬 처리하는 multi-plexing 방식으로 해당 문제를 해결하였다.

- HTTP와 HTTPS의 차이에 대해 설명하세요.  
    > HTTP는 따로 암호화 과정을 거치지 않기 때문에 중간에 패킷을 가로챌 수 있고, 수정할 수 있기 때문에 상대적으로 보안에 취약하다. 이를 보완하기 위해 나온 것이 HTTPS이며 HTTPS는 중간에 암호화 계층을 거쳐서 패킷을 암호화하게 된다. HTTP는 80번 포트를, HTTPS는 443번 포트를 사용한다.
    
- HTTP의 Status Code의 종류는 어떻게 되나요?  
  > - 1xx(정보) : 요청을 받았으며 프로세스를 계속 진행합니다.   
  > - 2xx(성공) : 요청을 성공적으로 받았으며 인식했고 수용하였습니다.  
  > - 3xx(리다이렉션) : 요청 완료를 위해 추가 작업 조치가 필요합니다.  
  > - 4xx(클라이언트 오류) : 요청의 문법이 잘못되었거나 요청을 처리할 수 없습니다.  
  > - 5xx(서버 오류) : 서버가 명백히 유효한 요청에 대한 충족을 실패했습니다.   
    
- 주소창에 URL을 치고 엔터를 치면 흐름이 어떻게 되나요?  
    > 1) 클라이언트(브라우저)는 우선 서버의 80번 포트에 TCP Connection을 요청하고 대기 중인 서버는 이를 수락한다.
    > 2) TCP Connection에 성공하면 클라이언트는 해당 URL 접속에 필요한 object들을 요청하는 request message를 보내게 된다.
    > 3) 서버는 reqeust message를 확인 후 request된 object들을 담은 response message를 작성하여 다시 클라이언트에게 전송한다.
    > 4) 클라이언트는 response message 내의 object들로 해당 URL의 HTML을 화면에 띄운다.
    > 5) 통신이 완료되면 TCP conncection을 종료한다.

- HTTP는 왜 비연결성인가?  
    > HTTP 서버가 다수의 클라이언트들과 연결을 계속 유지해야 하는 경우 자원의 낭비가 심하다. 통신이 없는 클라이언트들과의 연결을 끊어 더 많은 클라이언트들과의 연결이 가능해지고 서버 자원을 효율적으로 사용할 수 있다.
    
- 프록시와 프록시 서버에 대해 설명해주세요.  
    > 프록시는 직접 통신이 아닌 중간 단계를 거쳐 통신하는 것을 의미하며, 프록시 서버는 server와 client 사이에서 Web cache의 역할을 하는 서버를 의미한다. server에 요청되는 client의 request의 일부를 중간에서 처리함으로써 response time과 traffic을 줄이기 위한 용도로 사용된다.

- cookie와 session에 대해 설명해주세요.  
    > cookie와 session 모두 HTTP의 특징인 stateless를 보완하기 위해 사용한다. cookie와 session의 차이점은 크게 상태 정보를 저장하는 위치이며 cookie는 클라이언트에 저장하고, session은 서버에 저장한다. cookie는 사용자의 정보가 client에 저장되어 HTTP 헤더에 쿠키를 넣어 request를 하는 반면, session은 서버에 저장되는 데이터로 서버에 접속할 때 받은 세션 ID 쿠키를 사용하여 저장하고 이를 헤더에 넣어 서버에 저장된 정보를 확인한다. 보안성은 세션이 높으나 속도는 쿠키가 빠르다.

### ⚡️ Chapter 2-4, 2-5

- 도메인과 DNS가 무엇인지 설명해주세요.  
    > 도메인이란, 인터넷에 연결된 호스트의 IP를 사람이 쉽게 기억하기 어렵기 때문에 이를 위해서 각 IP에 사람이 쉽게 기억하고 입력할 수 있도록 문자(영문, 한글 등)로 만든 인터넷 주소를 의미한다. 예를 들어 114.108.157.19처럼 되어있는 실제 IP 주소를 daum.net으로 하는 것과 같은 것이다.   

    >  DNS(Domain Name System)란, 도메인 주소와 IP 주소를 매핑해주는 데이터베이스 시스템을 의미한다.  


- Domain Name 구조를 설명해주세요.  
    > 트리 형태의 계층 구조로 구성되어 있다.  

    > - 최상단에는 Root DNS Server들이 존재한다. .com, .net, .edu 등 가장 큰 범위의 각 도메인을 담당하고 있는 TLD server들이 누구인지에 대한 정보를 가지고 있다. 

    > - 두 번째단에는 TLD(Top Level Domain) server들이 존재한다. .com, .net 등의 큰 도메인이나, .kr, .jp 등의 국가 도메인을 하나씩 담당하고 있는 서버이다. 각 도메인 내의 속한 기관, 그룹 도메인들을 담당하는 각 authoritative DNS server들이 누구인지에 대한 정보를 가지고 있다. 

    > - 세 번째단에는 authoritative DNS server들이 존재한다. 어떤 기관, 그룹 내의 모든 host들에 대한 hostname -> IP 매핑 정보를 보유하고 있다. 

    > - 최하단에는 host가 존재하게 된다. 

    > - 계층 구조에 속하지 않지만 local DNS name server가 존재한다. host와 DNS 사이에 존재하며 일종의 proxy의 역할을 수행한다.  


- Domain Name System 동작과정을 설명해주세요.
    > 1) 웹 브라우저에 도메인 주소(ex> www.google.com)를 입력한다.  
    > 2) host는 local DNS server에 도메인 주소의 IP 주소를 요청한다.  
    > 2-1) Local DNS server에 IP 주소가 있는 경우, 컴퓨터에게 IP 주소를 응답해준다.  
    > 2-2) Local DNS server에 IP 주소가 없는 경우, Root DNS server에 IP 주소를 요청한다.  
    > 3) Root DNS server는 '.com'의 TLD server에게 요청하라고 Local DNS server에게 TLD server의 주소를 알려준다.  
    > 4) TLD server는 해당 도메인의 authoritative DNS server에게 요청하라고 Local DNS server에게 authoritative DNS server의 주소를 알려준다.  
    > 5) 위의 과정을 반복하다보면 DNS Server가 알고자하는 IP 주소를 알고 있는 name 주소에 도달해서 IP 주소를 얻을 수 있게 된다.
