from math import atan,cos,sin,degrees,pi,tan

d=0.09
s=1
def fn(alpha_deg):
	alpha=alpha_deg*pi/180
	theeta=atan( (d/s+s*tan(alpha))  )
	return (degrees(theeta))


if __name__ == '__main__':
	while True:
		alpha=float(raw_input('Enter the angle:'))
		print fn( alpha )
