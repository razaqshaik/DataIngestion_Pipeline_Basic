# 🌦️ Climate Data Streaming Dashboard

A **real-time climate data pipeline** that demonstrates modern data streaming architecture using Apache Kafka, Python, MySQL, and Flask.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-2.8+-orange.svg)](https://kafka.apache.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue.svg)](https://www.mysql.com/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

## 📋 Overview

This project showcases a complete data streaming solution for processing and visualizing climate data in real-time. The system ingests weather data through Kafka, stores it in MySQL, and presents it through a dynamic web dashboard.

### 🏗️ Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Producer  │───▶│    Kafka    │───▶│  Consumer   │───▶│   MySQL     │
│             │    │   Broker    │    │             │    │ Database    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                 │
                                                                 ▼
                                                        ┌─────────────┐
                                                        │    Flask    │
                                                        │  Dashboard  │
                                                        └─────────────┘
```

## ✨ Features

- **Real-time Data Processing**: Streams climate data using Apache Kafka
- **Persistent Storage**: Stores data in MySQL for historical analysis
- **Live Dashboard**: Web-based interface with auto-refresh functionality
- **Scalable Architecture**: Designed to handle high-volume data streams
- **Simple Setup**: Easy to deploy and configure

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Apache Kafka 2.8+
- MySQL 8.0+
- Java 8+ (for Kafka)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd climate-data-streaming-dashboard
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**
   ```sql
   CREATE DATABASE climate_db;
   USE climate_db;
   
   CREATE TABLE climate_data (
       id INT AUTO_INCREMENT PRIMARY KEY,
       state VARCHAR(50) NOT NULL,
       latitude FLOAT NOT NULL,
       longitude FLOAT NOT NULL,
       datetime DATETIME NOT NULL,
       temperature FLOAT NOT NULL,
       INDEX idx_datetime (datetime),
       INDEX idx_state (state)
   );
   ```

4. **Configure Kafka**
   ```bash
   # Start Zookeeper
   bin/zookeeper-server-start.sh config/zookeeper.properties
   
   # Start Kafka Server
   bin/kafka-server-start.sh config/server.properties
   
   # Create topic
   bin/kafka-topics.sh --create \
       --topic climate-topic \
       --bootstrap-server localhost:9092 \
       --partitions 3 \
       --replication-factor 1
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_NAME=climate_db
DB_USER=your_username
DB_PASSWORD=your_password

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=climate-topic

# Flask Configuration
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
FLASK_DEBUG=True
```

## 📂 Project Structure

```
climate-data-streaming-dashboard/
├── 📁 src/
│   ├── producer.py          # Kafka producer for climate data
│   ├── consumer.py          # Kafka consumer with MySQL integration
│   └── app.py              # Flask web application
├── 📁 templates/
│   └── index.html          # Dashboard HTML template
├── 📁 static/
│   ├── css/
│   │   └── style.css       # Dashboard styling
│   └── js/
│       └── dashboard.js    # Frontend JavaScript
├── 📁 config/
│   └── database.py         # Database configuration
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── docker-compose.yml     # Docker setup (optional)
└── README.md             # This file
```

## 🏃‍♂️ Running the Application

### Step 1: Start the Consumer
```bash
python consumer.py
```
*This process listens to Kafka and inserts data into MySQL*

### Step 2: Start the Producer (Optional)
```bash
python producer.py
```
*Sends sample climate data to Kafka topic*

### Step 3: Launch the Dashboard
```bash
python app.py
```
*Access the dashboard at http://127.0.0.1:5000*

## 📊 Dashboard Features

- **Real-time Updates**: Auto-refreshes every 5 seconds
- **Latest Data**: Shows the most recent 10 climate records
- **Interactive UI**: Clean, responsive design
- **Data Visualization**: Temperature trends and geographical distribution

## 🛠️ Development

### Adding New Data Sources

1. Modify `producer.py` to connect to your data source
2. Ensure data format matches the expected schema:
   ```json
   {
     "state": "California",
     "latitude": 34.0522,
     "longitude": -118.2437,
     "datetime": "2024-01-15T10:30:00",
     "temperature": 22.5
   }
   ```

### Extending the Dashboard

- Add new visualizations in `templates/index.html`
- Implement AJAX for smoother updates
- Add filtering and search capabilities
- Include additional weather metrics

## 📈 Performance Considerations

- **Kafka Partitions**: Increase partitions for higher throughput
- **Database Indexing**: Optimize queries with proper indexes
- **Connection Pooling**: Use connection pools for database operations
- **Caching**: Implement Redis for frequently accessed data

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Kafka Connection Error**
```bash
# Check if Kafka is running
netstat -an | grep 9092
```

**MySQL Connection Error**
```bash
# Verify MySQL service
systemctl status mysql
```

**Dashboard Not Loading**
- Check if Flask is running on the correct port
- Verify database connection
- Ensure consumer is processing messages

### Support

For issues and questions:
- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/your-repo/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-repo/discussions)

---

<div align="center">
  <p>Built with ❤️ for real-time data processing</p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>