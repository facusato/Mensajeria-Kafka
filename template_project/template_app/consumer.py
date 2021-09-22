import kafka

#consumer = kafka.KafkaConsumer(TOPIC_NAME)


def test_lst_msg():
	TOPIC_NAME = 'test'
	consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=1000, auto_offset_reset='earliest' ) #lee todos los registros del topic
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg
	#consumer.seek(0, 0)
	lst_msg = []
	for message in consumer:
		#print(message.value)
		string_value_b = str(message.value)
		fin = len (string_value_b)
		string_value = string_value_b[2:fin-1:1]
		lst_msg.append(string_value)


	yield lst_msg


def notifiSeguim_lst_msg(user):
	TOPIC_NAME = user+"_Seguidores"

	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000, auto_offset_reset='earliest', enable_auto_commit=True) #
	consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=1000, auto_offset_reset='earliest' ) #lee todos los registros del topic
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg

	#tp = kafka.TopicPartition(topic=TOPIC_NAME, partition=0)
	#consumer.seek(tp, 0)
	lst_msg = []
	for message in consumer:
		#print(message.value) # type Bytes
		string_value_b = str(message.value) 	#message.value = b'valor'
		fin = len (string_value_b)
		string_value = string_value_b[2:fin-1:1]	#corta la cadena retirando el (b'...')
		lst_msg.append(string_value)

	#consumer.commit(idGroup)

	yield lst_msg


def notifiLikes_lst_msg(user):
	TOPIC_NAME = user+"_Likes"

	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000, auto_offset_reset='earliest', enable_auto_commit=True) #
	consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=1000, auto_offset_reset='earliest' ) #lee todos los registros del topic
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg

	#tp = kafka.TopicPartition(topic=TOPIC_NAME, partition=0)
	#consumer.seek(tp, 0)
	lst_msg = []
	for message in consumer:
		#print(message.value) # type Bytes
		string_value_b = str(message.value) 	#message.value = b'valor'
		fin = len (string_value_b)
		string_value = string_value_b[2:fin-1:1]	#corta la cadena retirando el (b'...')
		lst_msg.append(string_value)

	#consumer.commit(idGroup)

	yield lst_msg




def noticias_lst_msg(user):
	TOPIC_NAME = user+"_News"

	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000, auto_offset_reset='earliest', enable_auto_commit=True) #
	consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=1000, auto_offset_reset='earliest' ) #lee todos los registros del topic
	#consumer = kafka.KafkaConsumer(TOPIC_NAME, consumer_timeout_ms=4000) #lee los enviados mientras esta escuchando esos 4 seg

	#tp = kafka.TopicPartition(topic=TOPIC_NAME, partition=0)
	#consumer.seek(tp, 0)
	lst_msg = []
	for message in consumer:
		#print(message.value) # type Bytes
		string_value_b = str(message.value) 	#message.value = b'valor'
		fin = len (string_value_b)
		string_value = string_value_b[2:fin-1:1]	#corta la cadena retirando el (b'...')
		lst_msg.append(string_value)

	#consumer.commit(idGroup)

	yield lst_msg
