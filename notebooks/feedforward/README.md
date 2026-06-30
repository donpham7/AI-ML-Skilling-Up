# Feedforward Notebooks

These notebooks use MNIST to introduce dense neural networks before moving into CNNs.

## Suggested order

1. `01_mnist_feedforward_quickstart.ipynb` - train a baseline dense network on MNIST.
2. `02_training_curves.ipynb` - visualize loss and accuracy over epochs.
3. `03_weights_and_activations.ipynb` - inspect learned weights, hidden activations, and prediction confidence.
4. `04_loss_landscape.ipynb` - plot a 2D slice of the loss surface around trained weights.
5. `05_3d_loss_landscape.ipynb` - render the same kind of loss slice as a 3D surface.

## Colab setup

From the repository root:

```python
!pip install -r requirements.txt
```

MNIST is downloaded to `data/`, which is ignored by git.
