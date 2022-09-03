# Computer Network

### ⚡️ Chapter 1-1, 1-2

- 프로토콜이란?
    > 인터넷 통신을 하는데 필요한 정해진 규약들을 의미한다.

- 패킷이란?
    > Host가 Packet Switching을 하는 과정에서 하나의 link로 데이터를 보낼 때 만약 너무 긴 데이터의 경우 이를 효율적으로 전송하기 위해 작은 단위로 데이터를 분할하게 되는데 이때 작은 단위의 데이터를 Packet이라고 한다.

- 네트워크, 인터넷의 개념을 설명해주세요
    > 네트워크는 Host 및 End System들과 인터넷을 연결해주는 연결망이다. 인터넷은 네트워크의 네트워크, 즉 네트워크들이 모인 네트워크이며 Host, Router, Communication Link로 이루어져 있다.

- ISP란?
    > Ethernet에서 사용되는 line이며, Ethernet Switch를 한 곳에 모은 institutional Router와 인터넷을 직접 연결해주는 dedicated line이다.

- DSL이란?
    > 전화를 하는데 필요한 access network로 다른 network와 데이터를 공유하지 않는 dedicated line이다. 평균적으로 downstream의 속도가 upstream의 속도보다 빠르다.

- Ethernet에 대해 설명하세요.
    > 학교나 기관에서 사용되는 access network이다. 각 Host들을 한 곳에 모으는 Ethernet Switch가 있고 이들은 다시 institutional Router로 연결된다. 이때, DSL이나 Cable Network와는 다르게 ISP라는 dedicated line으로 바로 인터넷과 연결된다.

- LAN에 대해 설명하세요.
    > Wi-Fi나 cellular network를 지칭하는 access network이다. Ethernet Switch에 직접 연결되는 구조를 띠며 Wi-Fi는 범위가 좁은 대신 대역폭이 크고, celluar network는 범위가 넓은 대신 대역폭이 상대적으로 작다는 특징을 가진다.

### ⚡️ Chapter 2-1, 2-2, 2-3

- port란 무엇인가요? Well-Known Port에 대해 설명해주세요.
    > port란 host 안에서 실행되고 있는 process를 정의해주는 identifier이다. Well-Known Port는 번호가 고정되어 있는 상태로 자주 사용되는 port를 의미하며 대표적인 예로 HTTP Server Port Number 80, Mail Server Port Number 25가 있다.

- 클라이언트와 서버의 통신 과정에 대해 설명해주세요.
    > 클라이언트는 서버에게 connection을 initiate하고 서버는 on 상태를 유지한 채 대기하다가 클라이언트의 connection 요청을 수락하게 된다. connection 요청 수락 후 클라이언트는 connection socket을 통해 request message를 전송한다. server는 해당 request message를 확인하고 request된 object를 담은 response message를 작성하여 전송한다. 모든 전송 과정이 끝나면 서버는 connection을 종료한다.

- HTTP method 4가지를 설명하시오.
    > HTTP의 method에는 HTTP 1.0과 1.1을 기준으로 GET, POST, HEAD, PUT, DELETE가 있다. GET은 server에 데이터를 요청(request)할 때 사용하는 method이며, POST는 데이터를 추가 및 변경이 필요할 때 사용하는 method이다. HEAD는 server에 request를 보내긴 하지만 object를 받지 않는 경우이며 주로 개발 과정에서 많이 사용된다. PUT은 server의 URL에 파일을 업로드하는 method이고, DELETE는 URL 영역에 있는 파일을 삭제하는 method이다. PUT과 DELETE는 remote로 server 내의 파일을 직접적으로 건드리기 때문에 관리자 권한일 경우에만 사용 가능하도록 해야한다.

- HTTP의 GET 방식과 POST 방식을 비교해주세요.
    > GET은 client가 server에 필요한 데이터를 요청할 때 사용하는 method이며, post는 데이터의 추가나 변경이 일어났을 때 사용하는 method이다.

- HTTP 1.0, 1.1, 2.0 차이점은 무엇인가요?
    > HTTP 1.0는 서버에게 웹페이지를 요청하는 받는 method들로 이루어져 있다. method로는 GET, HEAD, POST가 있으며 response 직후 종료되는 connection 특성을 갖고 있다. HTTP 1.1는 HTTP 1.0과 다르게 데이터의 pipelining이 일어나기 때문에 requst-response 이후로도 동일한 연결을 재사용할 수 있다. method로는 GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS이 있으며, response 직후로도 계속 연결이 유지된다는 long-lived한 connection 특성을 갖고 있다. HTTP 2.0은 기존의 HTTP 1.0과 1.1의 프로토콜을 계승하면서도 성능 향상에 초점을 맞췄다. HTTP 2.0는 한 connection으로 동시에 여러 개의 메시지를 주고 받을 수 있으며, response는 순서에 상관없이 stream으로 주고받을 수 있도록 하는 multiplexing 기능이 존재한다.

- HTTP의 특징에 대해 설명하시오.
    > HTTP는 server가 client가 보낸 request history를 전혀 기억하지 않는 stateless한 특징을 가진다.

- HTTP와 HTTPS의 차이에 대해 설명하세요.
    > HTTP는 따로 암호화 과정을 거치지 않기 때문에 중간에 패킷을 가로챌 수 있고, 수정할 수 있기 때문에 상대적으로 보안에 취약하다. 이를 보완하기 위해 나온 것이 HTTPS이며 HTTPS는 중간에 암호화 계층을 거쳐서 패킷을 암호화하게 된다.

- HTTP의 Status Code의 종류는 어떻게 되나요?
    > HTTP의 Status Code의 종류는 총 5가지이며 각각 200 OK, 301 Moved Permanently, 400 Bad Request, 404 Not Found, 505 HTTP Version Not Supported가 있다. 200 OK는 request가 성공하여 response의 body 부분에 요청한 object가 잘 들어갔음을 나타낸다. 301 Moved Permanently는 request된 object가 다른 곳에 저장되었음을 나타낸다. 400 Bad Request는 request message가 잘못되었음을 나타낸다. 404 Not Found는 request message에는 오류가 없지만 reqeust된 document가 현재 웹 서버에 없음을 의미한다. 505 HTTP Version Not Supported는 client의 HTTP 버전을 server가 수용할 수 없음을 의미힌다.

- HTTP 헤더의 구조에 대해서 설명해 주세요.
    > HTTP의 헤더는 HTTP Server의 이름인 Host, client의 브라우저인 User-Agent, Accept, 웹페이지의 특정 language를 요청하는 Accept-Language, Accept-Encoding, Accept-Charset, keep-Alive, TCP Connection의 상태를 결정하는 Connection으로 이루어져 있다. 헤더는 몇 줄의 line이 올 지 알 수 없으므로 carriage return과 line feed의 유무로 헤더의 끝을 파악한다.

- 주소창에 URL을 치고 엔터를 치면 흐름이 어떻게 되나요?
    > 클라이언트는 우선 서버에 TCP Connection을 요청하고 대기 중인 서버는 이를 수락하게 된다. 만약 TCP Connection에 성공하면 클라이언트는 해당 URL 접속에 필요한 object들을 요청하는 request message를 보내게 된다. 서버는 reqeust message를 확인 후 request된 object들을 담은 response message를 작성하여 다시 클라이언트에게 전송한다. 그리고 클라이언트는 response message 내의 object들로 해당 URL의 HTML을 화면에 띄운다.

- HTTP는 왜 비연결성인가?
    > HTTP의 서버가 다수의 클라이언트들과 연결을 계속 유지해야 할 경우, 더 이상의 통신이 없는 클라이언트들과의 연결을 끊음으로써 서버 자원의 낭비를 막을 수 있고 이를 통해 더 많은 클라이언트들과의 연결이 가능해지기 때문이다.

- 프록시와 프록시 서버에 대해 설명해주세요.
    > 프록시란 직접 통신이 아닌 중간 단계를 거쳐 통신함을 의미하며 프록시 서버는 cache를 local site 내에 두어 original server까지 직접 도달하지 않더라고 object를 직접 가져올 수 있게 하는 Web cache이다.

- 클라이언트와 서버는 무엇인가요?
    > 클라이언트는 다른 프로그램에게 서비스를 request하는 프로그램이며 서버는 들어오는 request에 응답하고 이에 해당하는 response를 보내주는 프로그램이다.

- cookie와 session에 대해 설명해주세요.
    > 데이터를 필연적으로 유지해야 하는 경우 HTTP 프로토콜의 stateless 특성을 대처하기 위해서 cookie와 session을 사용한다. cookie와 session의 차이점은 크게 상태 정보의 저장 위치이며 cookie는 클라이언트에 저장하고, session은 서버에 저장한다. cookie는 사용자가 어떠한 웹 사이트를 방문할 경우, 그 사이트가 사용하고 있는 서버에서 사용자의 컴퓨터에 저장하는 작은 기록 정보 파일이며, session에 비해 보안은 취약하나 서버 자원을 덜 사용하기 때문에 자원의 낭비를 방지하며 속도가 빠르다는 특징을 가진다. session은 일정 시간동안 같은 클라이언트로부터 들어오는 일련의 요구를 하나의 상태로 보고, 그 상태를 일정하게 유지시키는 기술이며 보안이 cookie에 비해 강력하나 서버 자원을 사용하기 때문에 속도와 자원의 측면에서 조금은 불리하다는 특징을 가진다.

- cookie를 쓰는 이유를 설명해주세요.
    > HTTP Protocol 자체는 stateless하지만 server 자체에서 client들의 transaction history를 유지하기 위해 cookie를 사용한다.
