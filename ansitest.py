# import sys
# import time

# def deletelines(n=1):
# 	"""delete n lines in terminal window"""
# 	for _ in range(n):
# 		sys.stdout.write('\x1b[1A')
# 		sys.stdout.write('\x1b[2K')

class ansi:
	end = '\033[0m'
	class foreground:
		black = '\033[30m'
		red = '\033[31m'
		green = '\033[32m'
		yellow = '\033[33m'
		blue = '\033[34m'
		magenta = '\033[35m'
		cyan = '\033[36m'
		white = '\033[37m'
	class background:
		black = '\033[40m'
		red = '\033[41m'
		green = '\033[42m'
		yellow = '\033[43m'
		blue = '\033[44m'
		magenta = '\033[45m'
		cyan = '\033[46m'
		white = '\033[47m'


# # print (ansi.foreground.red + ansi.background.white + "red then off" + ansi.end)
# # print("whatever")
# # print(ansi.foreground.red + "red then nothing")
# # print("whatever")

# backgroundcodes = [ansi.background.black, ansi.background.magenta, ansi.background.magenta,
#  ansi.background.cyan, ansi.background.cyan, ansi.background.blue, ansi.background.blue, ansi.background.white]
# while True:
# 	for ct in range(8, len(backgroundcodes) * 73):
# 		print(backgroundcodes[ct % len(backgroundcodes)] + "  " + ansi.end, end="")
# 		if ct % (3 * len(backgroundcodes)) == len(backgroundcodes) - 1:
# 			print()
# 			temp = backgroundcodes.pop(-1)
# 			backgroundcodes = [temp] + backgroundcodes
# 	print(ansi.end)
# 	deletelines(25)
# 	temp = backgroundcodes.pop(-1)
# 	backgroundcodes = [temp] + backgroundcodes
# 	time.sleep(.15)
