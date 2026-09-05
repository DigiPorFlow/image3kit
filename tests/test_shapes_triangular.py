from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np

import image3kit as ik


def _make_triangular_image():
    img = ik.VxlImgU8((120, 30, 33), 1)
    # Same parameters as pnmkit/tests/synthetic_triu.py::_make_tringu_image
    img.paint(ik.triangular((0, 28, 16), L1=15, L2=15, h=18, Lt=30, c_rp_rt=3.2, c_side_mid=1.6, val=0))
    img.spacing = ik.dbl3(5e-7, 5e-7, 5e-7)
    return img


def test_triangular_porosity():
    img = _make_triangular_image()
    assert img.shape == (120, 30, 33)

    expected_porosity = 0.14723905723905725
    actual_porosity = np.mean(img.data == 0)
    assert abs(actual_porosity - expected_porosity) < 1e-6


def test_triangular_roundtrip():
    img = _make_triangular_image()

    with tempfile.TemporaryDirectory() as tmp_dir:
        mhd_path = str(Path(tmp_dir) / "tringu.mhd")
        tif_path = str(Path(tmp_dir) / "tringu.tif")
        img.write(mhd_path)
        img.write(tif_path)

        img_read = ik.read_image(tif_path)
        assert img_read.shape == img.shape
        assert np.array_equal(img_read.data, img.data)
        assert tuple(img_read.spacing) == tuple(img.spacing)


if __name__ == "__main__":
    test_triangular_porosity()
    test_triangular_roundtrip()
