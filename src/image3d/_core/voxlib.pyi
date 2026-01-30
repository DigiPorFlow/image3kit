"""
The VxlImg template classes
"""
from __future__ import annotations
import collections.abc
import image3kit._core.sirun
import numpy
import numpy.typing
import typing
__all__: list[str] = ['VxlImgF32', 'VxlImgI32', 'VxlImgU16', 'VxlImgU8', 'cube', 'cylinder', 'labelImage', 'readImageBase', 'shape', 'sphere', 'voxelImageTBase']
class VxlImgF32:
    def AND(self, other: VxlImgF32) -> None:
        """
        Voxel-by-voxel AND operation.
        """
    def FaceMedian06(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt) -> int:
        """
        Set voxel value to 0/1 if it has more than nAdj0/1 neighbours with value 0/1, in its 6 nearest voxels
        """
    def NOT(self, arg0: VxlImgF32) -> None:
        """
        Voxel-by-voxel NOT operation.
        """
    def OR(self, other: VxlImgF32) -> None:
        """
        Voxel-by-voxel OR operation.
        """
    def Paint(self, shape: shape) -> None:
        """
        Paint (set values of) a shape into the image.
        """
    def PaintAdd(self, shape: shape) -> None:
        """
        Add (+) a shape's value to the image.
        """
    def PaintAddAfter(self, shape: shape) -> None:
        """
        Add (+) a shape's value after the shape (plane...)
        """
    def PaintAddBefore(self, shape: shape) -> None:
        """
        Add (+) a shape's value before the shape (plane...)
        """
    def PaintAfter(self, shape: shape) -> None:
        """
        Paint after the shape (plane...)
        """
    def PaintBefore(self, shape: shape) -> None:
        """
        Paint before the shape (plane...)
        """
    def PointMedian032(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt, lbl0: typing.SupportsFloat, lbl1: typing.SupportsFloat) -> None:
        """
        Set voxel value to lbl0/1 if it has more than nAdj0/1 neighbours with value lbl0/1, in its 6+26 nearest voxels
        """
    def XOR(self, other: VxlImgF32) -> None:
        """
        Voxel-by-voxel XOR operation.
        """
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    @typing.overload
    def __init__(self, shape: tuple = (0, 0, 0), value: typing.SupportsFloat = 0) -> None:
        """
        Initialize a new image of size tuple (nx, ny, nz) with the fill value.
        """
    @typing.overload
    def __init__(self, filepath: typing.Any, processKeys: bool = True) -> None:
        """
        Read image dimensions/metadata from a (header) file. SUpported file types are .am, .raw
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
    def __repr__(self) -> str:
        ...
    def addSurfNoise(self, mask1: typing.SupportsInt, mask2: typing.SupportsInt, threshold: typing.SupportsInt, seed: typing.SupportsInt) -> None:
        """
        Add surface noise.
        """
    def adjustBrightnessWith(self, image_file: str) -> bool:
        ...
    def adjustSliceBrightness(self, mask_a: VxlImgU8, mask_b: VxlImgU8, ref_image: VxlImgF32, smooth_iter: typing.SupportsInt = 3, smooth_kernel: typing.SupportsInt = 20) -> bool:
        ...
    def averageWith(self, arg0: str) -> bool:
        ...
    def averageWith_mBE(self, arg0: str) -> bool:
        ...
    def bilateralGauss(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def bilateralX(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, x_step: typing.SupportsInt = 2, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def circleOut(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsFloat) -> None:
        """
        Circle out operation.
        """
    def cropD(self, begin: image3kit._core.sirun.int3, end: image3kit._core.sirun.int3, emptyLayers: typing.SupportsInt = 0, emptyLayersValue: typing.SupportsFloat = 1, verbose: bool = False) -> None:
        """
        Crop the image (inplace) from begin index tupe ix,iy,iz (inclusive) to and end index tuple.
        """
    def cutOutside(self, axis: str = 'z', extra_out: typing.SupportsInt = 0, threshold: typing.SupportsInt = -1, cut_highs: typing.SupportsInt = 0, shift_x: typing.SupportsInt = 0, shift_y: typing.SupportsInt = 0, fill_val: typing.SupportsInt = 0) -> None:
        ...
    def data(self) -> numpy.typing.NDArray[numpy.float32]:
        """
        Get the raw data buffer as a numpy array.
        """
    def delense032(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsFloat) -> None:
        """
        Delense operation.
        """
    def dering(self, x0: typing.SupportsInt, y0: typing.SupportsInt, x1: typing.SupportsInt, y1: typing.SupportsInt, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255, nr: typing.SupportsInt = 0, ntheta: typing.SupportsInt = 18, nz: typing.SupportsInt = 0) -> bool:
        ...
    def direction(self, arg0: str) -> None:
        """
        Get direction?
        """
    def faceMedNgrowToFrom(self, labelTo: typing.SupportsFloat, labelFrom: typing.SupportsFloat, nDiff: typing.SupportsInt) -> None:
        """
        Face median grow to/from labels.
        """
    def fillHoles(self, maxHoleRadius: typing.SupportsInt) -> None:
        """
        Fill closed holes in the image.
        """
    def flipEndian(self) -> None:
        ...
    def grow0(self) -> None:
        """
        Grow pore phase (voxel values of 0).
        """
    def growBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Expand the image boundaries, increasing its size by `num_layers` in all directions
        """
    def growLabel(self, arg0: typing.SupportsFloat) -> None:
        ...
    def growingThreshold(self, startMin: typing.SupportsFloat, startMax: typing.SupportsFloat, finalMin: typing.SupportsFloat, finalMax: typing.SupportsFloat, iterations: typing.SupportsInt = 4) -> None:
        ...
    def keepLargest0(self) -> None:
        ...
    def mapFrom(self, sourceImage: VxlImgF32, vmin: typing.SupportsFloat, vmax: typing.SupportsFloat, scale: typing.SupportsFloat, shift: typing.SupportsFloat) -> None:
        """
        Map values from another image.
        """
    def meanWide(self, width: typing.SupportsInt = 0, noise_val: typing.SupportsInt = 4, average: typing.SupportsInt = 0, delta: typing.SupportsInt = 20, iterations: typing.SupportsInt = 15, smooth_image: str = '') -> bool:
        ...
    def medianFilter(self) -> None:
        """
        Apply a 1+6-neighbour median filter.
        """
    def medianX(self) -> None:
        """
        Apply median filter with kernel size of 1 in x-direction to reduce compressed file size
        """
    def mode26(self, arg0: typing.SupportsInt) -> None:
        ...
    def modeNSames(self, nSameNeighbors: typing.SupportsInt) -> int:
        """
        Apply mode filter based on nearest 6 neighbor voxels.
        """
    def nx(self) -> int:
        ...
    def ny(self) -> int:
        ...
    def nz(self) -> int:
        ...
    def otsu_threshold(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 256) -> typing.Annotated[list[float], "FixedSize(5)"]:
        ...
    def plotAll(self, name: str = 'pltAll', minv: typing.SupportsInt = 0, maxv: typing.SupportsInt = -1000001, sliceIndex: typing.SupportsInt = -1000000, nBins: typing.SupportsInt = 128, normalAxis: str = 'xyz', grey: bool = True, color: bool = True, histogram: bool = True, zProfile: bool = True, alphaImage: VxlImgF32 = None, alphaMin: typing.SupportsInt = 0, alphaMax: typing.SupportsInt = -1000001) -> bool:
        """
        Plot all visualizations (Histogram, ZProfile, Slices) with various options, hackish for debugging, all args except are optional
        """
    def printInfo(self) -> None:
        ...
    def rangeTo(self, min: typing.SupportsFloat, max: typing.SupportsFloat, val: typing.SupportsFloat) -> None:
        """
        Set values in range [min, max] to val.
        """
    def read(self, filename: str) -> None:
        """
        Read image from file.
        """
    def readAscii(self, filename: str) -> bool:
        """
        Read image data from an ASCII file.
        """
    def readFromFloat(self, header: str, scale: typing.SupportsFloat = 1.0, shift: typing.SupportsFloat = 0.0) -> bool:
        ...
    def redirect(self, arg0: str) -> None:
        """
        Swap X axis with the given axis (y or z).
        """
    def replaceByImageRange(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def replaceOutSideValue(self, val_old: typing.SupportsInt = 0, val_new: typing.SupportsInt = 2, hole_size: typing.SupportsInt = 5) -> bool:
        ...
    def replaceRange(self, min: typing.SupportsFloat, max: typing.SupportsFloat, val: typing.SupportsFloat) -> None:
        """
        Replace values in range [min, max] with val.
        """
    def replaceRangeByImage(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def resample(self, factor: typing.SupportsFloat) -> None:
        """
        Resample image by factor f, using averaging (downsampling, f>1) or nearest when upsampling (f<1)
        """
    def resampleMax(self, factor: typing.SupportsFloat) -> VxlImgF32:
        """
        Downsample the image, setting voxel values to maximum of original encompassing voxel values.
        """
    def resampleMean(self, factor: typing.SupportsFloat) -> VxlImgF32:
        """
        Resample the image using mean interpolation.
        """
    def resampleMode(self, factor: typing.SupportsFloat) -> VxlImgF32:
        """
        Downsample the image, setting voxel values to mode of original encompassing voxel values.
        """
    def rescaleValues(self, min: typing.SupportsFloat, max: typing.SupportsFloat) -> None:
        """
        Rescale image values to [min, max].
        """
    def resliceZ(self, factor: typing.SupportsFloat) -> VxlImgF32:
        """
        Reslice along the Z axis.
        """
    def setOffset(self, offset: image3kit._core.sirun.dbl3) -> None:
        """
        Set the spatial offset (origin).
        """
    def shape(self) -> tuple:
        ...
    def shrink0(self) -> None:
        """
        Shrink pore phase (voxel values of 0).
        """
    def shrinkBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Shrink the image boundaries, decreasing its size by the given num_layers in all directions
        """
    def sliceFromPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt) -> None:
        """
        Read a slice from a Png image
        """
    def sliceToPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt, color_map: str = 'gray') -> None:
        """
        Save a 2D slice as a PNG image, color_map can be 'gray' or 'RGB'
        """
    def smooth(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1) -> bool:
        ...
    def svgHistogram(self, filename: str = 'aa.svg', bins: typing.SupportsInt = 128, min_val: typing.SupportsFloat = 3e+38, max_val: typing.SupportsFloat = -3e+38) -> int:
        ...
    def svgZProfile(self, filename: str = 'aa.svg', min_val: typing.SupportsFloat = 0, max_val: typing.SupportsFloat = 255) -> int:
        ...
    def threshold101(self, min: typing.SupportsFloat, max: typing.SupportsFloat) -> None:
        """
        Apply a threshold to binarize the image, set voxel-values to convert to 0 in between the min and max thresholds and 1 outside of it
        """
    def variance(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255) -> float:
        ...
    def write(self, filename: str) -> None:
        """
        Write the image to a file (.mhd, .raw, .ra.gz formats).
        """
    def write8bit(self, filename: str, min: typing.SupportsFloat, max: typing.SupportsFloat) -> None:
        """
        Write as 8-bit image scaled between min and max.
        """
    def writeAConnectedPoreVoxel(self, filename: str) -> None:
        """
        Write a specific connected pore voxel to file.
        """
    def writeContour(self, outSurf: str) -> None:
        """
        Write contour extraction to a surface file.
        """
    def writeNoHeader(self, filename: str) -> None:
        """
        Write the raw image data without a header.
        """
class VxlImgI32:
    def AND(self, other: VxlImgI32) -> None:
        """
        Voxel-by-voxel AND operation.
        """
    def FaceMedian06(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt) -> int:
        """
        Set voxel value to 0/1 if it has more than nAdj0/1 neighbours with value 0/1, in its 6 nearest voxels
        """
    def NOT(self, arg0: VxlImgI32) -> None:
        """
        Voxel-by-voxel NOT operation.
        """
    def OR(self, other: VxlImgI32) -> None:
        """
        Voxel-by-voxel OR operation.
        """
    def Paint(self, shape: shape) -> None:
        """
        Paint (set values of) a shape into the image.
        """
    def PaintAdd(self, shape: shape) -> None:
        """
        Add (+) a shape's value to the image.
        """
    def PaintAddAfter(self, shape: shape) -> None:
        """
        Add (+) a shape's value after the shape (plane...)
        """
    def PaintAddBefore(self, shape: shape) -> None:
        """
        Add (+) a shape's value before the shape (plane...)
        """
    def PaintAfter(self, shape: shape) -> None:
        """
        Paint after the shape (plane...)
        """
    def PaintBefore(self, shape: shape) -> None:
        """
        Paint before the shape (plane...)
        """
    def PointMedian032(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt, lbl0: typing.SupportsInt, lbl1: typing.SupportsInt) -> None:
        """
        Set voxel value to lbl0/1 if it has more than nAdj0/1 neighbours with value lbl0/1, in its 6+26 nearest voxels
        """
    def XOR(self, other: VxlImgI32) -> None:
        """
        Voxel-by-voxel XOR operation.
        """
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    @typing.overload
    def __init__(self, shape: tuple = (0, 0, 0), value: typing.SupportsInt = 0) -> None:
        """
        Initialize a new image of size tuple (nx, ny, nz) with the fill value.
        """
    @typing.overload
    def __init__(self, filepath: typing.Any, processKeys: bool = True) -> None:
        """
        Read image dimensions/metadata from a (header) file. SUpported file types are .am, .raw
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
    def __repr__(self) -> str:
        ...
    def addSurfNoise(self, mask1: typing.SupportsInt, mask2: typing.SupportsInt, threshold: typing.SupportsInt, seed: typing.SupportsInt) -> None:
        """
        Add surface noise.
        """
    def adjustBrightnessWith(self, image_file: str) -> bool:
        ...
    def adjustSliceBrightness(self, mask_a: VxlImgU8, mask_b: VxlImgU8, ref_image: VxlImgI32, smooth_iter: typing.SupportsInt = 3, smooth_kernel: typing.SupportsInt = 20) -> bool:
        ...
    def averageWith(self, arg0: str) -> bool:
        ...
    def averageWith_mBE(self, arg0: str) -> bool:
        ...
    def bilateralGauss(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def bilateralX(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, x_step: typing.SupportsInt = 2, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def circleOut(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsInt) -> None:
        """
        Circle out operation.
        """
    def cropD(self, begin: image3kit._core.sirun.int3, end: image3kit._core.sirun.int3, emptyLayers: typing.SupportsInt = 0, emptyLayersValue: typing.SupportsInt = 1, verbose: bool = False) -> None:
        """
        Crop the image (inplace) from begin index tupe ix,iy,iz (inclusive) to and end index tuple.
        """
    def cutOutside(self, axis: str = 'z', extra_out: typing.SupportsInt = 0, threshold: typing.SupportsInt = -1, cut_highs: typing.SupportsInt = 0, shift_x: typing.SupportsInt = 0, shift_y: typing.SupportsInt = 0, fill_val: typing.SupportsInt = 0) -> None:
        ...
    def data(self) -> numpy.typing.NDArray[numpy.int32]:
        """
        Get the raw data buffer as a numpy array.
        """
    def delense032(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsInt) -> None:
        """
        Delense operation.
        """
    def dering(self, x0: typing.SupportsInt, y0: typing.SupportsInt, x1: typing.SupportsInt, y1: typing.SupportsInt, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255, nr: typing.SupportsInt = 0, ntheta: typing.SupportsInt = 18, nz: typing.SupportsInt = 0) -> bool:
        ...
    def direction(self, arg0: str) -> None:
        """
        Get direction?
        """
    def faceMedNgrowToFrom(self, labelTo: typing.SupportsInt, labelFrom: typing.SupportsInt, nDiff: typing.SupportsInt) -> None:
        """
        Face median grow to/from labels.
        """
    def fillHoles(self, maxHoleRadius: typing.SupportsInt) -> None:
        """
        Fill closed holes in the image.
        """
    def flipEndian(self) -> None:
        ...
    def grow0(self) -> None:
        """
        Grow pore phase (voxel values of 0).
        """
    def growBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Expand the image boundaries, increasing its size by `num_layers` in all directions
        """
    def growLabel(self, arg0: typing.SupportsInt) -> None:
        ...
    def growingThreshold(self, startMin: typing.SupportsInt, startMax: typing.SupportsInt, finalMin: typing.SupportsInt, finalMax: typing.SupportsInt, iterations: typing.SupportsInt = 4) -> None:
        ...
    def keepLargest0(self) -> None:
        ...
    def mapFrom(self, sourceImage: VxlImgI32, vmin: typing.SupportsInt, vmax: typing.SupportsInt, scale: typing.SupportsFloat, shift: typing.SupportsFloat) -> None:
        """
        Map values from another image.
        """
    def meanWide(self, width: typing.SupportsInt = 0, noise_val: typing.SupportsInt = 4, average: typing.SupportsInt = 0, delta: typing.SupportsInt = 20, iterations: typing.SupportsInt = 15, smooth_image: str = '') -> bool:
        ...
    def medianFilter(self) -> None:
        """
        Apply a 1+6-neighbour median filter.
        """
    def medianX(self) -> None:
        """
        Apply median filter with kernel size of 1 in x-direction to reduce compressed file size
        """
    def mode26(self, arg0: typing.SupportsInt) -> None:
        ...
    def modeNSames(self, nSameNeighbors: typing.SupportsInt) -> int:
        """
        Apply mode filter based on nearest 6 neighbor voxels.
        """
    def nx(self) -> int:
        ...
    def ny(self) -> int:
        ...
    def nz(self) -> int:
        ...
    def otsu_threshold(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 256) -> typing.Annotated[list[float], "FixedSize(5)"]:
        ...
    def plotAll(self, name: str = 'pltAll', minv: typing.SupportsInt = 0, maxv: typing.SupportsInt = -1000001, sliceIndex: typing.SupportsInt = -1000000, nBins: typing.SupportsInt = 128, normalAxis: str = 'xyz', grey: bool = True, color: bool = True, histogram: bool = True, zProfile: bool = True, alphaImage: VxlImgI32 = None, alphaMin: typing.SupportsInt = 0, alphaMax: typing.SupportsInt = -1000001) -> bool:
        """
        Plot all visualizations (Histogram, ZProfile, Slices) with various options, hackish for debugging, all args except are optional
        """
    def printInfo(self) -> None:
        ...
    def rangeTo(self, min: typing.SupportsInt, max: typing.SupportsInt, val: typing.SupportsInt) -> None:
        """
        Set values in range [min, max] to val.
        """
    def read(self, filename: str) -> None:
        """
        Read image from file.
        """
    def readAscii(self, filename: str) -> bool:
        """
        Read image data from an ASCII file.
        """
    def readFromFloat(self, header: str, scale: typing.SupportsFloat = 1.0, shift: typing.SupportsFloat = 0.0) -> bool:
        ...
    def redirect(self, arg0: str) -> None:
        """
        Swap X axis with the given axis (y or z).
        """
    def replaceByImageRange(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def replaceOutSideValue(self, val_old: typing.SupportsInt = 0, val_new: typing.SupportsInt = 2, hole_size: typing.SupportsInt = 5) -> bool:
        ...
    def replaceRange(self, min: typing.SupportsInt, max: typing.SupportsInt, val: typing.SupportsInt) -> None:
        """
        Replace values in range [min, max] with val.
        """
    def replaceRangeByImage(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def resample(self, factor: typing.SupportsFloat) -> None:
        """
        Resample image by factor f, using averaging (downsampling, f>1) or nearest when upsampling (f<1)
        """
    def resampleMax(self, factor: typing.SupportsFloat) -> VxlImgI32:
        """
        Downsample the image, setting voxel values to maximum of original encompassing voxel values.
        """
    def resampleMean(self, factor: typing.SupportsFloat) -> VxlImgI32:
        """
        Resample the image using mean interpolation.
        """
    def resampleMode(self, factor: typing.SupportsFloat) -> VxlImgI32:
        """
        Downsample the image, setting voxel values to mode of original encompassing voxel values.
        """
    def rescaleValues(self, min: typing.SupportsInt, max: typing.SupportsInt) -> None:
        """
        Rescale image values to [min, max].
        """
    def resliceZ(self, factor: typing.SupportsFloat) -> VxlImgI32:
        """
        Reslice along the Z axis.
        """
    def setOffset(self, offset: image3kit._core.sirun.dbl3) -> None:
        """
        Set the spatial offset (origin).
        """
    def shape(self) -> tuple:
        ...
    def shrink0(self) -> None:
        """
        Shrink pore phase (voxel values of 0).
        """
    def shrinkBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Shrink the image boundaries, decreasing its size by the given num_layers in all directions
        """
    def sliceFromPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt) -> None:
        """
        Read a slice from a Png image
        """
    def sliceToPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt, color_map: str = 'gray') -> None:
        """
        Save a 2D slice as a PNG image, color_map can be 'gray' or 'RGB'
        """
    def smooth(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1) -> bool:
        ...
    def svgHistogram(self, filename: str = 'aa.svg', bins: typing.SupportsInt = 128, min_val: typing.SupportsFloat = 3e+38, max_val: typing.SupportsFloat = -3e+38) -> int:
        ...
    def svgZProfile(self, filename: str = 'aa.svg', min_val: typing.SupportsFloat = 0, max_val: typing.SupportsFloat = 255) -> int:
        ...
    def threshold101(self, min: typing.SupportsInt, max: typing.SupportsInt) -> None:
        """
        Apply a threshold to binarize the image, set voxel-values to convert to 0 in between the min and max thresholds and 1 outside of it
        """
    def variance(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255) -> float:
        ...
    def write(self, filename: str) -> None:
        """
        Write the image to a file (.mhd, .raw, .ra.gz formats).
        """
    def write8bit(self, filename: str, min: typing.SupportsFloat, max: typing.SupportsFloat) -> None:
        """
        Write as 8-bit image scaled between min and max.
        """
    def writeAConnectedPoreVoxel(self, filename: str) -> None:
        """
        Write a specific connected pore voxel to file.
        """
    def writeContour(self, outSurf: str) -> None:
        """
        Write contour extraction to a surface file.
        """
    def writeNoHeader(self, filename: str) -> None:
        """
        Write the raw image data without a header.
        """
class VxlImgU16:
    def AND(self, other: VxlImgU16) -> None:
        """
        Voxel-by-voxel AND operation.
        """
    def FaceMedian06(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt) -> int:
        """
        Set voxel value to 0/1 if it has more than nAdj0/1 neighbours with value 0/1, in its 6 nearest voxels
        """
    def NOT(self, arg0: VxlImgU16) -> None:
        """
        Voxel-by-voxel NOT operation.
        """
    def OR(self, other: VxlImgU16) -> None:
        """
        Voxel-by-voxel OR operation.
        """
    def Paint(self, shape: shape) -> None:
        """
        Paint (set values of) a shape into the image.
        """
    def PaintAdd(self, shape: shape) -> None:
        """
        Add (+) a shape's value to the image.
        """
    def PaintAddAfter(self, shape: shape) -> None:
        """
        Add (+) a shape's value after the shape (plane...)
        """
    def PaintAddBefore(self, shape: shape) -> None:
        """
        Add (+) a shape's value before the shape (plane...)
        """
    def PaintAfter(self, shape: shape) -> None:
        """
        Paint after the shape (plane...)
        """
    def PaintBefore(self, shape: shape) -> None:
        """
        Paint before the shape (plane...)
        """
    def PointMedian032(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt, lbl0: typing.SupportsInt, lbl1: typing.SupportsInt) -> None:
        """
        Set voxel value to lbl0/1 if it has more than nAdj0/1 neighbours with value lbl0/1, in its 6+26 nearest voxels
        """
    def XOR(self, other: VxlImgU16) -> None:
        """
        Voxel-by-voxel XOR operation.
        """
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    @typing.overload
    def __init__(self, shape: tuple = (0, 0, 0), value: typing.SupportsInt = 0) -> None:
        """
        Initialize a new image of size tuple (nx, ny, nz) with the fill value.
        """
    @typing.overload
    def __init__(self, filepath: typing.Any, processKeys: bool = True) -> None:
        """
        Read image dimensions/metadata from a (header) file. SUpported file types are .am, .raw
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
    def __repr__(self) -> str:
        ...
    def addSurfNoise(self, mask1: typing.SupportsInt, mask2: typing.SupportsInt, threshold: typing.SupportsInt, seed: typing.SupportsInt) -> None:
        """
        Add surface noise.
        """
    def adjustBrightnessWith(self, image_file: str) -> bool:
        ...
    def adjustSliceBrightness(self, mask_a: VxlImgU8, mask_b: VxlImgU8, ref_image: VxlImgU16, smooth_iter: typing.SupportsInt = 3, smooth_kernel: typing.SupportsInt = 20) -> bool:
        ...
    def averageWith(self, arg0: str) -> bool:
        ...
    def averageWith_mBE(self, arg0: str) -> bool:
        ...
    def bilateralGauss(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def bilateralX(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, x_step: typing.SupportsInt = 2, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def circleOut(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsInt) -> None:
        """
        Circle out operation.
        """
    def cropD(self, begin: image3kit._core.sirun.int3, end: image3kit._core.sirun.int3, emptyLayers: typing.SupportsInt = 0, emptyLayersValue: typing.SupportsInt = 1, verbose: bool = False) -> None:
        """
        Crop the image (inplace) from begin index tupe ix,iy,iz (inclusive) to and end index tuple.
        """
    def cutOutside(self, axis: str = 'z', extra_out: typing.SupportsInt = 0, threshold: typing.SupportsInt = -1, cut_highs: typing.SupportsInt = 0, shift_x: typing.SupportsInt = 0, shift_y: typing.SupportsInt = 0, fill_val: typing.SupportsInt = 0) -> None:
        ...
    def data(self) -> numpy.typing.NDArray[numpy.uint16]:
        """
        Get the raw data buffer as a numpy array.
        """
    def delense032(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsInt) -> None:
        """
        Delense operation.
        """
    def dering(self, x0: typing.SupportsInt, y0: typing.SupportsInt, x1: typing.SupportsInt, y1: typing.SupportsInt, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255, nr: typing.SupportsInt = 0, ntheta: typing.SupportsInt = 18, nz: typing.SupportsInt = 0) -> bool:
        ...
    def direction(self, arg0: str) -> None:
        """
        Get direction?
        """
    def faceMedNgrowToFrom(self, labelTo: typing.SupportsInt, labelFrom: typing.SupportsInt, nDiff: typing.SupportsInt) -> None:
        """
        Face median grow to/from labels.
        """
    def fillHoles(self, maxHoleRadius: typing.SupportsInt) -> None:
        """
        Fill closed holes in the image.
        """
    def flipEndian(self) -> None:
        ...
    def grow0(self) -> None:
        """
        Grow pore phase (voxel values of 0).
        """
    def growBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Expand the image boundaries, increasing its size by `num_layers` in all directions
        """
    def growLabel(self, arg0: typing.SupportsInt) -> None:
        ...
    def growingThreshold(self, startMin: typing.SupportsInt, startMax: typing.SupportsInt, finalMin: typing.SupportsInt, finalMax: typing.SupportsInt, iterations: typing.SupportsInt = 4) -> None:
        ...
    def keepLargest0(self) -> None:
        ...
    def mapFrom(self, sourceImage: VxlImgU16, vmin: typing.SupportsInt, vmax: typing.SupportsInt, scale: typing.SupportsFloat, shift: typing.SupportsFloat) -> None:
        """
        Map values from another image.
        """
    def meanWide(self, width: typing.SupportsInt = 0, noise_val: typing.SupportsInt = 4, average: typing.SupportsInt = 0, delta: typing.SupportsInt = 20, iterations: typing.SupportsInt = 15, smooth_image: str = '') -> bool:
        ...
    def medianFilter(self) -> None:
        """
        Apply a 1+6-neighbour median filter.
        """
    def medianX(self) -> None:
        """
        Apply median filter with kernel size of 1 in x-direction to reduce compressed file size
        """
    def mode26(self, arg0: typing.SupportsInt) -> None:
        ...
    def modeNSames(self, nSameNeighbors: typing.SupportsInt) -> int:
        """
        Apply mode filter based on nearest 6 neighbor voxels.
        """
    def nx(self) -> int:
        ...
    def ny(self) -> int:
        ...
    def nz(self) -> int:
        ...
    def otsu_threshold(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 256) -> typing.Annotated[list[float], "FixedSize(5)"]:
        ...
    def plotAll(self, name: str = 'pltAll', minv: typing.SupportsInt = 0, maxv: typing.SupportsInt = -1000001, sliceIndex: typing.SupportsInt = -1000000, nBins: typing.SupportsInt = 128, normalAxis: str = 'xyz', grey: bool = True, color: bool = True, histogram: bool = True, zProfile: bool = True, alphaImage: VxlImgU16 = None, alphaMin: typing.SupportsInt = 0, alphaMax: typing.SupportsInt = -1000001) -> bool:
        """
        Plot all visualizations (Histogram, ZProfile, Slices) with various options, hackish for debugging, all args except are optional
        """
    def printInfo(self) -> None:
        ...
    def rangeTo(self, min: typing.SupportsInt, max: typing.SupportsInt, val: typing.SupportsInt) -> None:
        """
        Set values in range [min, max] to val.
        """
    def read(self, filename: str) -> None:
        """
        Read image from file.
        """
    def readAscii(self, filename: str) -> bool:
        """
        Read image data from an ASCII file.
        """
    def readFromFloat(self, header: str, scale: typing.SupportsFloat = 1.0, shift: typing.SupportsFloat = 0.0) -> bool:
        ...
    def redirect(self, arg0: str) -> None:
        """
        Swap X axis with the given axis (y or z).
        """
    def replaceByImageRange(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def replaceOutSideValue(self, val_old: typing.SupportsInt = 0, val_new: typing.SupportsInt = 2, hole_size: typing.SupportsInt = 5) -> bool:
        ...
    def replaceRange(self, min: typing.SupportsInt, max: typing.SupportsInt, val: typing.SupportsInt) -> None:
        """
        Replace values in range [min, max] with val.
        """
    def replaceRangeByImage(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def resample(self, factor: typing.SupportsFloat) -> None:
        """
        Resample image by factor f, using averaging (downsampling, f>1) or nearest when upsampling (f<1)
        """
    def resampleMax(self, factor: typing.SupportsFloat) -> VxlImgU16:
        """
        Downsample the image, setting voxel values to maximum of original encompassing voxel values.
        """
    def resampleMean(self, factor: typing.SupportsFloat) -> VxlImgU16:
        """
        Resample the image using mean interpolation.
        """
    def resampleMode(self, factor: typing.SupportsFloat) -> VxlImgU16:
        """
        Downsample the image, setting voxel values to mode of original encompassing voxel values.
        """
    def rescaleValues(self, min: typing.SupportsInt, max: typing.SupportsInt) -> None:
        """
        Rescale image values to [min, max].
        """
    def resliceZ(self, factor: typing.SupportsFloat) -> VxlImgU16:
        """
        Reslice along the Z axis.
        """
    def segment(self, n_segments: typing.SupportsInt = 2, thresholds: collections.abc.Sequence[typing.SupportsInt], min_sizes: collections.abc.Sequence[typing.SupportsInt], smooth_image: str = '', noise_val: typing.SupportsFloat = 16.0, resolution_sq: typing.SupportsFloat = 2.0, write_dumps: typing.SupportsInt = 0) -> bool:
        ...
    def segment2(self, nSegs: typing.SupportsInt = 2, th: collections.abc.Sequence[typing.SupportsInt] = [], minSizs: collections.abc.Sequence[typing.SupportsInt] = [], noisev: typing.SupportsFloat = 2.0, localF: typing.SupportsFloat = 800.0, flatnes: typing.SupportsFloat = 0.1, resolution: typing.SupportsFloat = 2.0, gradFactor: typing.SupportsFloat = 0.0, krnl: typing.SupportsInt = 2, nItrs: typing.SupportsInt = 13, writedumps: typing.SupportsInt = 0) -> bool:
        ...
    def setOffset(self, offset: image3kit._core.sirun.dbl3) -> None:
        """
        Set the spatial offset (origin).
        """
    def shape(self) -> tuple:
        ...
    def shrink0(self) -> None:
        """
        Shrink pore phase (voxel values of 0).
        """
    def shrinkBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Shrink the image boundaries, decreasing its size by the given num_layers in all directions
        """
    def sliceFromPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt) -> None:
        """
        Read a slice from a Png image
        """
    def sliceToPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt, color_map: str = 'gray') -> None:
        """
        Save a 2D slice as a PNG image, color_map can be 'gray' or 'RGB'
        """
    def smooth(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1) -> bool:
        ...
    def svgHistogram(self, filename: str = 'aa.svg', bins: typing.SupportsInt = 128, min_val: typing.SupportsFloat = 3e+38, max_val: typing.SupportsFloat = -3e+38) -> int:
        ...
    def svgZProfile(self, filename: str = 'aa.svg', min_val: typing.SupportsFloat = 0, max_val: typing.SupportsFloat = 255) -> int:
        ...
    def threshold101(self, min: typing.SupportsInt, max: typing.SupportsInt) -> None:
        """
        Apply a threshold to binarize the image, set voxel-values to convert to 0 in between the min and max thresholds and 1 outside of it
        """
    def variance(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255) -> float:
        ...
    def write(self, filename: str) -> None:
        """
        Write the image to a file (.mhd, .raw, .ra.gz formats).
        """
    def write8bit(self, filename: str, min: typing.SupportsFloat, max: typing.SupportsFloat) -> None:
        """
        Write as 8-bit image scaled between min and max.
        """
    def writeAConnectedPoreVoxel(self, filename: str) -> None:
        """
        Write a specific connected pore voxel to file.
        """
    def writeContour(self, outSurf: str) -> None:
        """
        Write contour extraction to a surface file.
        """
    def writeNoHeader(self, filename: str) -> None:
        """
        Write the raw image data without a header.
        """
class VxlImgU8:
    def AND(self, other: VxlImgU8) -> None:
        """
        Voxel-by-voxel AND operation.
        """
    def FaceMedian06(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt) -> int:
        """
        Set voxel value to 0/1 if it has more than nAdj0/1 neighbours with value 0/1, in its 6 nearest voxels
        """
    def NOT(self, arg0: VxlImgU8) -> None:
        """
        Voxel-by-voxel NOT operation.
        """
    def OR(self, other: VxlImgU8) -> None:
        """
        Voxel-by-voxel OR operation.
        """
    def Paint(self, shape: shape) -> None:
        """
        Paint (set values of) a shape into the image.
        """
    def PaintAdd(self, shape: shape) -> None:
        """
        Add (+) a shape's value to the image.
        """
    def PaintAddAfter(self, shape: shape) -> None:
        """
        Add (+) a shape's value after the shape (plane...)
        """
    def PaintAddBefore(self, shape: shape) -> None:
        """
        Add (+) a shape's value before the shape (plane...)
        """
    def PaintAfter(self, shape: shape) -> None:
        """
        Paint after the shape (plane...)
        """
    def PaintBefore(self, shape: shape) -> None:
        """
        Paint before the shape (plane...)
        """
    def PointMedian032(self, nAdj0: typing.SupportsInt, nAdj1: typing.SupportsInt, lbl0: typing.SupportsInt, lbl1: typing.SupportsInt) -> None:
        """
        Set voxel value to lbl0/1 if it has more than nAdj0/1 neighbours with value lbl0/1, in its 6+26 nearest voxels
        """
    def XOR(self, other: VxlImgU8) -> None:
        """
        Voxel-by-voxel XOR operation.
        """
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
    @typing.overload
    def __init__(self, shape: tuple = (0, 0, 0), value: typing.SupportsInt = 0) -> None:
        """
        Initialize a new image of size tuple (nx, ny, nz) with the fill value.
        """
    @typing.overload
    def __init__(self, filepath: typing.Any, processKeys: bool = True) -> None:
        """
        Read image dimensions/metadata from a (header) file. SUpported file types are .am, .raw
        """
    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
    def __repr__(self) -> str:
        ...
    def addSurfNoise(self, mask1: typing.SupportsInt, mask2: typing.SupportsInt, threshold: typing.SupportsInt, seed: typing.SupportsInt) -> None:
        """
        Add surface noise.
        """
    def adjustBrightnessWith(self, image_file: str) -> bool:
        ...
    def adjustSliceBrightness(self, mask_a: VxlImgU8, mask_b: VxlImgU8, ref_image: VxlImgU8, smooth_iter: typing.SupportsInt = 3, smooth_kernel: typing.SupportsInt = 20) -> bool:
        ...
    def averageWith(self, arg0: str) -> bool:
        ...
    def averageWith_mBE(self, arg0: str) -> bool:
        ...
    def bilateralGauss(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def bilateralX(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, x_step: typing.SupportsInt = 2, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1, sigma_spatial: typing.SupportsFloat = 2.0) -> None:
        ...
    def circleOut(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsInt) -> None:
        """
        Circle out operation.
        """
    def cropD(self, begin: image3kit._core.sirun.int3, end: image3kit._core.sirun.int3, emptyLayers: typing.SupportsInt = 0, emptyLayersValue: typing.SupportsInt = 1, verbose: bool = False) -> None:
        """
        Crop the image (inplace) from begin index tupe ix,iy,iz (inclusive) to and end index tuple.
        """
    def cutOutside(self, axis: str = 'z', extra_out: typing.SupportsInt = 0, threshold: typing.SupportsInt = -1, cut_highs: typing.SupportsInt = 0, shift_x: typing.SupportsInt = 0, shift_y: typing.SupportsInt = 0, fill_val: typing.SupportsInt = 0) -> None:
        ...
    def data(self) -> numpy.typing.NDArray[numpy.uint8]:
        """
        Get the raw data buffer as a numpy array.
        """
    def delense032(self, x: typing.SupportsInt, y: typing.SupportsInt, r: typing.SupportsInt, d: str, val: typing.SupportsInt) -> None:
        """
        Delense operation.
        """
    def dering(self, x0: typing.SupportsInt, y0: typing.SupportsInt, x1: typing.SupportsInt, y1: typing.SupportsInt, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255, nr: typing.SupportsInt = 0, ntheta: typing.SupportsInt = 18, nz: typing.SupportsInt = 0) -> bool:
        ...
    def direction(self, arg0: str) -> None:
        """
        Get direction?
        """
    def distMapExtrude(self, distMapDict: dict = {}, offset: typing.SupportsFloat = 0.5, scale: typing.SupportsFloat = 1.0, power: typing.SupportsFloat = 1.0) -> None:
        """
        Extrude proportional to distance map
        """
    def faceMedNgrowToFrom(self, labelTo: typing.SupportsInt, labelFrom: typing.SupportsInt, nDiff: typing.SupportsInt) -> None:
        """
        Face median grow to/from labels.
        """
    def fillHoles(self, maxHoleRadius: typing.SupportsInt) -> None:
        """
        Fill closed holes in the image.
        """
    def flipEndian(self) -> None:
        ...
    def grow0(self) -> None:
        """
        Grow pore phase (voxel values of 0).
        """
    def growBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Expand the image boundaries, increasing its size by `num_layers` in all directions
        """
    def growLabel(self, arg0: typing.SupportsInt) -> None:
        ...
    def growingThreshold(self, startMin: typing.SupportsInt, startMax: typing.SupportsInt, finalMin: typing.SupportsInt, finalMax: typing.SupportsInt, iterations: typing.SupportsInt = 4) -> None:
        ...
    def keepLargest0(self) -> None:
        ...
    def mapFrom(self, sourceImage: VxlImgU8, vmin: typing.SupportsInt, vmax: typing.SupportsInt, scale: typing.SupportsFloat, shift: typing.SupportsFloat) -> None:
        """
        Map values from another image.
        """
    def meanWide(self, width: typing.SupportsInt = 0, noise_val: typing.SupportsInt = 4, average: typing.SupportsInt = 0, delta: typing.SupportsInt = 20, iterations: typing.SupportsInt = 15, smooth_image: str = '') -> bool:
        ...
    def medianFilter(self) -> None:
        """
        Apply a 1+6-neighbour median filter.
        """
    def medianX(self) -> None:
        """
        Apply median filter with kernel size of 1 in x-direction to reduce compressed file size
        """
    def mode26(self, arg0: typing.SupportsInt) -> None:
        ...
    def modeNSames(self, nSameNeighbors: typing.SupportsInt) -> int:
        """
        Apply mode filter based on nearest 6 neighbor voxels.
        """
    def nx(self) -> int:
        ...
    def ny(self) -> int:
        ...
    def nz(self) -> int:
        ...
    def otsu_threshold(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 256) -> typing.Annotated[list[float], "FixedSize(5)"]:
        ...
    def plotAll(self, name: str = 'pltAll', minv: typing.SupportsInt = 0, maxv: typing.SupportsInt = -1000001, sliceIndex: typing.SupportsInt = -1000000, nBins: typing.SupportsInt = 128, normalAxis: str = 'xyz', grey: bool = True, color: bool = True, histogram: bool = True, zProfile: bool = True, alphaImage: VxlImgU8 = None, alphaMin: typing.SupportsInt = 0, alphaMax: typing.SupportsInt = -1000001) -> bool:
        """
        Plot all visualizations (Histogram, ZProfile, Slices) with various options, hackish for debugging, all args except are optional
        """
    def printInfo(self) -> None:
        ...
    def rangeTo(self, min: typing.SupportsInt, max: typing.SupportsInt, val: typing.SupportsInt) -> None:
        """
        Set values in range [min, max] to val.
        """
    def read(self, filename: str) -> None:
        """
        Read image from file.
        """
    def readAscii(self, filename: str) -> bool:
        """
        Read image data from an ASCII file.
        """
    def readFromFloat(self, header: str, scale: typing.SupportsFloat = 1.0, shift: typing.SupportsFloat = 0.0) -> bool:
        ...
    def redirect(self, arg0: str) -> None:
        """
        Swap X axis with the given axis (y or z).
        """
    def replaceByImageRange(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def replaceOutSideValue(self, val_old: typing.SupportsInt = 0, val_new: typing.SupportsInt = 2, hole_size: typing.SupportsInt = 5) -> bool:
        ...
    def replaceRange(self, min: typing.SupportsInt, max: typing.SupportsInt, val: typing.SupportsInt) -> None:
        """
        Replace values in range [min, max] with val.
        """
    def replaceRangeByImage(self, min_val: typing.SupportsFloat, max_val: typing.SupportsFloat, image_file: str) -> None:
        ...
    def resample(self, factor: typing.SupportsFloat) -> None:
        """
        Resample image by factor f, using averaging (downsampling, f>1) or nearest when upsampling (f<1)
        """
    def resampleMax(self, factor: typing.SupportsFloat) -> VxlImgU8:
        """
        Downsample the image, setting voxel values to maximum of original encompassing voxel values.
        """
    def resampleMean(self, factor: typing.SupportsFloat) -> VxlImgU8:
        """
        Resample the image using mean interpolation.
        """
    def resampleMode(self, factor: typing.SupportsFloat) -> VxlImgU8:
        """
        Downsample the image, setting voxel values to mode of original encompassing voxel values.
        """
    def rescaleValues(self, min: typing.SupportsInt, max: typing.SupportsInt) -> None:
        """
        Rescale image values to [min, max].
        """
    def resliceZ(self, factor: typing.SupportsFloat) -> VxlImgU8:
        """
        Reslice along the Z axis.
        """
    def segment(self, n_segments: typing.SupportsInt = 2, thresholds: collections.abc.Sequence[typing.SupportsInt], min_sizes: collections.abc.Sequence[typing.SupportsInt], smooth_image: str = '', noise_val: typing.SupportsFloat = 16.0, resolution_sq: typing.SupportsFloat = 2.0, write_dumps: typing.SupportsInt = 0) -> bool:
        ...
    def segment2(self, nSegs: typing.SupportsInt = 2, th: collections.abc.Sequence[typing.SupportsInt] = [], minSizs: collections.abc.Sequence[typing.SupportsInt] = [], noisev: typing.SupportsFloat = 2.0, localF: typing.SupportsFloat = 800.0, flatnes: typing.SupportsFloat = 0.1, resolution: typing.SupportsFloat = 2.0, gradFactor: typing.SupportsFloat = 0.0, krnl: typing.SupportsInt = 2, nItrs: typing.SupportsInt = 13, writedumps: typing.SupportsInt = 0) -> bool:
        ...
    def setOffset(self, offset: image3kit._core.sirun.dbl3) -> None:
        """
        Set the spatial offset (origin).
        """
    def shape(self) -> tuple:
        ...
    def shrink0(self) -> None:
        """
        Shrink pore phase (voxel values of 0).
        """
    def shrinkBox(self, num_layers: typing.SupportsInt) -> None:
        """
        Shrink the image boundaries, decreasing its size by the given num_layers in all directions
        """
    def sliceFromPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt) -> None:
        """
        Read a slice from a Png image
        """
    def sliceToPng(self, normalAxis: str, filename: str, sliceIndex: typing.SupportsInt, val_min: typing.SupportsInt, val_max: typing.SupportsInt, color_map: str = 'gray') -> None:
        """
        Save a 2D slice as a PNG image, color_map can be 'gray' or 'RGB'
        """
    def smooth(self, iterations: typing.SupportsInt = 1, kernel_radius: typing.SupportsInt = 1, sigma_val: typing.SupportsFloat = 16.0, sharpness: typing.SupportsFloat = 0.1) -> bool:
        ...
    def svgHistogram(self, filename: str = 'aa.svg', bins: typing.SupportsInt = 128, min_val: typing.SupportsFloat = 3e+38, max_val: typing.SupportsFloat = -3e+38) -> int:
        ...
    def svgZProfile(self, filename: str = 'aa.svg', min_val: typing.SupportsFloat = 0, max_val: typing.SupportsFloat = 255) -> int:
        ...
    def threshold101(self, min: typing.SupportsInt, max: typing.SupportsInt) -> None:
        """
        Apply a threshold to binarize the image, set voxel-values to convert to 0 in between the min and max thresholds and 1 outside of it
        """
    def variance(self, min_val: typing.SupportsInt = 0, max_val: typing.SupportsInt = 255) -> float:
        ...
    def write(self, filename: str) -> None:
        """
        Write the image to a file (.mhd, .raw, .ra.gz formats).
        """
    def write8bit(self, filename: str, min: typing.SupportsFloat, max: typing.SupportsFloat) -> None:
        """
        Write as 8-bit image scaled between min and max.
        """
    def writeAConnectedPoreVoxel(self, filename: str) -> None:
        """
        Write a specific connected pore voxel to file.
        """
    def writeContour(self, outSurf: str) -> None:
        """
        Write contour extraction to a surface file.
        """
    def writeNoHeader(self, filename: str) -> None:
        """
        Write the raw image data without a header.
        """
class cube(shape):
    def __init__(self, arg0: tuple, arg1: tuple, arg2: typing.SupportsInt) -> None:
        ...
class cylinder(shape):
    def __init__(self, arg0: tuple, arg1: tuple, arg2: typing.SupportsFloat, arg3: typing.SupportsInt) -> None:
        ...
class shape:
    pass
class sphere(shape):
    def __init__(self, arg0: tuple, arg1: typing.SupportsFloat, arg2: typing.SupportsInt) -> None:
        ...
class voxelImageTBase:
    pass
def labelImage(arg0: VxlImgU8, arg1: typing.SupportsFloat, arg2: typing.SupportsFloat) -> VxlImgI32:
    ...
def readImageBase(filename: typing.Any, processKeys: typing.SupportsInt = 1) -> voxelImageTBase:
    """
    Global helper to read an image from a file.
    """
