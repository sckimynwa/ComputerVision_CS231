## CNN

- Forward pass
1. 필터가 입력데이터를 슬라이딩하면서 feature 추출
2. feature를 Max pooling or Average pooling으로 압축해서 다음 레이어로 전송
3. 이 과정을 반복해서 labeling

- Cnn은 마지막 레이어에 Fully Connected Layer가 붙는 경우가 많다. 
- Fully Connected Layer의 backprop은 Neural network과 동일


