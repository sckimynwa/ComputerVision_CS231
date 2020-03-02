### Faster R-CNN

R-CNN은 2개의 네트워크로 구성되어 있다. 
- Deep Convolution Network (Region Proposal Network (RPN))
- Fast R-CNN Detector 앞의 Proposed regions를 사용하여 Object Detection

2개의 모듈이 존재하지만, 전체적으로는 하나의 Object detection network.
* Faster R-CNN 이후부터 Fully Differentiable Model

#### Input Images

image는 height * width * depth를 가지고 있는 tensors (RGB Colored Image)

#### Base Network (Shared Network)

이전의 R-CNN에서는 Region Proposal을 하기 위해서 Selective Search를 사용. 
수천개 각각의 region proposals 마다 CNN(AlexNet)를 사용하여 forward pass
또한 3개의 모델을 각각 학습시켜야 했다. 

- Feature 뽑아내는 CNN
- classifier
- bounding box예측하는 regression model

Fast R-CNN에서는 중복되는 연산을 하나의 CNN으로 해결. 
이미지를 가장 먼저 받아서 feature추출 

모델은 기존의 모델을 주로 사용한다. (ResNet, VGG, Inception)등
이미 해당 Object를 학습해놓은 상태여야 한다. 

- 이미지를 받아서 CNN모델에 넣게 되면, 찾고자 하는 object의 feature map을 얻을 수 있다.

#### Region Proposal Networks (RPN)

input은 이전 base network에서 뽑아낸 특징맵을 사용한다. 
Feature map위에 n*n spatial window를 슬라이드 시킨다. 

각각의 윈도우가 찍은 지점마다 여러개의 region proposals를 예측하게 된다.
이후의 output 값은 1*1 kernel을 갖고 있는 2개의 convolution layer로 양분된다.

- Classification Layer (객체인지, 객체가 아닌지에 대한 확률값)
- Regression Layer (각 Anchor당 델타값들)


#### Region of Interest Pooling

ROI를 사용하게 되면 서로 다른 크기의 Feature maps들을 동일한 크기로 변환시켜줄 수 있다.

