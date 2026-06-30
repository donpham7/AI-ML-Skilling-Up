# Sandbox

Use this folder for local experiments, scratch notebooks, temporary datasets, and one-off project ideas.

Most files inside `sandbox/` are ignored by git so you can experiment freely without committing accidental work.

Tracked project starter files are allowed:

- `sandbox/**/setup.py`
- `sandbox/**/runner.ipynb`

Dataset files under `sandbox/**/data/` are ignored.

## Heart ECG Project

The heart project uses the MIT-BIH Arrhythmia ECG dataset from PhysioNet.

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
- train/test dataloaders
- TODO sections for model, loss function, and optimizer
- training curves and evaluation metrics

### 4. What you should edit

You should focus on:

- `preprocess_record(record)`
- `HeartECGModel`
- `loss_fn`
- `optimizer`
- training settings such as epochs, batch size, and learning rate

### 5. Git behavior

The dataset is intentionally ignored:

```text
sandbox/heart/data/
```

You can rerun `python setup.py` to recreate it after cloning the repo.
