import subprocess
import os

new_directory = "./GreenGuardiansGW/Arduino/Pictures"

os.chdir(new_directory)

command = "ls"

# Exécution de la commande
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("Sortie standard :", result.stdout)

lst=result.stdout
lst=lst.split("\n")
lst.remove("")
print(f"lst : {lst}")

filename=lst[-1]
print(f"filename : {filename}")