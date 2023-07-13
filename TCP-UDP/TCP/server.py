import socket

HOST = 'localhost'
PORT = 5005
HEADER = 1024  # Padrão do tamanho da mensagem
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
# Define as conversões de medidas


def meterstoKM(measure):
    return measure / 1000.0


def metersToMM(measure):
    return measure * 1000.0


def metersToCM(measure):
    return measure * 100.0


# Aguarda por conexões e processa os dados recebidos
server.listen()
print(f"Aguardando conexões em {HOST}:{PORT}...")

while True:
    conn, addr = server.accept()  # conexão com o client
    print(f"Conexão recebida")

    # Recebe a medida em measure
    data = conn.recv(HEADER)  # formato padrão da mensagem
    measure = float(data.decode('utf-8'))

    # Realiza as conversões
    km = meterstoKM(measure)
    mm = metersToMM(measure)
    cm = metersToCM(measure)

    # Retorna as conversões para o cliente
    conn.sendall(f"{km:.2f}km\n{mm:.2f}mm\n{cm:.2f}cm".encode('utf-8'))

    # Fecha a conexão
    conn.close()
