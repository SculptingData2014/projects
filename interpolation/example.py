"""
Test script for the nnsmoothing.NNSmoothing class.
"""

from nnsmoothing import NNSmoothing

src_file = 'data/sa-sample.csv'

# instantiate the class with test data file
smoother = NNSmoothing(src_file)

# uncomment the following line to reveal debugging info
# smoother.verbose_mode = True

test_points = [
    (301.75, -48.58),
    (276.14999, -3.5),
    (310.87, -49.88),
    (264.98001, 14.183),
]

print """
using default k for interpolation
"""
for x, y in test_points:
    ival = smoother.interpolate(x, y)
    print 'interpolated value for (%f, %f): %f' % (x, y, ival)

print """
using k = 8 for interpolation
"""
for x, y in test_points:
    ival = smoother.interpolate(x, y, k=8)
    print 'interpolated value for (%f, %f): %f' % (x, y, ival)

