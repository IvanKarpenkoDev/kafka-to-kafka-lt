class SendMsg():
    def __init__(self, producer_config=None, msg=None):
        self.producer_config = producer_config
        self.msg = msg


    def gen(self):
        producer = AvroProducer(producer_config, default_key_schema=key_schema, default_value_schema=value_schema)


# def msg(msisdn):
#     key = {"msisdn": msisdn}
#     value = {
#         "msisdn": msisdn,
#         'processingTss': [{'service': 'bd-af-filer', 'ts': int(time.time() * 1000)}],
#         'clientIds': [1],
#         'objectId': '94e62276-dee3-31b5-8bd5-4ef49e0ddb7a',
#         'payload': 0.879
#     }
#     return key, value
#
# def gen(num):
#     schema_registry_props_url = "http://10.72.153.33:8081"
#     sr = CachedSchemaRegistryClient({"url": schema_registry_props_url})
#
#     value_schema = sr.get_latest_schema("uce-value")[1]
#     key_schema = sr.get_latest_schema("uce-key")[1]
#
#     producer_config = {
#         "bootstrap.servers": "10.72.153.173:9094",
#         "schema.registry.url": schema_registry_props_url,
#         "security.protocol": "SASL_PLAINTEXT",
#         "sasl.mechanisms": "SCRAM-SHA-512",
#         "sasl.username": "dev1",
#         "sasl.password": "n7Fvx2DCvkSd"
#     }
#
#     producer = AvroProducer(producer_config, default_key_schema=key_schema, default_value_schema=value_schema)
#     producer.poll(0)
#
#     all_messages = [msg(7_900_000_00_00 + i) for i in range(num)]
#
#     for _ in range(1):
#         for item in all_messages:
#             producer.produce(topic="dev.af.bd-af-filer.uce", key=item[0], value=item[1])
#         producer.flush()`