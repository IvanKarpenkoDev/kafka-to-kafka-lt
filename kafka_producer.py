import concurrent.futures
import json
import time
from confluent_kafka.avro import AvroProducer, CachedSchemaRegistryClient
from confluent_kafka import Producer
from config import DEFAULT_CONFIG


class KafkaProducer:
    def __init__(self, config=None):
        self.config = DEFAULT_CONFIG.copy()
        if config:
            self.config.update(config)

        self.schema_registry_client = None
        # if self.config["SCHEMA_REGISTRY_URL"]:
        #     self.schema_registry_client = CachedSchemaRegistryClient({"url": self.config["SCHEMA_REGISTRY_URL"]})
        #     self.value_schema = self.schema_registry_client.get_latest_schema("uce-value")[1]
        #     self.key_schema = self.schema_registry_client.get_latest_schema("uce-key")[1]

        self.producer_config = {
            "bootstrap.servers": self.config["KAFKA_BROKER"],
            "security.protocol": self.config["SECURITY_PROTOCOL"]
        }

        # if self.config["SECURITY_PROTOCOL"] != "PLAINTEXT":
        #     self.producer_config.update({
        #         "sasl.mechanisms": self.config["SASL_MECHANISMS"],
        #         "sasl.username": self.config["SASL_USERNAME"],
        #         "sasl.password": self.config["SASL_PASSWORD"]
        #     })

        # if self.schema_registry_client:
        #     self.producer = AvroProducer(self.producer_config, default_key_schema=self.key_schema,
        #                                  default_value_schema=self.value_schema)
        # else:
        self.producer = Producer(self.producer_config)

    # def _send_message(self, key, value):
    #     if self.schema_registry_client:
    #         self.producer.produce(topic=self.config["KAFKA_TOPIC"], key=key, value=value)
    #     else:
    #         self.producer.produce(topic=self.config["KAFKA_TOPIC"], key=str(key).encode('utf-8'),
    #                               value=str(value).encode('utf-8'))
    #
    # def send_custom_messages(self, messages):
    #     """
    #     messages should be a list of tuples, where each tuple contains (key, value)
    #     """
    #     for key, value in messages:
    #         self._send_message(key, value)
    #     self.producer.flush()

    def gen_msg(self, key, value, iter: int, num_msg: int):
        for _ in range(iter):
            for i in range(num_msg):
                self.producer.produce(topic=self.config["KAFKA_TOPIC"],
                                      key=key,
                                      value=value)
            self.producer.flush()

    # def _generate_messages(self, key, value, num_msg):
    #     return [(key, value) for _ in range(num_msg)]
    #
    # def _send_messages(self, key, value, num_msg):
    #     for _ in range(num_msg):
    #         self.producer.produce(topic=self.config["KAFKA_TOPIC"], key=key, value=value)
    #     self.producer.flush()
    #
    # def gen_msg(self, key, value, iter, num_msg):
    #     self._generate_messages(self, key, value, num_msg)
    #
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         futures = [executor.submit(self._send_messages, key, value, num_msg) for _ in range(iter)]
    #         concurrent.futures.wait(futures)
