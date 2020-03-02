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





