#!/usr/bin/env python3
__author__='DGideas';
#Global Illumination rendering based on Python3

class Vec:
	#left-handed coordinate system
	x=0;
	y=0;
	z=0;
	
	def __init__(self,x,y,z):
		self.x=x;
		self.y=y;
		self.z=z;
		return;
		
	def Status(self):
		stat=[self.x,self.y,self.z];
		return stat;
	
a=Vec(1,1,2);
