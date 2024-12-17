from resize_image import resize_and_save_image
from pathlib import Path

CURRENT_DIR = Path.cwd()
HORIZONTAL_SOURCE_DIR = Path.joinpath(CURRENT_DIR, "src_for_horizontal")
VERTICAL_SOURCE_DIR = Path.joinpath(CURRENT_DIR, "src_for_vertical")
HORIZONTAL_OUTPUT_DIR = Path.joinpath(CURRENT_DIR, "outs/horizontal_outs")
VERTICAL_OUTPUT_DIR = Path.joinpath(CURRENT_DIR, "outs/vertical_outs")


def main():
    # конвертим горизонтальные
    if HORIZONTAL_SOURCE_DIR.exists() and HORIZONTAL_SOURCE_DIR.is_dir():
        for file in HORIZONTAL_SOURCE_DIR.iterdir():
            print(f"[INFO] ---->>> converting {file.stem}")
            resize_and_save_image(file, HORIZONTAL_OUTPUT_DIR)

    if VERTICAL_SOURCE_DIR.exists() and VERTICAL_SOURCE_DIR.is_dir():
        for file in VERTICAL_SOURCE_DIR.iterdir():
            print(f"[INFO] ---->>> converting {file.stem}")
            resize_and_save_image(file, VERTICAL_OUTPUT_DIR, horizontal=False)


if __name__ == "__main__":
    main()
