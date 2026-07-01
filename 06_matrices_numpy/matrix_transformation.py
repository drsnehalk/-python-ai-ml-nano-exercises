def mat_vec_mul(matrix,vector):
	result = []
	for row in matrix:
		total = 0
		for i in range(len(vector)):
			total+= row[i] * vector[i]
		result.append(total)
	return result

def scale_2D(sx, sy):
	return[
	[sx, 0],
	[0, sy]
	]
scale = scale_2D(2,3)


def reflection_x():
	return[
	[1,0],
	[0,-1]
	]

def reflection_y():
	return[
	[-1,0],
	[-0,1]
	]


point = [3, 2]

print(mat_vec_mul(scale, point))
reflect_x = reflection_x()
reflect_y = reflection_y()
print(mat_vec_mul(reflect_x,point))
print(mat_vec_mul(reflect_y,point))


import math

def rotation_2d(theta):
	return[
	[math.cos(theta),-math.sin(theta)],
	[math.sin(theta),math.cos(theta)]
	]
rotate = rotation_2d(math.pi / 2)
print(mat_vec_mul(rotate, [3, 2]))

def shear(k):
	return[
	[1, k],
	[0, 1]
	]

point = [3,2]
print(mat_vec_mul(shear(1),point))

scaled_point = mat_vec_mul(scale, point)
final_point = mat_vec_mul(reflect_x, scaled_point)

print(scaled_point)
print(final_point)
