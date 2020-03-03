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


#### Saliency Maps : Segmentation without supervision

#### Guided backpropagation

Gradient Ascent : generate a synthetic image that maximally activates a neuron

Guided backprop : find the part of an image that a neuron responds to

** check gradient ascent papers

#### Fooling image / Adversarial Examples

1. start from an arbitrary image
2. pick an arbitrary class
3. modify the image to maximize the class
4. repeat until network is fooled


#### DeepDream

Amplify existing features
rather than synthesizing an image to maximize a specific neuron, 
instead try to amplify the neuron activation at some layer in the network

#### Feature Inversion

#### Neural Texture Synthesis

- deep dream
- texture : Artwork

* gram matrix check

#### Wrap up

Activations : Nearest neighbors, Dimensionality Reduction, maximal pathces, occlusion

Gradients : Saliency maps, class visualization, fooling images, feature inversion

Fun : Deepdream, style transfer


