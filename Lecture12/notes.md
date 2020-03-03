### What's going on inside ConvNets?

First Conv Layer : Visualize Filters

e.g) AlexNet 11*11*3(channels) filters (64 filters) : 11*11*3*64
angles, opposing colors, oriented edges
* First Layer almost always the convolutional Layer.

Second Conv Layer : higher layer visualizing filters

We can visualize filters at higher layers, but not that interesting
connected to the output of the first layer
connected to the first layer, so we can recognize the activation pattern
but hard to explain.

Last Layer : Fully Connected Layer
e.g) AlexNet(4096 dimentional feature vector)

* Last Layer : Demensionality Reduction
visualize the space of FC7 feature vectors by reducing demensionality of vectors
from 4096 to 2 dimensions

Convnet has similar Semantic content 
find neighbor of feature space

use PCA algotirhm.(more complex t-SNE algorithm)

#### Occlusion Experiments

Occlusion: 폐쇄의 의미
input 이미지의 어떤 부분이 classification에 영향을 많이 미치는지 찾아보는 방법
cnn에 넣기 전에, 이미지의 일부를 마스크하고, 마스크 위치에서 확률의 히트맵을 그린다.

motivation: 이미지의 특정 부분을 block하면, network score가 극단적으로 변할 것이고, 
그러면 특정 부분은 classification decision에 매우 중요할 것

성능을 향상시키는것이 아니라 사람이 이해하기 쉽도록 하는 것에 그 목적

#### Saliency Maps : Segmentation without supervision

Saliency: 중요한
이미지 픽셀에 대해 class score의 gradient를 계산하고, 절대값을 취하기 + RGB채널을 최대로 취함
input에서 어떤 이미지가 classification에 중요한지 파악하는 방법
이미지 내의 객체를 추출할 수 있어서 좋으나 다루기 어렵다. 

#### Guided backpropagation

Gradient Ascent : generate a synthetic image that maximally activates a neuron

Guided backprop : find the part of an image that a neuron responds to

** check gradient ascent papers

일반적인 Backprop과는 다르게, Gradient를 시각화하는 과정에서 Positive Influence만 반영해서 관심있는 뉴런의 Gradient를 
선명하게 시각화 가능하다.

이미지의 어떤 부분이 최고로 영향을 미치는지 확인할 수 있는 방법

### Gradient Ascent

일부 input image에서 의존성을 제거한다.
Gradient Ascent를 실행해 이미지를 합성
weight고정하고 input image의 픽셀을 변경한다.

* '하늘' 이라는 초기 이미지를 주고 '새'의 속성을 갖도록 gradient ascent로 변형 -> deep dream의 원리


#### Fooling image / Adversarial Examples

1. start from an arbitrary image
2. pick an arbitrary class
3. modify the image to maximize the class
4. repeat until network is fooled


#### DeepDream

Amplify existing features
rather than synthesizing an image to maximize a specific neuron, 
instead try to amplify the neuron activation at some layer in the network

image와 layer를 선택한 후, 아래 작업을 반복
1. forward
2. 선택된 레이어에서 Activation 값과 같은 Gradient를 설정
3. Backward
4. Update Image

- Neural Network의 Feature를 시각화하고 이를 input이미지와 결합해 환각적인 이미지를 만들어내는 알고리즘


#### Feature Inversion

주어진 Feture vector와 일치한 이미지, 자연스러운 이미지와의 비교를 통해
네트워크가 깊어지면서 점점 Feature를 잃어버리는 것 확인


#### Neural Texture Synthesis

- deep dream
- texture : Artwork

* gram matrix check

#### Wrap up

Activations : Nearest neighbors, Dimensionality Reduction, maximal pathces, occlusion

Gradients : Saliency maps, class visualization, fooling images, feature inversion

Fun : Deepdream, style transfer


