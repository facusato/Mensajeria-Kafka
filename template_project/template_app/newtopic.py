from kafka.admin import KafkaAdminClient, NewTopic




def crear_topic_seguidores(usuario):

	KAFKA_SERVER = 'localhost:9092'

	admin_client = KafkaAdminClient(bootstrap_servers = KAFKA_SERVER)

	topic_list = []
	name_topic = str(usuario)+"_Seguidores"
	topic_list.append(NewTopic(name=name_topic, num_partitions=1, replication_factor=1))
	admin_client.create_topics(new_topics=topic_list, validate_only=False)

	msg = "[MSG FROM SERVER] el topic "+ name_topic +" se creo correctamente."
	#print (msg)

	return msg