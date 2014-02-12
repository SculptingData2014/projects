"""
Functions for filtering tabular data.
"""

def get_column(records, col_index, separator=','):
	"""
	Returns a "column" from a list of text records as a single list.

	@param  records: list of text strings.
	@param  col_index: column to extract starting at 0 for left-most.
	@param  separator: on which to split rows.
	"""

	column = []
	for line in records:
		tokens = line.split(separator)
		if col_index < len(tokens):
			token = tokens[col_index].strip()
		else:
			token = ''
		column.append(token)

	return column


def group_by(key_column, value_column):
	"""
	Transforms pair of columns into a dictionairy where all "values"
	are grouped (as lists) by associated fields from the "key" column.
	"""

	groups = {}
	for (key, value) in zip(key_column, value_column):
		if key in groups:
			groups[key].append(value)
		else:
			groups[key] = [value]  # initialize list

	return groups

