import socket

HOST = 'localhost'
PORT = 5005
HEADER = 1024  # Padrão do tamanho da mensagem
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Envia a medida em measure para o servidor
measure = 100.0
client.sendall(str(measure).encode('utf-8'))

# Recebe as conversões do servidor e exibe na tela
data = client.recv(HEADER)
print(data.decode('utf-8'))

# Fecha a conexão
client.close()
