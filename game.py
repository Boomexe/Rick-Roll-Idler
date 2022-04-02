from os import getcwd, path
from os.path import join

cwd = getcwd()
mainScript = path.join(cwd,'src', 'rickrollidler', 'scripts', 'main.py')
discordPresence = path.join(cwd, 'src', 'rickrollidler', 'scripts', 'discordrichpresence.py')

exec(open(mainScript).read())