from buildhat import Motor
eyebrows = Motor('C')
eyebrows.run_to_position(0)

def move_eyebrows (position):
	current_position = eyebrows.get_aposition()
	if position < current_position:
		rotation = 'anticlockwise'
	else:
		rotation = 'clockwise'
	eyebrows.run_to_position(position, direction = rotation)
