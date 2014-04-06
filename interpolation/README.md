Example use of Nearest Neighbors Interpolation
----------------------------------------------

The class `NNSmoothing` implements a function defined by interpolation from
values in an initial set of training data. The function is defined for 2D
inputs such as latitude-longitude coordinates.

The NN stands for "nearest neighbor," since the interpolant for a new XY-point
is determined by selecting the K nearest points from the training set.

The distance method, `dist`, must be implented by the user for their specific
use case. (Or by subclassing `NNSmoothing`.)

The `example.py` script in this folder illustrates how this works using the
supplied training set. Supplying a
[Euclidean distance](http://en.wikipedia.org/wiki/Euclidean_distance)
function for `dist`, one obtains output like the following:

    $ python example.py
    "Longitude [degrees_east],Latitude [degrees_north],Bot. Depth [m]" skipped: could not convert string to float: Longitude [degrees_east]
    100 data points loaded

    using default k for interpolation

    interpolated value for (301.750000, -48.580000): 257.464388
    interpolated value for (276.149990, -3.500000): 2155.006991
    interpolated value for (310.870000, -49.880000): 1070.107459
    interpolated value for (264.980010, 14.183000): 3240.927287

    using k = 8 for interpolation

    interpolated value for (301.750000, -48.580000): 612.957045
    interpolated value for (276.149990, -3.500000): 1763.780680
    interpolated value for (310.870000, -49.880000): 901.028601
    interpolated value for (264.980010, 14.183000): 3223.945885


Notice that changing, K, the number of nearest neighbors used to determine
the interpolant, affects the interpolated value.
