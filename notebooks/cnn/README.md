# CNN Notebooks

These notebooks use MNIST to help students see what a convolutional neural network is doing.

## Suggested order

1. `01_cnn_quickstart.ipynb` - train and evaluate a small CNN on MNIST.
2. `02_visualize_feature_maps.ipynb` - inspect activation maps from convolution layers.
3. `03_visualize_filters.ipynb` - inspect learned convolution filters.
4. `04_grad_cam.ipynb` - build a simple Grad-CAM heatmap for one prediction.
5. `05_misclassification_gallery.ipynb` - review incorrect predictions with confidence and heatmaps.

## Colab setup

From the repository root:

```python
!pip install -r requirements.txt
```

MNIST is downloaded to `data/`, which is ignored by git.
