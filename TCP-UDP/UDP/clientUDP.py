import socket

HOST = 'localhost'
PORT = 5011
HEADER = 1024  # Padrão do tamanho da mensagem
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
measure = 10.0
client.sendto(str(measure).encode('utf-8'), (HOST, PORT))

# Recebe as conversões do servidor e exibe na tela
data, addr = client.recvfrom(HEADER)
print(data.decode('utf-8'))

# Fecha a conexão
client.close()
