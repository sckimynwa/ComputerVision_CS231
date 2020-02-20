## Activation Function

활성화 함수를 사용하는 이유 :
DATA를 비선형으로 바꾸기 위해서이다.
선형시스템은 Deep Learning Model에 적용하게 되면, 망이 깊어지지 않는다.
선형시스템을 여러 겹으로 쌓아도, 그 결과는 그저 한 겹의 은닉층으로 구현이 가능하기 때문이다.


## RNN (Recurrent Neural Network)

일반적인 신경망은 (FFNets) : Feed-forward neural networks
데이터를 트레이닝 셋과 테스트 셋으로 나누어서 관리한다. 트레이닝 셋을 통해서 신경망의 가중치 학습

- 입력 데이터는 모든 노드를 단 한번씩만 지나간다. (데이터의 순서가 중요하지 않음)
- 데이터들의 시간적인 순서를 무시하고, 현재 주어진 데이터들만을 가지고 조합해서 학습

RNN은 Hidden layer의 결과가 다시 같은 Hidden layer의 input으로 들어가도록 연결되어 있다. 
따라서 순서, 시간적인 측면을 고려한 학습이 가능하다.

- 순서적인 측면을 고려해서 데이터를 판단할 수 있으므로, 문장 등의 데이터를 처리하는데에 유용하다

Long Term Dependency Problem

- 제공된 데이터와 참조해야 할 데이터 사이의 차이 (GAP)이 크다면, 성능저하가 온다.
- 이를 개선하기 위해서 LSTM이 등장.

## LSTM

- 상호작용하는 4개의 레이어가 존재한다. (기존의 RNN은 싱글 레이어 구조)
- 이 구조가 반복되어 나타나는 것이 LSTM
- 상호작용구조가, 문맥간의 GAP에 대한 오차를 줄이는데에 도움을 준다.

### Cell State

- 핵심 구조, 하나의 컨베이어 벨트처럼 전체 체인을 통과한다. 
- LSTM은 cell state에 게이트를 활용해서 정보를 더하거나 제거한다. 
- 게이트들은 Sigmoid neural network layer와 연결되어 있어서 선택적으로 정보를 취합할 수 있다.

cell state를 보호하기 위해서 3개의 게이트가 이용된다.

- forget gate layer
> 0, 1사이의 값을 갖는 h(t-1), x(t)를 입력으로 받는다.
> 이를 sigmoid 연산을 통해 0, 1의 결과를 만들고 이 값을 넘길지 말지를 결정한다.

- input gate layer
> 어떤 값을 우리가 update할지를 결정한다. 

- tanh layer
> cell state에 더해질 수 있는 새로운 후보 값



