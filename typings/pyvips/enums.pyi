"""
This type stub file was generated by pyright.
"""

from typing import Literal

class BandFormat:
    """BandFormat.

The format used for each band element.

Each corresponds to a native C type for the current machine. For example,
#VIPS_FORMAT_USHORT is <type>unsigned short</type>.

Attributes:

    NOTSET (str): invalid setting

    UCHAR (str): unsigned char format

    CHAR (str): char format

    USHORT (str): unsigned short format

    SHORT (str): short format

    UINT (str): unsigned int format

    INT (str): int format

    FLOAT (str): float format

    COMPLEX (str): complex (two floats) format

    DOUBLE (str): double float format

    DPCOMPLEX (str): double complex (two double) format

    """
    NOTSET: Literal["notset"]
    UCHAR: Literal["uchar"]
    CHAR: Literal["char"]
    USHORT: Literal["ushort"]
    SHORT: Literal["short"]
    UINT: Literal["uint"]
    INT: Literal["int"]
    FLOAT: Literal["float"]
    COMPLEX: Literal["complex"]
    DOUBLE: Literal["double"]
    DPCOMPLEX: Literal["dpcomplex"]


class BlendMode:
    """BlendMode.

The various Porter-Duff and PDF blend modes. See vips_composite(),
for example.

The Cairo docs have a nice explanation of all the blend modes:

https://www.cairographics.org/operators

The non-separable modes are not implemented.

Attributes:

    CLEAR (str): where the second object is drawn, the first is removed

    SOURCE (str): the second object is drawn as if nothing were below

    OVER (str): the image shows what you would expect if you held two semi-transparent slides on top of each other

    IN (str): the first object is removed completely, the second is only drawn where the first was

    OUT (str): the second is drawn only where the first isn't

    ATOP (str): this leaves the first object mostly intact, but mixes both objects in the overlapping area

    DEST (str): leaves the first object untouched, the second is discarded completely

    DEST_OVER (str): like OVER, but swaps the arguments

    DEST_IN (str): like IN, but swaps the arguments

    DEST_OUT (str): like OUT, but swaps the arguments

    DEST_ATOP (str): like ATOP, but swaps the arguments

    XOR (str): something like a difference operator

    ADD (str): a bit like adding the two images

    SATURATE (str): a bit like the darker of the two

    MULTIPLY (str): at least as dark as the darker of the two inputs

    SCREEN (str): at least as light as the lighter of the inputs

    OVERLAY (str): multiplies or screens colors, depending on the lightness

    DARKEN (str): the darker of each component

    LIGHTEN (str): the lighter of each component

    COLOUR_DODGE (str): brighten first by a factor second

    COLOUR_BURN (str): darken first by a factor of second

    HARD_LIGHT (str): multiply or screen, depending on lightness

    SOFT_LIGHT (str): darken or lighten, depending on lightness

    DIFFERENCE (str): difference of the two

    EXCLUSION (str): somewhat like DIFFERENCE, but lower-contrast

    """
    CLEAR: Literal["clear"]
    SOURCE: Literal["source"]
    OVER: Literal["over"]
    IN: Literal["in"]
    OUT: Literal["out"]
    ATOP: Literal["atop"]
    DEST: Literal["dest"]
    DEST_OVER: Literal["dest_over"]
    DEST_IN: Literal["dest_in"]
    DEST_OUT: Literal["dest_out"]
    DEST_ATOP: Literal["dest_atop"]
    XOR: Literal["xor"]
    ADD: Literal["add"]
    SATURATE: Literal["saturate"]
    MULTIPLY: Literal["multiply"]
    SCREEN: Literal["screen"]
    OVERLAY: Literal["overlay"]
    DARKEN: Literal["darken"]
    LIGHTEN: Literal["lighten"]
    COLOUR_DODGE: Literal["colour_dodge"]
    COLOUR_BURN: Literal["colour_burn"]
    HARD_LIGHT: Literal["hard_light"]
    SOFT_LIGHT: Literal["soft_light"]
    DIFFERENCE: Literal["difference"]
    EXCLUSION: Literal["exclusion"]


class Coding:
    """Coding.

How pixels are coded.

Normally, pixels are uncoded and can be manipulated as you would expect.
However some file formats code pixels for compression, and sometimes it's
useful to be able to manipulate images in the coded format.

The gaps in the numbering are historical and must be maintained. Allocate
new numbers from the end.

Attributes:

    NONE (str): pixels are not coded

    LABQ (str): pixels encode 3 float CIELAB values as 4 uchar

    RAD (str): pixels encode 3 float RGB as 4 uchar (Radiance coding)

    """
    ERROR: Literal["error"]
    NONE: Literal["none"]
    LABQ: Literal["labq"]
    RAD: Literal["rad"]


class Interpretation:
    """Interpretation.

How the values in an image should be interpreted. For example, a
three-band float image of type #VIPS_INTERPRETATION_LAB should have its
pixels interpreted as coordinates in CIE Lab space.

RGB and sRGB are treated in the same way. Use the colourspace functions if
you want some other behaviour.

The gaps in numbering are historical and must be maintained. Allocate
new numbers from the end.

Attributes:

    MULTIBAND (str): generic many-band image

    B_W (str): some kind of single-band image

    HISTOGRAM (str): a 1D image, eg. histogram or lookup table

    XYZ (str): the first three bands are CIE XYZ

    LAB (str): pixels are in CIE Lab space

    CMYK (str): the first four bands are in CMYK space

    LABQ (str): implies #VIPS_CODING_LABQ

    RGB (str): generic RGB space

    CMC (str): a uniform colourspace based on CMC(1:1)

    LCH (str): pixels are in CIE LCh space

    LABS (str): CIE LAB coded as three signed 16-bit values

    SRGB (str): pixels are sRGB

    YXY (str): pixels are CIE Yxy

    FOURIER (str): image is in fourier space

    RGB16 (str): generic 16-bit RGB

    GREY16 (str): generic 16-bit mono

    MATRIX (str): a matrix

    SCRGB (str): pixels are scRGB

    HSV (str): pixels are HSV

    """
    ERROR: Literal["error"]
    MULTIBAND: Literal["multiband"]
    B_W: Literal["b-w"]
    HISTOGRAM: Literal["histogram"]
    XYZ: Literal["xyz"]
    LAB: Literal["lab"]
    CMYK: Literal["cmyk"]
    LABQ: Literal["labq"]
    RGB: Literal["rgb"]
    CMC: Literal["cmc"]
    LCH: Literal["lch"]
    LABS: Literal["labs"]
    SRGB: Literal["srgb"]
    YXY: Literal["yxy"]
    FOURIER: Literal["fourier"]
    RGB16: Literal["rgb16"]
    GREY16: Literal["grey16"]
    MATRIX: Literal["matrix"]
    SCRGB: Literal["scrgb"]
    HSV: Literal["hsv"]


class DemandStyle:
    """DemandStyle.

See vips_image_pipelinev(). Operations can hint to the VIPS image IO
system about the kind of demand geometry they prefer.

These demand styles are given below in order of increasing
restrictiveness.  When demanding output from a pipeline,
vips_image_generate()
will use the most restrictive of the styles requested by the operations
in the pipeline.

#VIPS_DEMAND_STYLE_THINSTRIP --- This operation would like to output strips
the width of the image and a few pels high. This is option suitable for
point-to-point operations, such as those in the arithmetic package.

This option is only efficient for cases where each output pel depends
upon the pel in the corresponding position in the input image.

#VIPS_DEMAND_STYLE_FATSTRIP --- This operation would like to output strips
the width of the image and as high as possible. This option is suitable
for area operations which do not violently transform coordinates, such
as vips_conv().

#VIPS_DEMAND_STYLE_SMALLTILE --- This is the most general demand format.
Output is demanded in small (around 100x100 pel) sections. This style works
reasonably efficiently, even for bizzare operations like 45 degree rotate.

#VIPS_DEMAND_STYLE_ANY --- This image is not being demand-read from a disc
file (even indirectly) so any demand style is OK. It's used for things like
vips_black() where the pixels are calculated.

See also: vips_image_pipelinev().

Attributes:

    SMALLTILE (str): demand in small (typically 64x64 pixel) tiles

    FATSTRIP (str): demand in fat (typically 10 pixel high) strips

    THINSTRIP (str): demand in thin (typically 1 pixel high) strips

    """
    ERROR: Literal["error"]
    SMALLTILE: Literal["smalltile"]
    FATSTRIP: Literal["fatstrip"]
    THINSTRIP: Literal["thinstrip"]


class OperationRelational:
    """OperationRelational.

See also: vips_relational().

Attributes:

    EQUAL (str): ==

    NOTEQ (str): !=

    LESS (str): <

    LESSEQ (str): <=

    MORE (str): >

    MOREEQ (str): >=

    """
    EQUAL: Literal["equal"]
    NOTEQ: Literal["noteq"]
    LESS: Literal["less"]
    LESSEQ: Literal["lesseq"]
    MORE: Literal["more"]
    MOREEQ: Literal["moreeq"]


class OperationBoolean:
    """OperationBoolean.

See also: vips_boolean().

Attributes:

    AND (str): &

    OR (str): |

    EOR (str): ^

    LSHIFT (str): >>

    RSHIFT (str): <<

    """
    AND = ...
    OR = ...
    EOR = ...
    LSHIFT = ...
    RSHIFT = ...


class OperationMath2:
    """OperationMath2.

See also: vips_math().

Attributes:

    POW (str): pow( left, right )

    WOP (str): pow( right, left )

    ATAN2 (str): atan2( left, right )

    """
    POW = ...
    WOP = ...
    ATAN2 = ...


class OperationComplex2:
    """OperationComplex2.

See also: vips_complex2().

Attributes:

    CROSS_PHASE (str): convert to polar coordinates

    """
    CROSS_PHASE = ...


class OperationMath:
    """OperationMath.

See also: vips_math().

Attributes:

    SIN (str): sin(), angles in degrees

    COS (str): cos(), angles in degrees

    TAN (str): tan(), angles in degrees

    ASIN (str): asin(), angles in degrees

    ACOS (str): acos(), angles in degrees

    ATAN (str): atan(), angles in degrees

    SINH (str): sinh(), angles in radians

    COSH (str): cosh(), angles in radians

    TANH (str): tanh(), angles in radians

    ASINH (str): asinh(), angles in radians

    ACOSH (str): acosh(), angles in radians

    ATANH (str): atanh(), angles in radians

    LOG (str): log base e

    LOG10 (str): log base 10

    EXP (str): e to the something

    EXP10 (str): 10 to the something

    """
    SIN = ...
    COS = ...
    TAN = ...
    ASIN = ...
    ACOS = ...
    ATAN = ...
    SINH = ...
    COSH = ...
    TANH = ...
    ASINH = ...
    ACOSH = ...
    ATANH = ...
    LOG = ...
    LOG10 = ...
    EXP = ...
    EXP10 = ...


class OperationRound:
    """OperationRound.

See also: vips_round().

Attributes:

    RINT (str): round to nearest

    CEIL (str): the smallest integral value not less than

    FLOOR (str): largest integral value not greater than

    """
    RINT = ...
    CEIL = ...
    FLOOR = ...


class OperationComplex:
    """OperationComplex.

See also: vips_complex().

Attributes:

    POLAR (str): convert to polar coordinates

    RECT (str): convert to rectangular coordinates

    CONJ (str): complex conjugate

    """
    POLAR = ...
    RECT = ...
    CONJ = ...


class OperationComplexget:
    """OperationComplexget.

See also: vips_complexget().

Attributes:

    REAL (str): get real component

    IMAG (str): get imaginary component

    """
    REAL = ...
    IMAG = ...


class Combine:
    """Combine.

How to combine values. See vips_compass(), for example.

Attributes:

    MAX (str): take the maximum of the possible values

    SUM (str): sum all the values

    MIN (str): take the minimum value

    """
    MAX = ...
    SUM = ...
    MIN = ...


class Access:
    """Access.

The type of access an operation has to supply. See vips_tilecache()
and #VipsForeign.

@VIPS_ACCESS_RANDOM means requests can come in any order.

@VIPS_ACCESS_SEQUENTIAL means requests will be top-to-bottom, but with some
amount of buffering behind the read point for small non-local accesses.

Attributes:

    RANDOM (str): can read anywhere

    SEQUENTIAL (str): top-to-bottom reading only, but with a small buffer

    """
    RANDOM = ...
    SEQUENTIAL = ...
    SEQUENTIAL_UNBUFFERED = ...


class Extend:
    """Extend.

See vips_embed(), vips_conv(), vips_affine() and so on.

When the edges of an image are extended, you can specify
how you want the extension done.

#VIPS_EXTEND_BLACK --- new pixels are black, ie. all bits are zero.

#VIPS_EXTEND_COPY --- each new pixel takes the value of the nearest edge
pixel

#VIPS_EXTEND_REPEAT --- the image is tiled to fill the new area

#VIPS_EXTEND_MIRROR --- the image is reflected and tiled to reduce hash
edges

#VIPS_EXTEND_WHITE --- new pixels are white, ie. all bits are set

#VIPS_EXTEND_BACKGROUND --- colour set from the @background property

We have to specify the exact value of each enum member since we have to
keep these frozen for back compat with vips7.

See also: vips_embed().

Attributes:

    BLACK (str): extend with black (all 0) pixels

    COPY (str): copy the image edges

    REPEAT (str): repeat the whole image

    MIRROR (str): mirror the whole image

    WHITE (str): extend with white (all bits set) pixels

    BACKGROUND (str): extend with colour from the @background property

    """
    BLACK = ...
    COPY = ...
    REPEAT = ...
    MIRROR = ...
    WHITE = ...
    BACKGROUND = ...


class CompassDirection:
    """CompassDirection.

A direction on a compass. Used for vips_gravity(), for example.

Attributes:

    CENTRE (str): centre

    NORTH (str): north

    EAST (str): east

    SOUTH (str): south

    WEST (str): west

    NORTH_EAST (str): north-east

    SOUTH_EAST (str): south-east

    SOUTH_WEST (str): south-west

    NORTH_WEST (str): north-west

    """
    CENTRE = ...
    NORTH = ...
    EAST = ...
    SOUTH = ...
    WEST = ...
    NORTH_EAST = ...
    SOUTH_EAST = ...
    SOUTH_WEST = ...
    NORTH_WEST = ...


class Direction:
    """Direction.

See vips_flip(), vips_join() and so on.

Operations like vips_flip() need to be told whether to flip left-right or
top-bottom.

See also: vips_flip(), vips_join().

Attributes:

    HORIZONTAL (str): left-right

    VERTICAL (str): top-bottom

    """
    HORIZONTAL = ...
    VERTICAL = ...


class Align:
    """Align.

See vips_join() and so on.

Operations like vips_join() need to be told whether to align images on the
low or high coordinate edge, or centre.

See also: vips_join().

Attributes:

    LOW (str): align low coordinate edge

    CENTRE (str): align centre

    HIGH (str): align high coordinate edge

    """
    LOW = ...
    CENTRE = ...
    HIGH = ...


class Interesting:
    """Interesting.

Pick the algorithm vips uses to decide image "interestingness". This is used
by vips_smartcrop(), for example, to decide what parts of the image to
keep.

#VIPS_INTERESTING_NONE and #VIPS_INTERESTING_LOW mean the same -- the
crop is positioned at the top or left. #VIPS_INTERESTING_HIGH positions at
the bottom or right.

See also: vips_smartcrop().

Attributes:

    NONE (str): do nothing

    CENTRE (str): just take the centre

    ENTROPY (str): use an entropy measure

    ATTENTION (str): look for features likely to draw human attention

    LOW (str): position the crop towards the low coordinate

    HIGH (str): position the crop towards the high coordinate

    ALL (str): everything is interesting

    """
    NONE = ...
    CENTRE = ...
    ENTROPY = ...
    ATTENTION = ...
    LOW = ...
    HIGH = ...
    ALL = ...


class Angle:
    """Angle.

See vips_rot() and so on.

Fixed rotate angles.

See also: vips_rot().

Attributes:

    D0 (str): no rotate

    D90 (str): 90 degrees clockwise

    D180 (str): 180 degree rotate

    D270 (str): 90 degrees anti-clockwise

    """
    D0 = ...
    D90 = ...
    D180 = ...
    D270 = ...


class Angle45:
    """Angle45.

See vips_rot45() and so on.

Fixed rotate angles.

See also: vips_rot45().

Attributes:

    D0 (str): no rotate

    D45 (str): 45 degrees clockwise

    D90 (str): 90 degrees clockwise

    D135 (str): 135 degrees clockwise

    D180 (str): 180 degrees

    D225 (str): 135 degrees anti-clockwise

    D270 (str): 90 degrees anti-clockwise

    D315 (str): 45 degrees anti-clockwise

    """
    D0 = ...
    D45 = ...
    D90 = ...
    D135 = ...
    D180 = ...
    D225 = ...
    D270 = ...
    D315 = ...


class Precision:
    """Precision.

How accurate an operation should be.

Attributes:

    INTEGER (str): int everywhere

    FLOAT (str): float everywhere

    APPROXIMATE (str): approximate integer output

    """
    INTEGER = ...
    FLOAT = ...
    APPROXIMATE = ...


class FailOn:
    """FailOn.

How sensitive loaders are to errors, from never stop (very insensitive), to
stop on the smallest warning (very sensitive).

Each one implies the ones before it, so #VIPS_FAIL_ON_ERROR implies
#VIPS_FAIL_ON_TRUNCATED.

Attributes:

    NONE (str): never stop

    TRUNCATED (str): stop on image truncated, nothing else

    ERROR (str): stop on serious error or truncation

    WARNING (str): stop on anything, even warnings

    """
    NONE = ...
    TRUNCATED = ...
    ERROR = ...
    WARNING = ...


class ForeignPpmFormat:
    """ForeignPpmFormat.

The netpbm file format to save as.

#VIPS_FOREIGN_PPM_FORMAT_PBM images are single bit.

#VIPS_FOREIGN_PPM_FORMAT_PGM images are 8, 16, or 32-bits, one band.

#VIPS_FOREIGN_PPM_FORMAT_PPM images are 8, 16, or 32-bits, three bands.

#VIPS_FOREIGN_PPM_FORMAT_PFM images are 32-bit float pixels.

Attributes:

    PBM (str): portable bitmap

    PGM (str): portable greymap

    PPM (str): portable pixmap

    PFM (str): portable float map

    """
    PBM = ...
    PGM = ...
    PPM = ...
    PFM = ...


class ForeignSubsample:
    """ForeignSubsample.

Set subsampling mode.

Attributes:

    AUTO (str): prevent subsampling when quality >= 90

    ON (str): always perform subsampling

    OFF (str): never perform subsampling

    """
    AUTO = ...
    ON = ...
    OFF = ...


class ForeignDzLayout:
    """ForeignDzLayout.

What directory layout and metadata standard to use.

Attributes:

    DZ (str): use DeepZoom directory layout

    ZOOMIFY (str): use Zoomify directory layout

    GOOGLE (str): use Google maps directory layout

    IIIF (str): use IIIF v2 directory layout

    IIIF3 (str): use IIIF v3 directory layout

    """
    DZ = ...
    ZOOMIFY = ...
    GOOGLE = ...
    IIIF = ...
    IIIF3 = ...


class ForeignDzDepth:
    """ForeignDzDepth.

How many pyramid layers to create.

Attributes:

    ONEPIXEL (str): create layers down to 1x1 pixel

    ONETILE (str): create layers down to 1x1 tile

    ONE (str): only create a single layer

    """
    ONEPIXEL = ...
    ONETILE = ...
    ONE = ...


class ForeignDzContainer:
    """ForeignDzContainer.

How many pyramid layers to create.

Attributes:

    FS (str): write tiles to the filesystem

    ZIP (str): write tiles to a zip file

    SZI (str): write to a szi file

    """
    FS = ...
    ZIP = ...
    SZI = ...


class RegionShrink:
    """RegionShrink.

How to calculate the output pixels when shrinking a 2x2 region.

Attributes:

    MEAN (str): use the average

    MEDIAN (str): use the median

    MODE (str): use the mode

    MAX (str): use the maximum

    MIN (str): use the minimum

    NEAREST (str): use the top-left pixel

    """
    MEAN = ...
    MEDIAN = ...
    MODE = ...
    MAX = ...
    MIN = ...
    NEAREST = ...


class ForeignWebpPreset:
    """ForeignWebpPreset.

Tune lossy encoder settings for different image types.

Attributes:

    DEFAULT (str): default preset

    PICTURE (str): digital picture, like portrait, inner shot

    PHOTO (str): outdoor photograph, with natural lighting

    DRAWING (str): hand or line drawing, with high-contrast details

    ICON (str): small-sized colorful images

    TEXT (str): text-like

    """
    DEFAULT = ...
    PICTURE = ...
    PHOTO = ...
    DRAWING = ...
    ICON = ...
    TEXT = ...


class ForeignTiffCompression:
    """ForeignTiffCompression.

The compression types supported by the tiff writer.

Use @Q to set the jpeg compression level, default 75.

Use @predictor to set the lzw or deflate prediction, default horizontal.

Use @lossless to set WEBP lossless compression.

Use @level to set webp and zstd compression level.

Attributes:

    NONE (str): no compression

    JPEG (str): jpeg compression

    DEFLATE (str): deflate (zip) compression

    PACKBITS (str): packbits compression

    CCITTFAX4 (str): fax4 compression

    LZW (str): LZW compression

    WEBP (str): WEBP compression

    ZSTD (str): ZSTD compression

    JP2K (str): JP2K compression

    """
    NONE = ...
    JPEG = ...
    DEFLATE = ...
    PACKBITS = ...
    CCITTFAX4 = ...
    LZW = ...
    WEBP = ...
    ZSTD = ...
    JP2K = ...


class ForeignTiffPredictor:
    """ForeignTiffPredictor.

The predictor can help deflate and lzw compression. The values are fixed by
the tiff library.

Attributes:

    NONE (str): no prediction

    HORIZONTAL (str): horizontal differencing

    FLOAT (str): float predictor

    """
    NONE = ...
    HORIZONTAL = ...
    FLOAT = ...


class ForeignTiffResunit:
    """ForeignTiffResunit.

Use inches or centimeters as the resolution unit for a tiff file.

Attributes:

    CM (str): use centimeters

    INCH (str): use inches

    """
    CM = ...
    INCH = ...


class ForeignHeifCompression:
    """ForeignHeifCompression.

The compression format to use inside a HEIF container.

This is assumed to use the same numbering as %heif_compression_format.

Attributes:

    HEVC (str): x265

    AVC (str): x264

    JPEG (str): jpeg

    AV1 (str): aom

    """
    HEVC = ...
    AVC = ...
    JPEG = ...
    AV1 = ...


class Size:
    """Size.

Controls whether an operation should upsize, downsize, both up and
downsize, or force a size.

See also: vips_thumbnail().

Attributes:

    BOTH (str): size both up and down

    UP (str): only upsize

    DOWN (str): only downsize

    FORCE (str): force size, that is, break aspect ratio

    """
    BOTH = ...
    UP = ...
    DOWN = ...
    FORCE = ...


class Intent:
    """Intent.

The rendering intent. #VIPS_INTENT_ABSOLUTE is best for
scientific work, #VIPS_INTENT_RELATIVE is usually best for
accurate communication with other imaging libraries.

Attributes:

    PERCEPTUAL (str): perceptual rendering intent

    RELATIVE (str): relative colorimetric rendering intent

    SATURATION (str): saturation rendering intent

    ABSOLUTE (str): absolute colorimetric rendering intent

    """
    PERCEPTUAL = ...
    RELATIVE = ...
    SATURATION = ...
    ABSOLUTE = ...


class Kernel:
    """Kernel.

The resampling kernels vips supports. See vips_reduce(), for example.

Attributes:

    NEAREST (str): The nearest pixel to the point.

    LINEAR (str): Convolve with a triangle filter.

    CUBIC (str): Convolve with a cubic filter.

    MITCHELL (str): Convolve with a Mitchell kernel.

    LANCZOS2 (str): Convolve with a two-lobe Lanczos kernel.

    LANCZOS3 (str): Convolve with a three-lobe Lanczos kernel.

    """
    NEAREST = ...
    LINEAR = ...
    CUBIC = ...
    MITCHELL = ...
    LANCZOS2 = ...
    LANCZOS3 = ...


class PCS:
    """PCS.

Pick a Profile Connection Space for vips_icc_import() and
vips_icc_export(). LAB is usually best, XYZ can be more convenient in some
cases.

Attributes:

    LAB (str): use CIELAB D65 as the Profile Connection Space

    XYZ (str): use XYZ as the Profile Connection Space

    """
    LAB = ...
    XYZ = ...


class OperationMorphology:
    """OperationMorphology.

More like hit-miss, really.

See also: vips_morph().

Attributes:

    ERODE (str): true if all set

    DILATE (str): true if one set

    """
    ERODE = ...
    DILATE = ...


class CombineMode:
    """CombineMode.

See vips_draw_image() and so on.

Operations like vips_draw_image() need to be told how to combine images
from two sources.

See also: vips_join().

Attributes:

    SET (str): set pixels to the new value

    ADD (str): add pixels

    """
    SET = ...
    ADD = ...


class Token:
    """Token.

Attributes:

    """
    LEFT = ...
    RIGHT = ...
    STRING = ...
    EQUALS = ...


class Saveable:
    """Saveable.

See also: #VipsForeignSave.

Attributes:

    MONO (str): 1 band (eg. CSV)

    RGB (str): 1 or 3 bands (eg. PPM)

    RGBA (str): 1, 2, 3 or 4 bands (eg. PNG)

    RGBA_ONLY (str): 3 or 4 bands (eg. WEBP)

    RGB_CMYK (str): 1, 3 or 4 bands (eg. JPEG)

    ANY (str): any number of bands (eg. TIFF)

    """
    MONO = ...
    RGB = ...
    RGBA = ...
    RGBA_ONLY = ...
    RGB_CMYK = ...
    ANY = ...


class ImageType:
    """ImageType.

Attributes:

    """
    ERROR = ...
    NONE = ...
    SETBUF = ...
    SETBUF_FOREIGN = ...
    OPENIN = ...
    MMAPIN = ...
    MMAPINRW = ...
    OPENOUT = ...


