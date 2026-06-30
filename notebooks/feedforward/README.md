# Feedforward Notebooks

You will use MNIST to learn dense neural networks before moving into CNNs.

## Learning goals

After this section, you should be able to explain:

- what a model, loss function, optimizer, batch, and epoch are
- how the PyTorch training loop updates model parameters
- why train/test splits matter
- how to read loss and accuracy curves
- what overfitting looks like
- how hidden activations and confidence relate to model behavior

## Suggested order

1. `01_mnist_feedforward_quickstart.ipynb` - train a baseline dense network on MNIST.
2. `02_training_curves.ipynb` - visualize loss and accuracy over epochs.
3. `03_weights_and_activations.ipynb` - inspect learned weights, hidden activations, and prediction confidence.
4. `04_loss_landscape.ipynb` - plot a 2D slice of the loss surface around trained weights.
5. `05_3d_loss_landscape.ipynb` - render the same kind of loss slice as a 3D surface.

## Training loop pattern

Pay attention to the repeated training pattern you will reuse later:

```python
logits = model(batch_X)
loss = loss_fn(logits, batch_y)

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

Useful things for you to change:

- hidden layer sizes
- activation functions
- learning rate
- optimizer
- batch size
- number of epochs

After this section, you should be comfortable navigating notebooks that load data, define a model, train it, and evaluate it.

## Colab setup

From the repository root:

```python
!pip install -r requirements.txt
```

MNIST is downloaded to `data/`, which is ignored by git.
