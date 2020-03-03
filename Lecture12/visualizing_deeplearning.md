### Visualizing for CNN

딥러닝의 약점 중 하나는 학습이 왜 성공적인지, 혹은 왜 실패했는지를 해석하기가 힘들다
데이터도 많고, 파라미터도 많고 복잡하며, 각각의 Layer들이 도대체 무엇을 하고 있는지
알기가 쉽지 않아 답답하다.

Visualize를 통해 이를 극복하려는 여러 시도들이 있다. 
비단 딥러닝 뿐 아니라, Data Science에서도 이러한 시각화를 많이 이용한다.
고차원 데이터를 선형압축해 보여주는 PCA, t_SNE등등

또한 레이어를 거치면서 인풋이 학습되어 가는 과정을 reference하거나, 
학습된 결과를 통해 input을 역추적함으로써 확인이 가능하다.

1. Layer Activations

2. Conv/FC filters

3. Retrieving Images that maximally activate a neuron