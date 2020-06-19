"""
	rectangle = '12345678'
	RX(rectangle) = '87654321'


def RX( rectangle ):
	result = ''
	for c in rectangle:
		result = c + result
	return result	