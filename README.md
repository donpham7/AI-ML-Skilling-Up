# AI-ML-Skilling-Up

Course notes and exercises for learning machine learning with scikit-learn and PyTorch.

You can use this repository in Google Colab or run it locally with `pip`.

## Learning sequence

Follow this path:

1. `notebooks/feedforward/` - learn the training loop, loss functions, optimizers, train/test splits, metrics, and overfitting.
2. `notebooks/cnn/` - learn why neural network structure matters, using convolutions, feature maps, filters, Grad-CAM, and misclassification analysis.
3. `sandbox/heart/runner.ipynb` - apply the same workflow to a messier ECG project where preprocessing, class imbalance, and honest evaluation matter.

The heart project is a capstone-style playground after you have worked through the feedforward and CNN notebooks. You should recognize the same rhythm: load data, preprocess, create batches, define a model, choose a loss and optimizer, train, plot curves, evaluate, and explain errors.

## Repository structure

```text
.
├── notebooks/
│   ├── feedforward/
│   │   ├── 01_mnist_feedforward_quickstart.ipynb
│   │   ├── 02_training_curves.ipynb
│   │   ├── 03_weights_and_activations.ipynb
│   │   ├── 04_loss_landscape.ipynb
│   │   └── 05_3d_loss_landscape.ipynb
│   ├── cnn/
│   ├── rnn/
│   └── sklearn/
│       └── 01_sklearn_quickstart.ipynb
├── sandbox/
│   ├── README.md
│   └── heart/
│       ├── runner.ipynb
│       └── setup.py
├── requirements.txt
└── README.md
```

## Setup

### Google Colab

1. Open a notebook from `notebooks/` in Google Colab.
2. If a package is missing, run this from the repository root:

```python
!pip install -r requirements.txt
```

If the notebook is opened directly from GitHub, Colab may place the notebook outside the repository root. In that case, clone the repo first:

```python
!git clone https://github.com/YOUR_USERNAME/AI-ML-Skilling-Up.git
%cd AI-ML-Skilling-Up
!pip install -r requirements.txt
```

### Local Python

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter notebook
```

## Notebooks

- `notebooks/feedforward/` - runnable MNIST notebooks for dense neural networks and the foundations of training.
- `notebooks/cnn/` - runnable CNN notebooks for convolutional models and visual interpretation.
- `notebooks/rnn/` - runnable RNN notebooks.
- `notebooks/sklearn/` - classical machine learning baselines.

## Sandbox

Use `sandbox/` for scratch notebooks, experiments, temporary datasets, and local project work. The heart ECG project lives here as your guided project starter.

Most contents of `sandbox/` are ignored by git. Project starter files such as `sandbox/**/setup.py` and `sandbox/**/runner.ipynb` may be tracked.

## Git hygiene

Generated datasets, model checkpoints, and outputs are ignored by default:

- `data/`
- `datasets/`
- `models/`
- `checkpoints/`
- `outputs/`
- `*.pt`, `*.pth`, `*.ckpt`
