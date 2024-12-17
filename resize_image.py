import numpy as np
from PIL import Image
import seam_carving
from pathlib import Path

ADD_VALUE = 740


def resize_and_save_image(filepath: str, output_dir: Path, horizontal=True) -> None:
    src = np.array(Image.open(filepath))
    src_h, src_w, _ = src.shape

    if horizontal:
        src_w += ADD_VALUE
    else:
        src_h += ADD_VALUE

    dst = seam_carving.resize(
        src,  # source image (rgb or gray)
        size=(src_w, src_h),  # target size
        energy_mode="backward",  # choose from {backward, forward}
        order="width-first",  # choose from {width-first, height-first}
        keep_mask=None,  # object mask to protect from removal
    )
    file_name = str(filepath).split("\\")[-1].split(".")[0] + "_converted.jpg"
    out_path = Path.joinpath(output_dir, file_name)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    Image.fromarray(dst).save(out_path)
