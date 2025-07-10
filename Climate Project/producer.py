import requests
import json
from kafka import KafkaProducer
import time
from datetime import date

# Define Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define states + coordinates
states = {
    'Delhi': {'lat': 28.6139, 'lon': 77.2090},
    'Mumbai': {'lat': 19.0760, 'lon': 72.8777},
    'Bengaluru': {'lat': 12.9716, 'lon': 77.5946}
}

# Define start & end dates for last 6 months
start_date = '2024-01-01'
end_date = '2024-06-30'

for state, coords in states.items():
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={coords['lat']}&longitude={coords['lon']}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&hourly=temperature_2m"
    )

    print(f"Requesting: {url}")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        times = data['hourly']['time']
        temps = data['hourly']['temperature_2m']

        for time_str, temp in zip(times, temps):
            record = {
                'state': state,
                'latitude': coords['lat'],
                'longitude': coords['lon'],
                'datetime': time_str,
                'temperature': temp
            }
            producer.send('climate-topic', value=record)
            print(f"Sent: {record}")
            time.sleep(0.1)
    else:
        print(f"Failed for {state}: {response.status_code} | {response.text}")

producer.flush()
producer.close()
