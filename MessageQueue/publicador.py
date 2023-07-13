import pika

# Conecta-se ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila
channel.queue_declare(queue='fila_de_notificacoes')


# publicador, responsavel  mensagens para a fila
def publicador():
    while True:
        mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ")
        if mensagem == "sair":
            break
        channel.basic_publish(
            exchange='', routing_key='fila_de_notificacoes', body=mensagem)
    print("Publicador encerrado.")


if __name__ == "__main__":
    publicador()


connection.close()  # Fecha a conexão com o servidor RabbitMQ
