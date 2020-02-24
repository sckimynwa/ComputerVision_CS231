### Motivation

Batch Normalization은 기본적으로 Gradient Vanishing, Gradient Exploding이 일어나지 않도록 하는 아이디어 중의 하나.
> 기존에는 Activation 함수의 변화 (ReLU 등)으로 해결 시도
Traning 과정 자체를 전체적으로 안정화하여 학습 속도를 가속시킬 수 있는 근본적인 방법이 없을까?

- Internal Covariance Shift
네트워크의 각 층이나 Activation마다 입력값의 분산이 달라진다. 
각 층의 input distribution을 정규화하는 방법 생각.

### Algorithm

- mini-batch 단위로 데이터를 가져와서 학습시키고, 각 feature 별로 평균과 표준편차 구한다음 정규화한다.

- 실제로 네트워크에 적용시킬 때에는 특정 Hidden Layer에 들어가기 전에 Batch Normalization Layer를 더해준 후에 
새로운 값을 Activation 함수에 넣어준다.

- 활성화함수의 활성화값 또는 출력값을 정규화하는 작업을 의미한다.
- 신경망의 각 레이어에서 데이터의 분포를 정규화하는 작업. 
- 일종의 노이즈를 추가하는 방법으로, 이는 배치마다 정규화를 함으로써 전체 데이터에 대한 평균의 분산과 값이 달라질 수 있다. 
- 학습을 할 때마다 홠성화값, 출력값을 정규화하기 때문에 초기화 문제에서 비교적 자유로워진다.

핵심은 각각의 hidden layer마다 값을 정규화하여 과적합 문제를 해결하는 것.
학습시의 미니배치를 한 단위로 정규화를 하는 것으로 분포의 평균이 0, 분산이 1이 되도록 정규화 하는 것을 의미한다. 


