from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path
from urllib.request import urlopen


DATASET_URL = (
    "https://physionet.org/static/published-projects/mitdb/"
    "mit-bih-arrhythmia-database-1.0.0.zip"
)
DATA_DIR = Path(__file__).resolve().parent / "data"
ARCHIVE_PATH = DATA_DIR / "mit-bih-arrhythmia-database-1.0.0.zip"
EXTRACT_DIR = DATA_DIR / "mit-bih-arrhythmia-database-1.0.0"
CHUNK_SIZE = 1024 * 1024


def format_mb(byte_count: int) -> str:
    return f"{byte_count / (1024 * 1024):.1f} MB"


def download_with_progress(url: str, destination: Path) -> None:
    partial_destination = destination.with_suffix(destination.suffix + ".part")

    with urlopen(url, timeout=30) as response:
        total_size = int(response.headers.get("Content-Length", 0))
        downloaded = 0

        with partial_destination.open("wb") as file:
            while True:
                chunk = response.read(CHUNK_SIZE)
                if not chunk:
                    break

                file.write(chunk)
                downloaded += len(chunk)

                if total_size:
                    percent = downloaded / total_size * 100
                    print(
                        f"\rDownloading... {format_mb(downloaded)} / "
                        f"{format_mb(total_size)} ({percent:.1f}%)",
                        end="",
                        flush=True,
                    )
                else:
                    print(
                        f"\rDownloading... {format_mb(downloaded)}",
                        end="",
                        flush=True,
                    )

    print()
    partial_destination.replace(destination)


def download_dataset(force: bool = False) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if ARCHIVE_PATH.exists() and not force:
        print(f"Archive already exists: {ARCHIVE_PATH}")
        return

    if ARCHIVE_PATH.exists():
        ARCHIVE_PATH.unlink()

    print("Downloading MIT-BIH Arrhythmia Database...")
    print(f"Source: {DATASET_URL}")
    download_with_progress(DATASET_URL, ARCHIVE_PATH)
    print(f"Saved: {ARCHIVE_PATH}")


def extract_dataset(force: bool = False) -> None:
    if EXTRACT_DIR.exists() and force:
        shutil.rmtree(EXTRACT_DIR)

    if EXTRACT_DIR.exists():
        print(f"Dataset already extracted: {EXTRACT_DIR}")
        return

    print("Extracting dataset...")
    with zipfile.ZipFile(ARCHIVE_PATH) as archive:
        archive.extractall(DATA_DIR)
    print(f"Extracted to: {DATA_DIR}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download and extract the MIT-BIH ECG dataset for the heart sandbox project."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Redownload and re-extract the dataset.",
    )
    args = parser.parse_args()

    download_dataset(force=args.force)
    extract_dataset(force=args.force)

    print("\nDone. Dataset files are in:")
    print(DATA_DIR)


if __name__ == "__main__":
    main()
