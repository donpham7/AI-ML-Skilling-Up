# Sandbox

Use this folder for local experiments, scratch notebooks, temporary datasets, and one-off project ideas.

Most files inside `sandbox/` are ignored by git so you can experiment freely without committing accidental work.

Tracked project starter files are allowed:

- `sandbox/**/setup.py`
- `sandbox/**/runner.ipynb`

Dataset files under `sandbox/**/data/` are ignored.

## Heart ECG Project

The heart project uses the MIT-BIH Arrhythmia ECG dataset from PhysioNet.

This project is meant to come after the feedforward and CNN notebooks. It gives you a more realistic signal-classification problem where the familiar training workflow still applies, but the choices are less automatic.

Use it to practice:

- choosing preprocessing for noisy real-world signals
- designing a model for `(batch, channels, samples)` ECG windows
- choosing a loss function and optimizer
- reading train/test curves
- interpreting accuracy, balanced accuracy, precision, recall, F1, and the confusion matrix
- noticing class imbalance and possible data leakage

### 1. Install dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

If you are using the course conda environment:

```bash
conda activate ai-ml-skilling-up
pip install -r requirements.txt
```

### 2. Download the dataset

From the heart sandbox folder:

```bash
cd sandbox/heart
python setup.py
```

This downloads and extracts the dataset into:

```text
sandbox/heart/data/
```

The download can take a minute or two depending on PhysioNet.

### 3. Open the runner notebook

Open:

```text
sandbox/heart/runner.ipynb
```

The notebook provides:

- device setup
- dataset discovery
- ECG record loading
- an empty preprocessing function for you to fill in
- ECG window creation
- inter-patient train/test dataloaders
- TODO sections for model, loss function, and optimizer
- training curves and evaluation metrics

### 4. What you should edit

Focus on:

- `preprocess_record(record)`
- `HeartECGModel`
- `loss_fn`
- `optimizer`
- training settings such as epochs, batch size, and learning rate

### 5. Suggested workflow

Change one thing at a time:

1. Start with a simple preprocessing choice, such as selecting one lead and normalizing each record.
2. Build a small model that produces two logits: `normal` and `abnormal`.
3. Choose `nn.CrossEntropyLoss()` and an optimizer such as Adam.
4. Train for a few epochs.
5. Compare train and test curves.
6. Read the confusion matrix and class-level precision/recall.
7. Decide what to try next.

Good experiments include:

- changing the preprocessing
- trying a feedforward model versus a 1D CNN
- changing the number of convolution channels
- using class-weighted loss
- changing learning rate or epochs

The goal is not only to get a high score. The goal is to explain why the score changed.

### 6. Git behavior

The dataset is intentionally ignored:

```text
sandbox/heart/data/
```

You can rerun `python setup.py` to recreate it after cloning the repo.
