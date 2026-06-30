# AI-ML-Skilling-Up

Course notes and exercises for learning machine learning with scikit-learn and PyTorch.

This repository is designed to work well in Google Colab while still being easy to run locally with `pip`.

## Repository structure

```text
.
├── modules/
│   ├── feedforward/
│   ├── cnn/
│   └── rnn/
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
│   └── README.md
├── requirements.txt
└── README.md
```

## Student setup

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

## Modules

- `modules/feedforward/` - dense neural networks, MNIST baselines, training curves, and loss landscape slices.
- `modules/cnn/` - convolutional neural networks for image and spatial data.
- `modules/rnn/` - recurrent neural networks for sequence data.

## Notebooks

- `notebooks/feedforward/` - runnable MNIST feedforward neural network notebooks.
- `notebooks/cnn/` - runnable CNN notebooks.
- `notebooks/rnn/` - runnable RNN notebooks.
- `notebooks/sklearn/` - classical machine learning baselines.

## Sandbox

Use `sandbox/` for scratch notebooks, experiments, temporary datasets, and local project work.

The contents of `sandbox/` are ignored by git, except for `sandbox/README.md`.

## Git hygiene

Generated datasets, model checkpoints, and outputs are ignored by default:

- `data/`
- `datasets/`
- `models/`
- `checkpoints/`
- `outputs/`
- `*.pt`, `*.pth`, `*.ckpt`
