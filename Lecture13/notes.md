#### Unsupervised Learning

Clustiering, PCA, Autoencoders -> Unsupervised Learning


#### Pixel RNN / Pixel CNN

AR: Auto Regressive Model
자기 자신을 입력으로 하여 자기 자신을 예측하는 모형을 AR이라 한다.

저해상도 이미지/영상을 고해상도로 변환하는 작업을 Super Resolution(SR)이라고 한다.
고해상도 이미지/영상을 픽셀 단위로 예측하는 경우, Xi를 예측할 때는 이전의 모든 픽셀 예측 결과를 활용하게 된다.

Pixel RNN
RNN(Recurrent Neural NetworK)는 시퀀스 데이터 처리에 특화된 아키텍쳐

Pixel CNN
CNN은 본래 시퀀스 데이터와는 직접 관련이 없으나, Masked Convolution Filter를 사용하면
AR Modeling이 가능하다. 


#### Autoencoders

데이터 생성이 목적이 아니다.
레이블되지 않은 학습 데이터들로부터 저차원의 feature representation을 학습하기 위한 비지도학습.

Autoencoder를 통해 x데이터는 z특징으로 매핑된다. 
z는 x보다 작으므로 Autoencoder를 통해 차원 축소의 효과를 기대할 수 있다.

인코더가 학습한 특징 매핑을 지도학습 모델의 초기값으로 사용할 수 있다.
그 이후 추가적인 분류기를 붙인다.

이 Autoencoder는 레이블링되지 않은 많은 데이터들로부터 양질의 general feature representation을 학습할 수 있다ㅏ.
AE는 입력을 복원하는 과정에서 특징을 잘 학습했고, 학습된 특징은 지도학습 모델의 초기화에 이용할 수 있었다.

#### Variational autoencoder

VAE는 Generative Model의 하나로, 확률분포를 학습함으로써 데이터를 생성하는 것이 목적이다.

1. Encoder Network
학습용 데이터(x)를 받고 잠재 변수(z)의 확률분포에 대한 파라미터를 출력한다.
인코더의 역할은 데이터가 주어졌을 때 Deocder가 원래의 데이터로 잘 복원할 수 있는 z를 샘플링할 수 있는
이상적인 확률분포 (p(z|x))를 찾는 것이다. 하지만 어떤 것이 이상적인 확률분포인지는 아무도 모른다.
이를 위해 Variational Inference를 사용한다.

- Variational Inference
우리가 이상적인 확률분포를 모르지만, 이를 추정하기 위해서 다루기 쉬운 분포(가우시안 분포 등)를 가정하고, 이 확률분포의 모수를 바꿔가며, 이상적인 확률분포에 근사하게 만들어, 그것을 사용하는 것. 

2. Decoder Network
잠재변수에 대한 확률분포(p(z))에서 샘플링한 벡터를 입력받아 원본 이미지를 복원한다.

우리가 궁극적으로 알고 싶은 것은 p(x), 즉 실제 데이터의 분포이다. 

#### GAN

GAN: Generative Adversarial Network
1. Generative : 생성 모델이라는 것을 의미. 생성 모델이란, 그럴듯한 가짜를 만들어내는 모델이다.
진짜 같은 가짜 사람 얼굴 사진을 만들어내거나 실제로 있을 법한 고양이 사진을 만들어내는 등.
그럴듯하다 : 수학적으로는 실제 데이터의 분포와 비슷한 분포에서 나온 데이터를 실제와 비슷하다고 말할 수 있따.
예를 들어 그럴 듯한 키와 몸무게 조합을 만들어 내려면 실제 키와 몸무게의 분포를 최대한 비슷하게 따라가야 한다.
얼굴 이미지의 생성 모델을 만들겠다는 것은 사람 얼굴처럼 보이는 픽셀값 조합의 분포를 찾아내겠다는 것.

2. Adversarial
두 개의 모델을 적대적으로(Adversarial)하게 경쟁시키며 발전시킨다는 것을 뜻한다.
Generator vs Discriminator를 경쟁적으로 학습시킴으로써 발전한다. 

생성자의 목적은 그럴듯한 가짜 데이터를 만들어서 구분자를 속이는 것
구분자의 목적은 생성자가 만든 가짜 데이터와 진짜 데이터를 구분하는 것이다.
이 둘을 함께 학습시키면서 진짜와 구분할 수 없는 가짜를 만들어내는 생성자를 얻을 수 있따.
GAN의 핵심적인 아이디어인 Adversarial Training방식이다.

3. Network
이 모델이 인공신경망 또는 딥러닝을 만들어졌기 때문에 Network라는 이름이 붙는다.
딥러닝은 강력한 머신러닝 모델을 가능하게 만드는 기술이다. 

> non-linear activation function
> Hierarchy structure
> Backpropagation

답러닝은 이론적으로 어떤 함수도 근사할 수 있는 함수이다. GAN은 실제 데이터 분포를 근사하는 함수를 만들기 위해서
이러한 딥러닝 구조를 활용한다.
