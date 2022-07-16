# Operating System

### ⚡️ Chapter 1-2. Introduction & OS Stuructures

- 운영체제란 무엇인가?
  > 컴퓨터 하드웨어를 관리하는 소프트웨어이자 컴퓨터에서 항상 실행 중인 프로그램이다. 응용 프로그램을 위한 기반(system service)을 제공하며, 컴퓨터 사용자와 컴퓨터 하드웨어 사이에서 중재자 역할을 하면서 사용자가 하드웨어를 직접 조작하는 것을 방지한다. 

- 운영체제의 주요 목적은?
  > 다양한 사용자를 위해 다양한 응용 프로그램 간의 하드웨어 사용을 제어하고 조정한다. 이를 통해 사용자 편의성과 시스템 효율성을 높이는 것을 목적으로 한다.

- 커널이란 무엇인가?
  > 운영체제의 핵심 기능을 의미한다. 운영체제 자체도 소프트웨어이므로 컴퓨터 시스템에서 수행되기 위해선 메모리에 프로그램이 올라가 있어야 한다. 하지만 운영체제는 규모가 매우 크기 때문에 모두 메모리에 올라간다면 메모리 공간의 낭비가 발생할 수 있으므로, 항상 필요한 부분만을 메모리에 올려놓고 사용하게 된다. 이때 메모리에 상주하는 운영체제의 부분을 커널이라고 한다.

- 부팅이 되는 과정은?
  > 컴퓨터의 전원이 켜지면 Boot-ROM에 저장되어 있는 Bootstrap Program이 실행된다.  
  > 1. Bootstrap Program은 가장 먼저 CPU 레지스터, 메모리 등 컴퓨터 시스템 하드웨어를 초기화한다. 
  > 2. 하드 디스크 드라이브에서 운영체제 프로그램을 메인 메모리의 첫 번째 주소 위치에 로드한 후, PC 레지스터에 해당 주소를 저장한다. 
  > 3. 운영체제 프로그램 실행이 시작된다. 

- 시스템 콜에 대해 설명하세요
  > 사용자(응용프로그램)가 운영체제(커널)의 서비스를 사용할 수 있도록 하는 인터페이스이다. 특정 저수준 작업은 어셈블리 언어로, 대부분은 C, C++ 같은 HLL로 작성된 함수 형태로 제공된다.  
  > 시스템 콜의 종류는 크게 프로세스 제어, 파일 조작, 장치 조작, 정보 유지 보수, 커뮤니케이션, 보안으로 묶인다. 

- 멀티프로세싱과 멀티프로그래밍의 차이는?
  > * __멀티프로세싱__ : 다수의 프로세서(CPU)가 다수의 프로세스를 서로 협력적으로 처리하는 것, 프로그램을 더 빨리 처리하기 위함이 목적
  > * __멀티프로그래밍__ : 단일 프로세서(CPU)가 다수의 프로세스가 동시에 처리하는 것, CPU의 활용도를 최대화하기 위함이 목적

- 메모리 계층 구조의 순서가 어떻게 되는가? CPU에서 가까운 순으로 말해보시오.
  > 레지스터 - 캐시 - 메인 메모리 - 비휘발성 메모리 - 하드 디스크 드라이브 - 광학 디스크 - 자기 테이프 순이다.  

----------------------------------------------------------------------------------------------------------------
  
### ⚡️ Chapter 3. Processes

- Heap과 Stack의 차이점은 무엇인가요?
  > * __Heap__ : FIFO, 프로그램의 런타임 중에 동적으로 할당되는 메모리가 저장되는 영역이다.  
  > * __Stack__ : LIFO, 함수 호출 시 함수 파라미터, return 주소, 지역 변수 등 임시 데이터의 저장장소이다. 

- 프로세스에 할당되는 메모리의 각 영역에 대해서 설명해 주세요.
  > * __Text__ : Code 혹은 Instruction 영역이라고도 하며, 프로그램 코드가 저장되어 있다. 고정 크기이다.
  > * __Data__ : 전역 변수를 저장하고 있는 영역이다. 고정 크기이다.
  > * __Heap__ : 프로그램의 런타임 중에 동적으로 할당되는 메모리가 저장되는 영역이다. 가변 크기이다.
  > * __Stack__ : 함수 호출 시 함수 파라미터, return 주소, 지역 변수 등 임시 데이터의 저장장소이다. 가변 크기이다.

- 프로세스와 그 특징에 대해 설명하세요
  > 프로세스란 쉽게 말해 실행 중인 프로그램이며 CPU의 모든 활동을 말한다. 운영체제 내의 작업의 단위이다.   
  > 프로세스는 메모리 내에 여러 구역으로 구성되어 배치된다. Text 영역에는 프로그램의 코드, Data 영역에는 전역/static 변수, Heap 영역에는 프로그램 런타임 중 동적으로 할당되는 메모리, Stack 영역에는 함수 호출 시의 임시 데이터가 저장된다.  
  > 프로세스는 실행되는 동안 여러 상태를 가지며 변화한다. New는 프로세스가 생성 중일 때, Running은 명령어들이 실행 중일 때, Waiting은 특정 이벤트가 발생하기를 기다릴 때, Ready는 프로세서가 할당되기를 기다릴 때, Terminated는 실행이 종료되었을 때의 상태를 말한다. 

- 프로세스가 종료되는 두 가지 조건은?
  > - 첫 번째는 프로세스가 마지막 문장의 실행을 끝내고, exit() 시스템 콜을 사용하여 OS에 자신의 삭제를 요청하여 종료한다. 이때 프로세스는 자신을 기다리는 부모 프로세스의 wait() 호출에 의해 상태 값을 반환하고, 물리 메모리, 가상 메모리, 열린 파일, 입출력 버퍼 등의 모든 자원을 OS에 반환한다.  
  > - 두 번째는 부모 프로세스가 자식 프로세스를 종료시키는 것이다. 부모 프로세스가 자식의 pid 값을 이용해 적절한 시스템 콜을 호출하여 자식 프로세스의 종료를 유발할 수 있다. 이때 부모 프로세스만이 이러한 시스템 콜을 호출할 수 있다.

- 인터럽트 발생 처리과정을 설명하세요.
  > CPU가 컨트롤러가 인터럽트 요청 라인에 신호를 보낸 것을 감지하면, 현재 실행 중인 현재 모든 레지스터 내용을 스택 영역 혹은 PCB에 저장한다.  
  > 그 후 인터럽트 번호를 읽고 해당 번호를 인터럽트 벡터의 인덱스로 사용하여 인터럽트 서비스 루틴(ISR)로 점프하고 인터럽트를 처리한다.  
  > 인터럽트 서비스 루틴의 실행이 종료되면, 저장해놓았던 레지스터 내용을 다시 복구하여 중단됐던 프로그램을 이어서 실행한다. 

- 인터럽트 기능이 없었다면 사용하는 방식에 대해 설명하세요.
  > 인터럽트 기능이 없었다면 컨트롤러는 어떤 일을 할 때를 알기 위해 계속 체크해야 하며, 이를 **폴링(Polling)** 이라고 한다. 폴링은 CPU가 다른 프로그램이나 입출력 장치들에서의 상태 변화를 지속적으로 계속 확인하고 그에 따라 프로그램을 처리하는 방식이다. 인터럽트 방식에 비해 구현이 간편하다는 장점이 있지만 다른 프로그램이나 장치들 간의 폴링이 많아질수록 CPU 사용량이 늘어나 성능이 크게 떨어지게 되며, 폴링의 주기가 길어질수록 반응 속도가 늦어져 실시간성이 떨어진다는 단점이 있다.

- 프로세스의 생성 과정에 대해 설명해보세요.
  > 1. 생성된 새로운 프로세스에 프로세스 id를 할당한다.  
  > 2. 프로세스의 모든 구성 요소를 포함할 수 있는 주소 공간과 PCB 공간을 할당한다.  
  > 3. PCB를 초기화한다. 프로그램의 코드는 Text 영역, 초기화된 전역/static 변수는 Data 영역에 저장되며 Heap과 Stack 영역은 초기 메모리 주소만 초기화된다. 그 외에 프로세스의 상태 정보, 프로그램 카운터, 우선순위 등이 초기화된다.
  > 4. PCB에 여러 정보가 기록되면 Ready Queue에서 CPU를 할당받기를 대기한다. 

- IPC의 통신 과정 설명하세요.
  > IPC의 방식에는 Shared Memory 방식과 Message Passing 방식 두 가지가 있다.  
  > **Shared Memory** 방식은 둘 이상의 프로세스가 공유하는 메모리 영역을 두고 해당 메모리 영역에 데이터를 채우거나 소비하는 등 변경하는 데이터를 공유하는 방식으로 통신한다.  
  > **Message Passing** 방식은 두 프로세스가 communication link를 설정하고 서로 메시지를 주고받는 방식으로 통신하며, 이때 커널이 메시지를 전달해주며 관리한다.

- Context Switching이란 무엇인가요?
  > CPU가 인터럽트 요청에 의해 현재 실행 중인 Task(프로세스 또는 스레드)을 멈추고 다른 Task를 실행해야 할 때, 현재 진행하고 있는 Task의 상태를 PCB 또는 TCB에 저장하고 다음으로 진행할 Task를 실행할 수 있도록 상태 값을 읽어와 저장하는 교체 과정을 말한다. 

- 동기와 비동기, 블로킹과 넌블로킹의 차이는 무엇인가요?
  > Message passing 시스템에서 두 프로세스가 서로 메시지를 주고받기 위해 설정되어야 할 통신연결(communication link) 방법의 종류들이다.   
  > __동기식(synchronous)과 블로킹(Blocking)은 같은 방법을 의미하는 것이다.__ 이 방법에서 메시지 송신 시 송신자는 메시지가 수신자 혹은 메일박스에 의해 수신될 때까지 봉쇄되고, 수신 시 수신자는 메시지가 이용 가능해질 때까지 봉쇄된다.  
  > __비동기식(asynchronous)과 넌블로킹(Non-blocking)은 같은 방법을 의미하는 것이다.__ 이 방법에서 메시지 송신 시 송신자는 메시지 수신 여부에 관계없이 메시지 전송 후 작업을 이어서 하게 되고, 수신 시 수신자는 메시지 이용 가능 여부에 관계없이 유효한 메시지 또는 널(null)메시지를 수신한다.

- 프로세스 제어블록에는 어떤 정보가 담겨있나요?
  > * **Process number** : 프로세스 id (pid)
  > * **Process state** : new / ready / running / waiting / terminate / halted 등 프로세스의 상태
  > * **Program counter** : process가 다음으로 실행할 instruction의 주소
  > * **CPU registers** : AC, IR, DR, SR, General-purpose register, condition code 등의 레지스터 정보  
  > * **CPU-scheduling information** : process 우선순위, scheduling queue의 포인터 등
  > * **Memory-management information** : base/limit register의 값, page table/segment table 정보 등 
  > * **Accounting information** : CPU 사용 시간, 계정번호 등 
  > * **I/O State information** : 열린 파일들의 리스트, 이 process에 할당된 I/O 장치들

- child process, orphan process, zombie process에 대해 설명해 보시오.
  > * __child process__ : 어떤 process에서 fork() 시스템 콜을 호출하여 새롭게 생성된 process를 의미, 이때 fork()를 호출한 process는 parent process라고 한다.  
  > * __orphan process__ : 자식 프로세스가 exit() 시스템 콜을 호출하여 종료되면 사용하던 자원과 메모리는 운영체제로 반환되지만 프로세스 id와 프로세스 종료 상태 등의 정보가 프로세스 테이블에 남아있게 되는데, parent process에서 wait() 시스템 콜을 호출함으로써 자식 프로세서의 종료 상태를 회수하면 남아있던 정보까지 운영체제로 반환된다. 그러나 parent process가 wait()을 호출하지 않고 자식 프로세스보다 먼저 종료해버린 경우에 child process가 완전히 종료되지 못하고 남아있게 되는데 이때 child process를 orphan process라고 한다. UNIX 시스템에선 이 상태를 orphan process의 parent를 모든 process의 상위 프로세스인 init process로 설정하고 wait()를 호출함으로써 해결한다.  
  > * __zombie process__ : 자신은 종료되었지만, parent prcess가 아직 wait()를 호출하지 않은 상태일 때의 child process를 의미한다. 모든 프로세스는 아주 짧은 시간이나마 zombie process 상태를 머무르게 된다. zombie process를 활용하여 daemon process(background process)를 만들 때 쓰이기도 한다. 

### ⚡️ Chapter 4. Thread

- 프로세스와 쓰레드의 차이를 설명해보세요

  > 프로세스는 운영체제로부터 할당받는 작업의 단위(실행 중인 프로그램)이고, 스레드는 할당 받은 자원을 이용하는 실행 단위이다. 프로세스는 독립적인 메모리 영역을 할당받지만 스레드는 스택을 제외한 나머지 공간을 공유한다.

- 크롬 탭이 프로세스인지 쓰레드인지 설명해보세요

  > 크롬은 탭마다 PID를 가지고 있으니 Process이며 각 Tab마다 랜더링 정보나 기타 데이터를 따로 관리한다. 이로 인해 메모리를 많이 잡아먹기도 하지만 하나의 Tab에 오류가 생겼다고 모든 Tab에 영향을 끼치진 않는다.

- 멀티 프로세스와 멀티 스레드 각각의 장단점

  > - 멀티 프로세스
  >   - 장점  
  >     • 각 프로세스가 독립된 영역(code, data, stack, heap)을 갖고 있기 때문에 여러 자식 프로세스 중 하나에 문제가 발생해도 해당 프로세스에만 영향을 미친다.  
• 메모리 침범 문제를 OS 차원에서 해결하므로 안전하다.  
  >   - 단점  
  >      • 작업량이 많아지면 context switching 시 오버헤드가 발생한다.  
          • 프로세스 간의 복잡한 통신(IPC)가 필요하다.  
  > - 멀티 스레드
  >   - 장점  
  >     • 메모리 공간, 시스템 자원의 효율성이 증가한다.  
• context switching 시 교환해야 할 대상이 적으므로 비용이 적다.  
• data, heap 영역을 이용해 데이터를 주고 받으므로 스레드 간 통신이 간단하다.  
  >   - 단점  
  >     • 서로 다른 스레드가 Stack을 제외한 메모리 공간을 공유하기 때문에 동기화 문제가 발생할 수 있다.  
• 스레드 간의 자원 공유는 전역 변수(data segment)를 이용하므로 다른 스레드가 동시에 사용할 때 충돌이 발생할 수 있다.  
• 하나의 스레드에 문제가 생기면 전체 스레드가 영향을 받는다.  
• 주의 깊은 설계가 필요하며 디버깅이 까다롭다.  
• 멀티 스레드의 단점은 critical section 기법을 통해 대비할 수 있다.  

- 멀티 프로세스 대신 멀티 스레드를 사용하는 이유는 무엇입니까?

  > - Responsiveness(응답성)
  >    - 프로세스의 일부가 block 되어도, 지속적인 실행이 가능함
  >  - Resource Sharing(자원 공유)
  >    - 프로세스의 자원을 공유하여 shared memory와 message passing보다 용이
  >  - Economy(경제)
  >    - 프로세스 생성보다 효율적
  >    - 스레드 스위칭이 context switching보다 오버헤드가 적음
  >  - Scalability(확장성)
  >     - 각 프로세스들을 thread 단위로 분할하여 실행함으로써 multiprocessor 구조에서 더 큰 이점을 얻을 수 있음

- 사용자 수준의 스레드와 커널 수준의 스레드의 차이는 무엇인가요?

  > - **User threads**
  >   - user mode에서 사용되는 thread  
  >   - kernel 위에서 kernel support 없이 관리  
  >   - OS가 가진 CPU들을 자유롭게 사용할 수는 없음  
  > - **kernel threads**
  >   - kernel mode에서 사용되는 thread  
  >   - OS가 직접 관리 및 지원  
  >   - OS가 가진 CPU들을 자유롭게 사용할 수 있음  

- 스레드 풀링이란 무엇이고 장점은?

  > - Thread Pools
  >   - 프로세스를 시작할 때 아예 일정한 수의 thread들을 미리 풀로 만들어 두는 것  
  >   - 매번 사용되고 바로 폐기되는 스레드를 새로 생성하는 것은 시간 낭비  
  >   - 개수의 한계 없이 모든 요청에서 새 스레드를 생성하면 CPU 시간, 메모리 공간 등 자원이 고갈될 수 있기 때문  
  > - 장점
  >   - 새 스레드를 만들어 주기보다 기존 스레드로 서비스해 주는 것이 종종 더 빠르다.  
  >   - 스레드 풀은 임의 시각에 존재할 스레드 개수에 제한을 둔다. 이러한 제한은 많은 수의 스레드를 병렬 처리할 수 없는 시스템에 도움이 된다.  
  >   - 태스크를 생성하는 방법을 태스크로부터 분리하면 태스크를 실행을 다르게 할 수 있다. 예를 들어 태스크를 일정 시간 후에 실행되도록 스케줄 하거나 혹은 주기적으로 실행시킬 수 있다.  
  
### ⚡️ Chapter 5. CPU Scheduling
 
- CPU 스케줄링이란 무엇인가요?  
  > 프로세스가 작업을 수행할 때, 언제 어떤 프로세스에 CPU를 할당할지를 결정하는 방법이다. 어떤 프로세스가 대기해야 할 경우, OS가 CPU를 그 프로세스로부터 회수하고 다른 프로세스에 할당하여 **CPU를 쉬지 않도록 바쁘게 유지하여 CPU의 이용률을 최대화하는 것**이 목표이다.

- CPU Scheduling은 언제 발생하는가?  
  > - case1. Running state -> Waiting State  
  >   ex) I/O 요청, 자식 프로세스의 종료를 기다리기 위해 wait() 호출
  > - case2. Running state -> Ready state  
  >   ex) interrupt 발생 시  
  > - case3. Waiting state -> Ready state  
  >   ex) I/O 종료 시  
  > - case4. Terminate  
  > case1 & 4의 경우, 프로세스가 스스로 CPU를 release 하는 상황 -> 무조건 Non-preemptive  
  > case2 & 3의 경우, ready queue에 새로운 프로세스가 추가되는 상황 -> Preemptive / Non-preemptive 선택

- CPU 스케줄링 종류와 방법에는 대표적으로 어떤 것들이 있나요?  
  > - **FCFS Scheduling** : First Come, First Served. 가장 단순한 스케줄링 알고리즘으로, CPU를 먼저 요청한 프로세스가 먼저 CPU를 할당받으며 Non-preemptive
  > - **SJF Scheduling** : Shortest Job First. 가장 작은 '다음 CPU burst'를 가진 프로세스가 CPU를 할당받으며, Preemptive / Non-preemptive 모두 가능(Preemptive인 SJF Scheduling을 SRTF(Shortest Remaing Time First)라고 함)
  > - **RR Scheduling** : Round Robin. Time quantum(시간 할당량)을 가진 preemptive FCFS Scheduling으로, 한 프로세스가 한 번에 한 time quantum 만큼만 CPU를 사용하고 자발적으로 CPU release. Preemptive
  > - **Priority-based Scheduling** : 각 프로세스에 우선순위를 부여하고, 가장 높은 우선순위를 가진 프로세스에 CPU를 할당. Preemptive / Non-preemptive 모두 가능. Starvation Problem이 발생할 수 있고, 이를 Aging으로 해결
  > - **MLQ Scheduling** : Multi-Level Queue. 별도의 우선순위를 가진 여러 개의 큐를 두어, 각각의 큐 내에서 스케줄링(Intra-Queue Scheduling) and 큐들끼리의 스케줄링(Inter-Queue Scheduling)이 이뤄짐
  > - **MLFQ Scheduling** : Multi-Level Feedback Scheduling. MLQ에서 한 프로세스는 영구적으로 특정 큐에 할당되어 다른 큐로 이동하지 못하는 것과 달리, 프로세스가 큐들 사이를 이동할 수 있음. CPU burst의 성격에 따라 어느 큐에 들어갈지를 구분(I/O bound process에 가까울수록 높은 우선순위)

- Starvation이란?  
  > 계속해서 우선순위가 높은 프로세스가 새로 들어오면 우선순위가 낮은 프로세스는 CPU를 할당받지 못하고 무한으로 대기하는 문제

- Aging이란?  
  > 오랫동안 시스템에서 대기하는 프로세스들의 우선순위를 점진적으로 증가, 모든 프로세스는 언젠가 가장 높은 우선순위를 가지게 되므로, 무한 대기가 발생하지 않음 

- Preemptive Scheduling과 Non-preemptive Scheduling의 차이점?  
  > - **Preemptive** : 스케줄러가 CPU를 선점하고 있는 프로세스를 내보내고 다른 프로세스로 할당 가능, 복잡하지만 짧은 평균대기 시간을 보장한다는 
  > - **Non-preemptive** : 한번 프로세스가 CPU를 선점하면, 스스로 나올 때까지 종료/대기상태로 전환 불가, 단순하지만 평균대기 시간이 길어지는 단점


### ⚡️ Chapter 6. Process Synchronization

- 경쟁 상태(racing condition)란 무엇인가요?  
  > 여러 개의 프로세스가 동시에 동일한 자료에 접근하여 조작하고, 그 최종 연산 결과가 접근하는 순서에 따라 달라지게 되는 상황을 말한다. data inconsistency 문제가 발생할 수 있다.  
  > consistency 유지를 위해 협력 프로세스 간의 실행 순서를 정해주는 '동기화'가 필요하다.

- 임계영역 문제에 대한 해결책에는 어떤 것들이 있나요?  
  > - Peterson's Algorithm
  >   - cs 진입 의사 표시를 위한 변수 **flag**, 진입 가능 여부를 위한 변수 **turn**을 사용하여, flag와 turn을 검사하여 모두 true이면(다른 프로세스가 cs에 진입 중이면) 대기하고, 그렇지 않으면 진입하는 방식으로 동기화를 하는 알고리즘이다.
  >   - Busy Waiting(=spin lock)으로 인한 CPU cycle 낭비가 발생한다.
  >   - 컴파일러에 의해 entry section의 명령어 순서가 뒤바뀌면 mutex가 깨지는 문제가 발생한다. 
  > - 하드웨어 지원 동기화
  >   - Test & Modify를 atomic하게(사이에 끼어들 수 없는 하나의 instruction 단위 안에) 수행할 수 있도록 하는 명령어 **test_and_set(a)** 를 지원함으로써 간단하게 동기화할 수 있다.
  > - Semaphore
  >   - Integer 타입의 Synchronization variable S에 대해 atomic한 **P(S)** 연산 (cs 진입이 가능해질 때까지 대기하다가 S-- 후 진입하는 연산)과 **V(S)** 연산 (cs 완료 후 S++ 하는 연산)을 정의하여 동기화를 가능하게 하는 것
  >   - 0 이상의 정수값을 가질 수 있어, 초기값을 사용 가능한 자원의 개수로 초기화여 resource count의 용도로도 사용하는 Counting Semaphore / 0 or 1의 값만 가질 수 있는 Binary Semaphore(=Mutex)가 있다.
  >   - Busy-wait 방식과 Block & Wakeup 두 가지 방식으로 구현할 수 있다.
  > - Monitor
  >   - Monitor란 동시 수행 중인 프로세스 사이에서 abstract data type의 안전한 공유를 보장하기 위한 high-level synchronization construct이다. Monitor는 공유하는 변수와 그 변수를 조작할 수 있는 사용자 정의 opertaion(프로시저 or 함수)을 포함하며, Monitor 내의 operation은 원천적으로 동시에 여러 개가 실행될 수 없도록 설계되어 있어 **프로그래머가 따로 lock을 해줄 필요 없이** racing condition을 해결할 수 있다.

- 프로세스 혹은 스레드의 동기화란 무엇인가요? 
  > racing condition에서 발생할 수 있는 data inconsistency 방지를 위해 협력 프로세스 간의 실행 순서를 정해주는 것을 말한다. 

- thread-safe의 의미?  
  > 

- 락을 걸지 않고 경쟁상태를 해결할 수 있는 방법은 무엇인가요?
  > Monitor를 사용하는 것이다. Monitor란 동시 수행 중인 프로세스 사이에서 abstract data type의 안전한 공유를 보장하기 위한 high-level synchronization construct이다. Monitor는 공유하는 변수와 그 변수를 조작할 수 있는 사용자 정의 ppertaion(프로시저 or 함수)을 포함하며, Monitor 내의 operation은 원천적으로 동시에 여러 개가 실행될 수 없도록 설계되어 있어 프로그래머가 따로 lock을 해줄 필요 없이 racing condition을 해결할 수 있다.

- 교착상태란 무엇이며, 교착상태가 발생하기 위해서는 어떤 조건이 있어야 하나요?
  > 교착상태(Deadlock)란, 일련의 프로세스들이 서로가 가진 자원을 내어놓지 않고 상대방의 자원을 기다리며 block된 상태를 말한다. 
  > 교착상태가 발생하기 위해선 4가지 조건이 필요하다.
  >   1. Mutual Exclusion : 한 번에 하나의 프로세스만이 자원을 사용할 수 있는 것
  >   2. No preemption : 프로세스는 자원을 스스로 반납하며, 빼앗기지 않는 것
  >   3. Hold and Wait : 자원을 가진 프로세스가 다른 자원을 기다릴 때 보유한 자원을 내놓지 않고 계속 소유하는 것
  >   4. Circular Wait : 자원을 기다리는 프로세스들 간에 사이클이 형성되는 것 (P0 -> P1 -> ... -> Pn -> P0)
  
- 교착상태의 해결법은 무엇인가요?
  > 교착상태의 해결법은 크게 교착상태가 발생하지 않도록 방지하는 방법과 교착상태가 생기도록 놔두는 방법으로 나눌 수 있다.
  > - Deadlock을 미리 방지하는 방법
  >   - **Deadlock Prevention**
  >     - 자원할당 시 Deadlock 4가지 발생 조건 중 어느 하나가 만족되지 않도록 하는 것이다.
  >     - Mutual Exclusion에 대해서는 따로 방지하는 방법이 없다.  
  >     - No preemption에 대해서는 어떤 자원을 기다려야 하는 경우, 이미 보유한 자원을 빼앗기게 한다. 주로 State를 쉽게 save/restore 할 수 있는 CPU, Memory에 대해서 사용한다.
  >     - Hold and Wait에 대해서는 프로세스 시작 시 모든 필요한 자원을 미리 할당하거나, 자원이 필요할 경우 현재 보유한 자원을 모두 놓고 다시 요청하도록 한다.
  >     - Circular Wait에 대해서는 모든 자원 유형에 할당 순서를 정하고 정해진 순서대로만 자원을 할당하도록 한다.
  >   - **Deadlock Avoidance**
  >     - 자원 요청에 대한 부가 정보를 이용해서 deadlock으로부터 safe한 지를 동적으로 조사하여 safe할 때만 자원을 할당한다. 
  >     - Single instance per resource type인 경우, Claim edge(어떤 프로세스가 미래에 요청할 수 있는 자원을 가리키는 점선 화살표)가 추가된 자원할당 그래프를 통해 Claim edge를 포함하여 cycle의 존재여부를 검사하고, 없을 때만 자원을 할당한다.
  >     - Multiple instance per resource type인 경우, Banker's Algorithm을 사용한다.
   
  > - Deadlock이 생기도록 놔두는 방법
  >   - **Deadlock Detection and recovery**
  >     - Deadlock이 발생하도록 방치하지만, detection 루틴을 두어 Deadlock 발생 시 이를 recovery 한다.
  >     - Single instance per resource type일 때는 자원할당 그래프(or Wait-for 그래프)를 통해 cycle의 존재여부를 확인하여 cycle이 있으면 deadlock이라고 판단
  >     - Multiple instance per resource type일 때는 Banker's algorithm과 유사하지만, **"추가요청 가능 자원 <= 가용 자원"** 일 때가 아닌 **"현 시점 요청 자원 <= 가용 자원"** 일 때 자원을 할당하며, 이때 가용 자원의 갯수에는 현 시점에 요청이 없는 프로세스가 보유하고 있는 자원을 포함하여 산정한다.
  >   - **Deadlock Ignorance**
  >     - Deadlock은 매우 드물게 발생하기 때문에 이에 대한 조치 자체가 더 큰 overhead를 발생시킨다고 판단하여 아무런 조치를 취하지 않는 것이다. Deadlock이 발생했을 땐, 사람이 직접 알아챈 후 프로세스를 죽이는 방법으로 대처할 수 있다. 대부분의 범용 OS가 이 방법을 사용한다.

- Banker's algorithm 은 무엇입니까?
  > Deadlock 해결법 중 Deadlock avoidance에서 사용하는 알고리즘으로, resource type 당 여러 개의 instance가 있는 경우에 사용한다. 모든 프로세스가 자원의 최대 사용량을 미리 명시하고, 프로세스는 요청 자원을 모두 할당받은 후 유한 시간 내에 자원을 반납한다는 것을 가정으로 한다.
  > 기본 개념은 자원 요청 시 safe 상태를 유지할 때만 할당하는 것이다. 어떤 프로세스가 특정 자원을 요청했을 때, 해당 자원에 대한 해당 프로세스의 추가요청 가능 자원(해당 자원에 대한 최대 사용량 - 현재 보유량)이 현재 가용 자원 수보다 작거나 같을 때만 자원을 할당하고, 그렇지 않으면 할당하지 않음으로써 safe 상태를 유지하는 알고리즘이다.

- 교착상태와 starvation의 차이는?
  > 교착상태는 프로세스의 상태 중 block 상태일 때 발생하며, 절대 발생하지 않을 이벤트를 무한히 대기한다. 필요한 자원이 공유자원이다. 
  > Starvation은 프로세스의 ready 상태일 때 발생하며, 높은 우선순위를 가진 프로세스에 의해 원하는 자원을 계속 선점당하여 무한히 대기하는 것이다. 필요한 자원은 CPU 할당이다.
