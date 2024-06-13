from fabric import *



host = "192.168.43.21"
user = "pi"
password = "1234"

filenamedist="./ssh/test.json"



def lire_fichier_distance(filename):
    with Connection(host, user, connect_kwargs={"password": password}) as c:
        résultat = c.run(f"cat {filename}")
        #if(résultat == "canette") :


#lire_fichier_distance(filenamedist)


#transfert de fichier du local vers la raspberrypi
def transfertfichier(filename,link) :
    with Connection(host, user, connect_kwargs={"password": password}) as c:
        résultat = c.put(f"{filename}")
        c.run(f"mv ./{filename} {link}")
        print("file moved \n")
        c.run(f"cat ./ssh/output/{filename}")

def cannette() :
    with Connection(host, user, connect_kwargs={"password": password}) as c:
        résultat = c.run(f"python ./ssh/output/canette.py")

    
#transfertfichier("./canette.py","./ssh/output")

cannette()