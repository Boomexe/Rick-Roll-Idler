import subprocess
import os

cwd = os.getcwd()
mainScript = os.path.join(cwd,'src','scripts','main.py')
discordPresence = os.path.join(cwd,'src','scripts','discordrichpresence.py')

exec(open(mainScript).read())
# exec(open(discordPresence).read()) # RUNS ONLY FIRST ONE, NOT SECOND