## LeNet

- CNN 알고리즘의 이름
- "Gradient-based learning applied to document recognition"

- input, 3 Convolution layer (C1, C3, C5), 2 Subsampling layer(S2, S4), output layer
- activation function = tanh

1. C1 Layer
-  input image(32*32*3)
- 6 5*5 Convolutional filter
- results in 28 * 28 * 6 feature maps

2. S2 Layer
- stride 2 subsampling
- results in 14 * 14 * 6 feature maps
- using average pooling method
- after average, multiply parameter(one value) + bias (controls sigmoid functions' inactivity)

3. C3 Layer
- 3 5*5 Convolutional filter - 6 10 * 10 feature map
- 4 5*5 Convolutional filter - 6 10 * 10 feature map
- ...
- 16 * 10 * 10 featur e map

4. S4 Layer
- subsampling 
- results in 5 * 5 * 16 feature maps

5. C5 Layer
- 120 * ( 5 * 5 * 16 ) filter convolutional calcaulation
- 120 * 1 * 1 feature map

6. F6 Layer
- 84 unit feed forward network

7. Output Layer
- 10 RBF unit, result the class

## Alexnet

- similar to LeNet
- parallel structure using 2 GPU
- consists of 8 layers
    - 5 convolutional layer
    - 3 fully - connected layer

- 2, 4, 5 convolutional layer : connected to the same channel feature map
- 3 convolutional layer : connected to the all 2 feature map (channel)

- using ReLU as an activation function (better than tanh function)
- using dropout (but using all neurons in test) - prevent overfitting
- using max pooling & overlapping pooling
- local response normalization(LRN) : 활성화된 뉴런이 주변 이웃 뉴런들을 억누르는 현상
- 강하게 활성화된 뉴런의 주변 이웃들에 대해서 normalization
- data augmentation

## Resnet

- Using Residual Block to solve Vanishing Gradients


## Googlenet

- Network in Network (NIN)
- 일반적은 CNN 은 필터가 움직이면서 해당하는 입력 부분과 곱/합 연산을 수행, 활성화 함수를 거쳐서 결과를 만들어냄
- 데이터의 분포가 비선형적인 관계라면, -> MLP(Multi Layer Perceptron)을 중간에 넣어버림.
- 일반적인 CNN구조
    - Feature Extraction ( Conv + pooling layer )
    - Classifier ( Fully Connected Layer )
- Conv Layer가 Local receptive field 에서 feature 추출해내는 능력은 우수하지만, filter의 특징이 Linear하다는 한계
- 1*1 conv layer + MLP (Multi Layer Perceptron)

- non lenear 한 성질을 잘 활용할 수 있음
- 1 * 1 convolution을 통해서 Feature-map을 줄일 수 있음


- 마지막에 Fully-Connected Layer를 넣는 대신에 Global Average Pooling을 넣는다. (Overfitting 방지)
- Features

    1. 네트워크의 얕은 부분, 입력과 가까운 부분에는 Inception 모듈을 사용하지 않는다.
    2. Auxiliary Classifier : Loss를 중간중간 구하여 Gradient 적절하게 역전파. (0.3 곱해서 영향력 조절)
        - 테스트시에는 Auxiliary Classifier 제거
    3. Inception Module
        - 각 필터의 결과를 합쳐서(Concat) 표현하는 것
        - 연산량을 줄이기 위해서 1 * 1 Conv를 적극적으로 사용함.
