### Lecture 14

Reinforcement Learning
> http://karpathy.github.io/2016/05/31/rl/

인공지능 발전을 위해 해결해야 할 문제
1. 연산량(무어의 법칙)
2. 데이터 (이미지넷처럼 잘 만들어진 데이터셋)
3. 알고리즘
4. 환경

AlexNet : 90년대의 Convnet의 규모를 키운 버전.
Deep Q Learning : 함수 근사로 convnet을 사용한 것을 제외하면 매우 일반적인 알고리즘.

알파고는 policy gradient, Monte Carlo Tree Search를 사용했는데, 이 또한 널리 알려진 방법.
최근에 소개된 각종 연구의 일등공신은 알고리즘이 아니라 연산/데이터/환경

#### Policy Gradient

현재 강화학습에서 가장 흔하게 쓰이는 기뻡. 
아타리를 데이터 관점에서 보면, 210 * 160 * 3 Array
이 데이터를 받고 막대기를 위로 올릴지 내릴지에 대한 판단 -> 나중에 피드백을 받게 된다.
만일 상대가 공을 받는데 실패했다면 +1, 내가 공을 못받았다면 -1
중요한 것은 실제로 퐁을 어떻게 플레이하느냐가 문제가 아니다. 

Policy Network
현재 게임의 상태가 어떤지를 입력받고 이를 토대로 우리가 어떤 행동을 취해야하는지 판단한다.
입력은 2101*160*3의 노드를 입력으로 받고 최종적으로 up이 될 확률이 출력된다. (Stochastic 정책)
예를 들어 70% 확률로 Up인 상황이라면, 7:3인 동전 튀겨서 사용

* Challange
수백번의 행동 중에 어떤 행동이 승리에 결정적인 요인이 되었는지를 어떻게 판단하는가?
수백만개의 가중치를 어떻게 바꿔야 하는가?
: Credit Assignment Problem

강화 학습과 지도학습은 꽤 비슷하다.
차이점 : 정확한 라벨 값을 모른다. : 특정 시점에서의 선택이 올바른 선택인지, 잘못된 선택인지 알 수가 없다. 

샘플링에 기반한 정책(Stochastic Policy)로 행동을 결정하고, 게임에 승리할 경우 같은 선택을 할 확률을 증가시키고
패배했을 경우 감소시킨다. 

-> 이 과정 조금 불완전하다
예를 들어 어떤 게임에서 프레임 50에서 맞는 판단을 내렸지만 150에서 잘못된 판단을 내려서 최종적으로 게임에서 패배했다면, 50의 판단마저 불완전한 피드백을 받게 된다. 

* Advantage Functions(보상 함수)
상식적으로 생각해보면, 모든 판단은 판단을 내린 직후에 가장 영향력이 크고, 시간이 지나면 점점 상관관계가 줄어든다. 
'망각'을 모델링한다. + 각 보상을 표준화 하는 것

* Policy Gradient 

Policy Network를 사용하면 미분 불가능한 연사을 포함한 인공 신경망을 사용할 수 있다. 

#### Markov Decision Process

꽤 오랜역사를 자랑하고 있지만 1990년대 이후부터 인공지능 영역에 사용되었다.
각 상태(state)에서 다른 상태로의 이동 시 발생하는 작업 행위를 액션(action)이라고 정의
어떤 상태에 있느냐에 따라 취할 수 있는 액션이 다를 수 있다.

특정 상태에서만 사용가능한 한정된 액션이 정의되어 있다.
마르코프 프로세스와의 차이점은 상태의 이동 제약 조건에 이전 상태 + 행해진 액션에 영향을 받는다.
이 액션을 취함으로써 얻어지는 보상을 정의 R(x, a)

Policy
Step Sequence에서 각각의 상태들과, 그 상태들에 매핑된 액션들의 집합.
-> 하나의 자료구조 덩어리

Deterministic Policy


#### Markov Process

상태의 이동 제약 조건에 이전 상태만 영향을 받는다.

#### Belman Equation

#### Q-Learning

Deep Q-Learning with Experience Replay

#### Q-network Architecture

#### Monte Carlo Sampling

#### Recurrent Attention Mmodel (RAM)

