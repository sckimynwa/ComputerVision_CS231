### Semantic Segmentation

컴퓨터 비전 분야에서 가장 핵심적인 분야중의 하나
단순이 사진을 보고 분류하는 것에 그치지 않고, 그 장면을 완벽하게 이해해야 하는 높은 수준의 문제
자율주행에서부터, 해상에서 선박찾기 등
Deep Convolution Neural Network를 적용해서 발전.

사진을 찍을 때 인물을 찾아내서 인물을 제외한 배경을 흐릿하게 만드는 예제

* Computer vision Problems

- Classification : 인풋에 대해서 하나의 레이블을 예측하는 작업
> Alexnet, ResNet, Xception 등의 모델

- Localization/Detection : 물체의 레이블을 예측하면서 그 물체가 어디에 있는지 정보제공
> YOLO, R-CNN등의 모델(물체가 있는 곳에 네모를 그리는 등)

- Segmentation : 모든 픽셀의 레이블을 예측
> FCN, SegNet, DeepLab등의 모델

Semantic Image Segmentation의 목적 : 사진에 있는 모든 픽셀을 해당하는 class로 분류하는 것.
이미지에 있는 모든 픽셀에 대한 예측을 하는것으로, dense prediction이라고도 불린다.

* Semantic Image Segmentation은 같은 클래스의 객체를 구분하지 않는다. 
(COCO Detection Challenge, PASCAL VOC Challenge)

#### Task

Input : RGB Color Image or Grayscale Image
Ouput : Segmentation Map

One-Hot encoding으로 각 클래스에 대해 출력채널을 만들어서 segmentation map을 만든다. 
클래스의 개수만큼 만들어진 채널을 argmax를 통해서 하나의 출력물로 내어놓음.

* Alexnet, Resnet등 분류에 자주 쓰이는 신경망들은 Parameter의 개수와 차원을 줄이는 layer들을 가지고 있어서
자세한 위치정보를 잃게 된다. 그리고, 마지막에 쓰이는 Fully Connected Layer에서 위치에 대한 정보를 잃는다.

* 공간, 위치에 대한 정보를 잃지 않기 위해서는 Pooling & Fully Connected Layer를 없애고, 
stride = 1, padding 일정한 Convolution을 진행해야 하지만, 이는 메모리 특성상 현실적으로 불가능, 
따라서 Downsampling & Upsampling 의 형태를 띈다.


#### Downsampling

> 주 목적은 차원을 줄여서 적은 메모리로 Deep Learning
> 보통 stride 2이상인 Convolution 사용하거나, Pooling 사용 -> 어쩔 수 없이 특젙 feature의 정보 손실
> 마지막에 Fully Connected Network 사용

#### Upsampling

> 차원을 늘려서 인풋과 같은 차원으로 만들어주는 과정
> Strided Transpose Convolution을 주로 사용

### Classification & Localization

기본적으로 image classificatino과 비슷한 구조이지만, 하나의 Fully Connected Layer가 더 있다. 
Box Coordinate를 위한 Layer

하나의 레이어는 score를 반환, 하나는 Bounding Box의 좌표를 반환한다. 
2개의 loss가 존재하고, 이것은 완전히 지도학습이기 때문에, 학습 이미지는 label과 box coordinate를 둘다 가지고 있어야 한다. 

이 2개의 Loss를 함친 것을 Multi-task loss라고 부르며, 이 것의 Gradient를 구하려면 네트워크 가중치들의 각각의 미분 값을 구해야 한다.

* Regression Loss란
Cross entropy, softmax가 아닌 Loss를 뜻한다. 연속적인 Loss를 의미함.
고정된 개수의 카테고리가 있고, 이걸 가지고 Class Score를 예측하게 되면, cross entropy/svm loss 등을 사용할 수 있지만, 
출력이 연속적인 값이라면, (e.g 관절의 위치) 이는 연속적인 값이기 때문에 다른 loss를 사용해야 한다. 


### Object Detection

Localization은 이미지가 하나라고 가정, 하지만 Object Detection은 이미지가 몇 개인지 예측을 할 수 없다. 
regression을 이용해서 풀기에는 상당히 까다로움

1. Sliding Window
> 특정 크기를 가진 window를 계속해서 이동 카테코리 학습
> 하지만 어떻게 영역을 추측해야 하는지도 명확하지 않고, 크기가 얼마나 되는지도 알 수가 없다.

2. Region Proposal
> 딥러닝을 사용하지 않는다. 
> 객체가 있을법한 후보를 찾아내는 것. 1000개의 region을 selective search를 통해 찾아낸다. 
> '뭉친' 곳들을 찾아내는 방식. 따라서 이미지에 객체가 존재한다면, Selective Search 의 region 안에 있을 가능성이 높다. 
> region proposal을 CNN의 입력으로 해서 추출한다.

