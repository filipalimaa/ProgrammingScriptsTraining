import os 
import shutil   

pasta = "downloads"
subpasta= os.path.join(pasta, "txt")
# garantir que a pasta txt existe
os.makedirs(subpasta, exist_ok=True)
ficheiros = os.listdir(pasta)

for f in ficheiros:
    if f.endswith("."):
        origem = os.path.join(pasta, f)
        destino = os.path.join(subpasta, f)           
        shutil.move(origem, destino)
