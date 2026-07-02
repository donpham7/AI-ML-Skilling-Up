# AI-ML-Skilling-Up

Course notes and exercises for learning machine learning with scikit-learn and PyTorch.

You will run this repository locally with VS Code, Python, and Jupyter notebooks.

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
│   ├── cifar10/
│   │   └── runner.ipynb
│   └── heart/
│       ├── runner.ipynb
│       └── setup.py
├── requirements.txt
└── README.md
```

## Start here

This setup guide assumes you are new to Python projects. Follow the steps in order.

### 1. Install the tools

Install these first:

- VS Code: <https://code.visualstudio.com>
- Python 3: <https://www.python.org/downloads>
- Git: <https://git-scm.com/downloads>

When installing Python, make sure Python is added to your PATH if the installer gives you that option.

### 2. Install VS Code extensions

Open VS Code, go to Extensions, and install:

- Python
- Jupyter

These extensions let VS Code run `.ipynb` notebook files.

### 3. Open a terminal

Use the terminal for copy-paste commands.

- On macOS, open Terminal.
- On Windows, open PowerShell.

You can also open a terminal inside VS Code:

```text
Terminal -> New Terminal
```

### 4. Check that Python and Git work

On macOS, copy and paste:

```bash
python3 --version
git --version
```

On Windows PowerShell, copy and paste:

```powershell
python --version
git --version
```

If either command says it cannot be found, restart your terminal. If it still does not work, reinstall that tool and make sure it is added to PATH.

### 5. Download this repository

Choose a folder where you want your class projects to live, then run:

```bash
git clone https://github.com/donpham7/AI-ML-Skilling-Up.git
cd AI-ML-Skilling-Up
```

### 6. Pull the latest updates

After you have already downloaded the repository once, you do not need to clone it again. To get the newest notebooks and instructions, open a terminal inside the `AI-ML-Skilling-Up` folder and run:

```bash
git pull
```

Run `git pull` before each class or whenever you are told the course files changed.

### 7. Create a Python environment

On macOS or Linux, copy and paste:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Windows PowerShell, copy and paste:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell says scripts are disabled, run this once and try activating again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

After activation, your terminal prompt should show `.venv` somewhere. That means your project environment is active.

### 8. Open the project in VS Code

From inside the `AI-ML-Skilling-Up` folder, copy and paste:

```bash
code .
```

If `code .` does not work, open VS Code manually and choose:

```text
File -> Open Folder -> AI-ML-Skilling-Up
```

### 9. Select the notebook kernel

Start with:

```text
notebooks/feedforward/01_mnist_feedforward_quickstart.ipynb
```

When VS Code asks for a Python kernel, choose the `.venv` environment you created.

If VS Code does not ask automatically:

1. Open the notebook.
2. Click the kernel name in the top right.
3. Choose the `.venv` Python environment.
4. Run the first cell.

### 10. Test one notebook

Open this notebook:

```text
notebooks/feedforward/01_mnist_feedforward_quickstart.ipynb
```

Run the first few cells. If they run without errors, your setup is working. After that, follow the notebook and project READMEs for what to do next.

### Common setup problems

If `pip install -r requirements.txt` fails, make sure your virtual environment is active and try:

```bash
python -m pip install -r requirements.txt
```

If VS Code cannot find your environment, close and reopen VS Code from the project folder.

If a notebook says a package is missing, run this in the terminal from the repository root:

```bash
pip install -r requirements.txt
```

## Notebooks

- `notebooks/feedforward/` - runnable MNIST notebooks for dense neural networks and the foundations of training.
- `notebooks/cnn/` - runnable CNN notebooks for convolutional models and visual interpretation.
- `notebooks/rnn/` - runnable RNN notebooks.
- `notebooks/sklearn/` - classical machine learning baselines.

## Sandbox

Use `sandbox/` for scratch notebooks, experiments, temporary datasets, and local project work. The CIFAR-10 and heart ECG projects live here as guided project starters.

Most contents of `sandbox/` are ignored by git. Project starter files such as `sandbox/**/setup.py` and `sandbox/**/runner.ipynb` may be tracked.

## Git hygiene

Generated datasets, model checkpoints, and outputs are ignored by default:

- `data/`
- `datasets/`
- `models/`
- `checkpoints/`
- `outputs/`
- `*.pt`, `*.pth`, `*.ckpt`
