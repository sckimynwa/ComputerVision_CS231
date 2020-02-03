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

