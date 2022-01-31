
from os import walk, system
from os.path import join, dirname, exists, getsize

from bz2 import compress

"""

Script by Retro(http://steamcommunity.com/id/R3TROATTACK/

"""

print('\n\nScript by Retro(http://steamcommunity.com/id/R3TROATTACK/\n\n')

paths = []

def getFiles():
	for root, dirs, files in walk('./input'):
		for file in files:
			paths.append(join(root, file)[7:].replace('\\', '/'))

def createPaths(path):
	if not exists(dirname(path)):
		try:
			os.makedirs(dirname(path))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise

def compressFiles():
	for f in paths:
		reader = open(f'./input{f}', 'rb')
		data = reader.read()
		reader.close()
		if(exists(f'./output{f}.bz2') or exists(f'./output{f}')):
			print(f'{f[1:]} already exists in output folder skipping...')
		elif(getsize(f'./input{f}') < 157286400):
			print(f'Compressing file: {f[1:]}')
			data = compress(data)
			newPath = f'./output{f}'
			createPaths(newPath)

			compressed = open(f'./output{f}.bz2', 'wb')
			print(f'Writing file: {f[1:]}.bz2')
			compressed.write(data)
			compressed.close()
		else:
			print(f'{f[1:]} to big to compress copying old file over')
			compressed = open(f'./output{f}', 'wb')
			print(f'Writing file: {f[1:]}')
			compressed.write(data)
			compressed.close()

def main():
	getFiles()
	compressFiles()
	system('pause')

if __name__ == '__main__':
	main()
