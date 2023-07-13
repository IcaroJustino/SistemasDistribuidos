import socket

HOST = 'localhost'
PORT = 5011
HEADER = 1024  # Padrão do tamanho da mensagem
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

# Define as conversões de medidas


def meterstoKM(measure):
    return measure / 1000.0


def metersToMM(measure):
    return measure * 1000.0


def metersToCM(measure):
    return measure * 100.0


# Aguarda por conexões e processa os dados recebidos
print(f"Aguardando conexões em {HOST}:{PORT}...")

while True:
    # Recebe a medida em metros
    data, addr = server.recvfrom(HEADER)
    measure = float(data.decode('utf-8'))

    # Realiza as conversões
    km = meterstoKM(measure)
    mm = metersToMM(measure)
    cm = metersToCM(measure)

    # Retorna as conversões para o cliente
    message = f"{km:.2f}km\n{mm:.2f}mm\n{cm:.2f}cm".encode('utf-8')
    server.sendto(message, addr)
