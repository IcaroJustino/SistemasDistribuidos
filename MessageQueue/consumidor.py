import pika

# Conecta-se ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='fila_de_notificacoes')  # declaração da fila


# Função que atua como consumidor, recebendo mensagens da fila
def callback(ch, method, properties, body):
    print("Mensagem recebida:", body.decode())


# Define o consumidor
channel.basic_consume(queue='fila_de_notificacoes',
                      on_message_callback=callback, auto_ack=True)

# Inicia o consumo de mensagens
print("Aguardando mensagens...")
channel.start_consuming()

connection.close()
