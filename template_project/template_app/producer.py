import kafka 


def test_msg_write(msg):
	
	TOPIC_NAME = 'test'
	KAFKA_SERVER = 'localhost:9092'

	producer=kafka.KafkaProducer(bootstrap_servers = KAFKA_SERVER, value_serializer=str.encode)
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg
	#msg = bytes(msg, 'utf-8')
	producer.send(TOPIC_NAME, msg)

	producer.close()
	msg = "[MSG FROM SERVER] el mje se envio correctamente."
	#print (msg)

	return msg


def msg_seguir_usuario(seguidor,seguido):
	
	TOPIC_NAME = seguido+"_Seguidores"
	KAFKA_SERVER = 'localhost:9092'

	producer=kafka.KafkaProducer(bootstrap_servers = KAFKA_SERVER, value_serializer=str.encode)
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg
	#msg = bytes(msg, 'utf-8')

	msg = seguidor+" ahora te esta siguiendo!"

	producer.send(TOPIC_NAME, msg)
	#producer.flush()

	producer.close()
	msg_r = "[MSG FROM KAFKA] msg enviado correctamente"
	#print (msg_r)

	return msg_r


def msg_like_post(seguidor,seguido,title):
	
	TOPIC_NAME = seguido+"_Likes"
	KAFKA_SERVER = 'localhost:9092'

	producer=kafka.KafkaProducer(bootstrap_servers = KAFKA_SERVER, value_serializer=str.encode)
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg
	#msg = bytes(msg, 'utf-8')

	msg = "a "+ seguidor+" le gusto tu post "+ title

	producer.send(TOPIC_NAME, msg)
	#producer.flush()

	producer.close()
	msg_r = "[MSG FROM KAFKA] msg enviado correctamente"
	#print (msg_r)

	return msg_r


def msg_crear_post(idPost, lst_topics):
	
	#TOPIC_NAME = lst_topics
	KAFKA_SERVER = 'localhost:9092'

	producer=kafka.KafkaProducer(bootstrap_servers = KAFKA_SERVER, value_serializer=str.encode)
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg
	#msg = bytes(msg, 'utf-8')

	msg = idPost

	for TOPIC_NAME in lst_topics:
		producer.send(TOPIC_NAME, msg)
	#producer.flush()

	producer.close()
	msg_r = "[MSG FROM KAFKA] msg enviado correctamente"
	#print (msg_r)

	return msg_r