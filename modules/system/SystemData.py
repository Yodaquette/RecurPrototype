"""
	Andrew Goodman
	August 14, 2015
	
	Acquire system information
"""
import sys

class SystemData:
	"""
		Generate a system data report as a list
		
		Report Structure:
			[Operating System, Python version, Screen dimensions]
	"""
	def __init__(self):
		self.os_version = ''
		self.py_version = ''
		self.screenData = []

	def getSystemData(self):
		"""Return system data"""
		# Determine Tkinter module to use based on Python version
		try:
			# For Python 3.x
			import tkinter as tk
		except ImportError:
			# For Python 2.7
			import Tkinter as tk
			
		# Initialize a tkinter object to retrieve screen data
		rootScreen = tk.Tk()
		
		# Get main screen width and height resolution
		self.screenData.append(rootScreen.winfo_screenwidth())
		self.screenData.append(rootScreen.winfo_screenheight())
		
		# Get the currently running operating system
		self.os_version = sys.platform
		
		# Get the current version of Python running on the computer
		self.py_version = sys.version
		
		report = [self.os_version,self.py_version,self.screenData]
		
		return report
	
	def checkObjectSize(self,obj = None):
		"""Returns the size of an object in Bytes"""
		return sys.getsizeof(obj)

# CLASS TESTER
def main():
	s = SystemData()
	
	rep = s.getSystemData()
	print("object size: " + str(s.checkObjectSize(s)) + " bytes")
	
	for r in rep:
		print(r)

if __name__ == '__main__':
	main()