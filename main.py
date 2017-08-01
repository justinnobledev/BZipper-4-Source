import os, bz2

"""

Script by Retro(http://steamcommunity.com/id/R3TROATTACK/

"""

print('\n\nScript by Retro(http://steamcommunity.com/id/R3TROATTACK/\n\n')

paths = []

def getFiles():
	for root, dirs, files in os.walk('./input'):
		for file in files:
			paths.append(os.path.join(root, file)[7:].replace('\\', '/'))

def createPaths(path):
	if not os.path.exists(os.path.dirname(path)):
		try:
			os.makedirs(os.path.dirname(path))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise

def compressFiles():
	for file in paths:
		reader = open('./input'+file, 'rb')
		data = reader.read()
		reader.close()
		print('Compressing file: %s' % file)
		data = bz2.compress(data)
		newPath = './output%s' % file
		createPaths(newPath)
		compressed = open('./output'+file+'.bz2', 'wb')
		print('Writing file: %s.bz2' % file)
		compressed.write(data)
		compressed.close()

def main():
	getFiles()
	compressFiles()
	os.system('pause')

if __name__ == '__main__':
	main()