import socket

host = input("Introduce la Ip a escanear: ")
ports = input("Introduce los puertos a escanear (separados con comas): ")

#Esto separa los puertos hemos introducido por consola
ports = ports.split(",")
#Nos dice la cantidad de puertos guardados en el array ports
print(f"Se escanearan{len(ports)} puertos para la IP: {host}")

for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, int(port)))
    if result == 0:
        print(f"El puerto{port} está abierto")
    else:
        print(f"El puerto {port} esta cerrado")
    sock.close()

