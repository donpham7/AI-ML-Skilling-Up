# CNN Notebooks

You will use MNIST to see what a convolutional neural network is doing.

## Learning goals

After this section, you should be able to explain:

- why CNNs preserve local structure better than flattened feedforward networks
- how convolution filters slide across an input
- how feature maps represent learned local patterns
- how pooling changes spatial resolution
- how Grad-CAM and misclassification views can help debug a model
- why CNN ideas transfer from images to 1D signals such as ECG windows

## Suggested order

1. `01_cnn_quickstart.ipynb` - train and evaluate a small CNN on MNIST.
2. `02_visualize_feature_maps.ipynb` - inspect activation maps from convolution layers.
3. `03_visualize_filters.ipynb` - inspect learned convolution filters.
4. `04_grad_cam.ipynb` - build a simple Grad-CAM heatmap for one prediction.
5. `05_misclassification_gallery.ipynb` - review incorrect predictions with confidence and heatmaps.

## Bridge to the heart project

The heart ECG project uses 1D signal windows instead of 2D images, but the same core idea applies:

```text
image CNN: small filters scan nearby pixels
ECG CNN:   small filters scan nearby time samples
```

You can reuse the CNN mental model when you design `HeartECGModel` in `../../sandbox/heart/runner.ipynb`.

Useful things for you to change:

- number of convolution layers
- number of channels
- kernel sizes
- pooling strategy
- dropout
- learning rate and epochs

Compare train and test curves, then inspect mistakes instead of relying on accuracy alone.

## Colab setup

From the repository root:

```python
!pip install -r requirements.txt
```

MNIST is downloaded to `data/`, which is ignored by git.
