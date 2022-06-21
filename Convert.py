import os
import subprocess
import pydub
for root, subFolder, files in os.walk("."):
	for item in files:
		fileNamePath = str(root + "/" + item)
		print(fileNamePath)
		cmd = 'lame --preset insane "%s\"' % fileNamePath
		subprocess.call(cmd, shell=True)
