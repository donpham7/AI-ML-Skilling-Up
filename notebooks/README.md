# Notebooks

Your runnable Jupyter notebooks live here.

## Recommended path

Use these notebooks as a progression:

1. `feedforward/` - learn the PyTorch training loop and the basic experiment workflow.
2. `cnn/` - learn how convolutional models use local structure and how to inspect what they learned.
3. `../sandbox/heart/runner.ipynb` - apply the same workflow to an ECG project with TODO sections for you to fill in.

The common notebook rhythm is:

```text
imports and device
load data
preprocess data
build DataLoaders
define model
choose loss and optimizer
train
plot curves
evaluate
interpret mistakes
```

## Layout

- `feedforward/` - notebooks for dense neural networks, training loops, metrics, and loss landscapes.
- `cnn/` - notebooks for convolutional neural networks, feature maps, filters, Grad-CAM, and misclassifications.
- `rnn/` - notebooks for recurrent neural networks.
- `sklearn/` - notebooks for classical machine learning baselines.

## Setup

From the repository root:

```python
!pip install -r requirements.txt
```
