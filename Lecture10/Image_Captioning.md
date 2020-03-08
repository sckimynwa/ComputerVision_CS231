### Image Captioning with Semantic Attention

Image Captioning은 Computer Vision과 Natural Language Processing을 연결하는
매우 중요한 의의를 갖는 연구 분야.

#### Introduction

Image Captioning은 이미지를 보고 어떤 이미지인지 언어로 설명하는 작업

1. Top - down Approach
이미지를 통째로 시스템에 통과 시켜서 얻은 '요점'을 언어로 변환
현재 가장 많이 쓰이고 있는 접근 방식.
Recurrent Neural Network를 이용하여 각 파라미터들을 학습시킬 수 있다.

2. Bottom - Up Approach
이미지의 다양한 부분들로부터 단어를 도출해내고, 이를 결합하여 문장을 얻어낸다.


#### Visual Attention
이미지의 특정 부분에 집중하는 것. 컴퓨터는 이미지의 특히 중요한 부분에 집중하고, 
더 자세히 묘사하게 된다.

1. 이미지가 CNN을 통과하는 과정에서 생성된 Feature인 V를 얻으면서시작된다.
알고리즘도 이미지의 전체적인 특성을 확인한 후에, 구체적인 부분들을 관찰하게 된다.
이 전체적인 특징이 v이다.
이 특징은 pre-train된 네트워크를 사용하여 뽑아 낸다.

2. 이미지로부터 Bottom-Up 방식을 통해 얻어진 특징들의 집합으로, 
이미지에 등장하는 다양한 사물들이나 이벤트, 동작들을 Detector를 통해 검출해 낸다.
전체 이미지로부터 뽑은 부분적인 이미지들은 미리 준비된, 모든 단어들으 집합인 
y의 한 원소와 대응된다.

3. RNN을 이용해서 문장의 각 단어를 순서대로 출력하게 된다.
이미지의 각 부분에 대한 정보와, 어떤 문장이 진행중이었는지에 대한 정보.


