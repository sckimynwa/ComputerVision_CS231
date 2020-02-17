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
- 16 * 10 * 10 feature map

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
