def sum_of_multiples(limit, multiples):

	# Sanitize in-coming list
	for i, digits in enumerate(multiples):
		if digits <= 0: del multiples[i]

	return sum(value for value in range(limit)
				if any(value % multiple == 0
						for multiple in multiples))
