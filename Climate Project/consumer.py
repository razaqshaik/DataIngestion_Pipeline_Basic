from kafka import KafkaConsumer
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import json

# Kafka Consumer
consumer = KafkaConsumer(
    'climate-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# DB connection string
username = "root"
password = quote_plus("razaqsvne@2003")
host = "localhost"
port = "3306"
database = "climate_db"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Insert loop
for message in consumer:
    data = message.value
    print(f"Received: {data}")

    with engine.begin() as connection:
        insert_query = text("""
            INSERT INTO climate_data (state, latitude, longitude, datetime, temperature)
            VALUES (:state, :latitude, :longitude, :datetime, :temperature)
        """)
        # ✅ Pass dict directly — no unpacking!
        connection.execute(insert_query, data)
        print("Inserted into DB ✅")
