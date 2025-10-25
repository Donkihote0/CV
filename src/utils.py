from pathlib import Path

def check_dataset_structure(root='data'):
    root = Path(root)
    expected = ['train/images', 'train/labels', 'valid/images', 'valid/labels']
    missing = []
    for p in expected:
        if not (root / p).exists():
            missing.append(str(root / p))
    return missing
