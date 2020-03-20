### Style Transfer

general idea is to take two images, and produce a new image that reflects the content of one but the artistic "style" of the other.

#### Computing Loss

The Loss Function is a weghted sum of three terms: 
    
    content loss + style loss + total variation loss

We can then use this hybrid loss function to perform gradient descent not on the parameters of the model,
but instead on the pixel values of our original image.

1. Content Loss
: Content Loss measures how much the feature map of the generated iamge differs from the feature map of the source image. 