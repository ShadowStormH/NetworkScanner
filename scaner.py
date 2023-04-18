import socket

def leer_archivo(filename):
    #Con el archivo abierto haz lo siguiente
    with open(filename,"r") as file:
        lineas = file.readlines()
        lineaslimpias=[]
        for linea in lineas:
            lineaslimpias.append(linea.rstrip())
        return lineaslimpias

#host = input("Introduce la Ip a escanear: ")
#ports = input("Introduce los puertos a escanear (separados con comas): ")

hosts = leer_archivo("ips.txt")
ports = leer_archivo("puertos_comunes.txt")

#Esto separa los puertos hemos introducido por consola
#ports = ports.split(",")
#Nos dice la cantidad de puertos guardados en el array ports
#print(f"Se escanearan{len(ports)} puertos para la IP: {host}")
for host in hosts:
    for port in ports:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, int(port)))
        if result == 0:
            print(f"El puerto {port} está abierto en el host {host}")
        else:
            print(f"El puerto {port} esta cerrado en el host {host}")
        sock.close()


