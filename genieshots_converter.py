# The first batch of reverse telescope genie files, using timelapse.m written by James Tutt, was named slightly
# incompatably with the Alex Higley analysis code. This is just a rename and copy to the "standard" format so that the
# rest of the jupyter dot_movie.ipynb workflow can proceed nearly unchanged.
from pathlib import Path
import os
from datetime import datetime

import numpy as np
from PIL import Image
from astropy.io import fits


def get_png_files(source_dir):
    """
    Return a sorted list of PNG files in the source directory.

    Currently sorted by filename; if you prefer sort by modification time,
    change the sort key below.
    """
    png_files = sorted(
        Path(source_dir).glob("*.png"),
        key=lambda p: p.name  # or: key=lambda p: p.stat().st_mtime
    )
    return png_files


def get_file_mtime(path_obj):
    """
    Return the file modification time as a datetime object.
    """
    stat = path_obj.stat()
    return datetime.fromtimestamp(stat.st_mtime)


def format_timestamp(dt):
    """
    Format datetime as 'yy-mm-dd HH-MM-SS'
    Example: 2026-03-02 17:04:30 -> '26-03-02 17-04-30'
    """
    return dt.strftime("%y-%m-%d %H-%M-%S")


def png_to_fits(png_path, fits_path):
    """
    Read a PNG image and write it as a FITS file.

    - Converts to grayscale if needed by taking one channel.
    - Uses float32 data in the FITS file.
    """
    # Open PNG
    with Image.open(png_path) as img:
        # Convert to grayscale if it's multi-channel
        if img.mode not in ("I", "F", "L"):
            # Convert to grayscale
            img = img.convert("L")

        data = np.array(img, dtype=np.float32)

    hdu = fits.PrimaryHDU(data)
    hdul = fits.HDUList([hdu])

    # Create parent directory if needed
    fits_path.parent.mkdir(parents=True, exist_ok=True)

    # Overwrite if file exists
    hdul.writeto(fits_path, overwrite=True)


def build_output_name(index, timestamp_str):
    """
    Build output filename: image0001 26-03-02 17-04-30.fits
    """
    return f"image{index:04d} {timestamp_str}.fits"


def convert_folder(
    source_dir,
    dest_dir,
    dry_run=False
):
    """
    Convert all PNGs in source_dir to FITS files in dest_dir,
    with names based on index and file modification time.

    Parameters
    ----------
    source_dir : str or Path
        Directory containing PNG files.
    dest_dir : str or Path
        Destination directory for FITS files.
    dry_run : bool
        If True, only print planned operations without writing files.
    """
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)

    png_files = get_png_files(source_dir)

    if not png_files:
        print(f"No PNG files found in {source_dir}")
        return

    print(f"Found {len(png_files)} PNG files in {source_dir}")

    for idx, png_path in enumerate(png_files, start=1):
        # Get modification time and format it
        mtime = get_file_mtime(png_path)
        ts_str = format_timestamp(mtime)

        # Build output filename and path
        out_name = build_output_name(idx, ts_str)
        fits_path = dest_dir / out_name

        if dry_run:
            print(f"[DRY RUN] {png_path.name} -> {fits_path.name}")
        else:
            print(f"Converting {png_path.name} -> {fits_path.name}")
            png_to_fits(png_path, fits_path)


if __name__ == "__main__":
    # Adjust these paths as needed; raw strings avoid backslash-escape issues
    source = r"E:\Reverse Telescope Test Data\20260302\genieshots"
    dest = r"E:\Reverse Telescope Test Data\20260302_data\genieshots\genieshots_fits"

    # First run as dry-run to check naming without writing files:
    # convert_folder(source, dest, dry_run=True)

    # When you're happy, run the actual conversion:
    convert_folder(source, dest, dry_run=False)