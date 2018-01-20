from math import atan,cos,sin,degrees,pi

d=1
s=0.1
def fn(alpha_deg):
	alpha=alpha_deg*pi/180
	theeta=atan( (d*sin(alpha)-s) / (d*cos(alpha)) )
	return -45-(degrees(theeta))


if __name__ == '__main__':
	while True:
		alpha=float(raw_input('Enter the angle:'))
		print fn( alpha )
