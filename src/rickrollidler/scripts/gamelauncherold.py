from os import getcwd
from os.path import join

cwd = getcwd()
mainScript = join(cwd,'src', 'rickrollidler', 'scripts', 'main.py')
discordPresence = join(cwd, 'src', 'rickrollidler', 'scripts', 'discordrichpresence.py')

exec(open(mainScript).read())