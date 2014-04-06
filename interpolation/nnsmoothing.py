import math

class NNSmoothing(object):
    """
    Implements "nearest neighbor" smoothing, roughly based k-NN regression:
    <http://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm>
    """

    verbose_mode = False

    def __init__(self, input_csv):
        """
        The input data should be a CSV file where each line has the format:

            x, y, value

        Each value should be a decimal.
        Headers and ill-formated lines are skipped.
        """

        self.input_data = []
        for line in open(input_csv):
            line = line.strip()
            try:
                x, y, value = line.split(',')
                x, y, value = float(x), float(y), float(value)
                self.input_data.append((x, y, value))
            except Exception as ex:
                print ('"%s" skipped: %s' % (line, ex))

        print ('%d data points loaded' % len(self.input_data))

    def dist(self, x1, y1, x2, y2):
        """
        Implements the distance between (x1, y1) and (x2, y2).
        """
        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    def interpolate(self, x_new, y_new, k=4):
        """
        Returns a "smoothed" value for the point (x_new, y_new) by weighting values
        associated to the K nearest neighbors to (x_new, y_new) from the input_data.
        """
        # creates a new list of tuples indexed by the _distance_ from (x_new, y_new)
        # to each point in input_data, and sorts it by distance.
        results = [
            (self.dist(x_new, y_new, x, y), x, y, value) for (x, y, value) in self.input_data
        ]
        results.sort(key=lambda item: item[0])
        results = results[0:k]

        if self.verbose_mode:
            print ('NNSmoothing: %s -> %s' % ((x_new, y_new), results))

        weighted_values = [value / dist for (dist, _, _, value) in results if dist != 0]
        weights = [1.0 / dist for (dist, _, _, _) in results if dist != 0]

        return sum(weighted_values) / sum(weights)

