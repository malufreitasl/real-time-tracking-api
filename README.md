# Real-time Tracking API Challenge

This challenge involves accessing and processing data from a real-time tracking system for industrial vehicles. The system tracks the position of a logistic train identified by a gateway_id and the position is further identified by a beacon_id. For more information, access [Azitek's Milk Run website](https://azitek.io/milk-run).

The application fetches data from the real-time tracking system's API using the provided API key and processes it to generate the required information and graph. The generated graph is saved as average_time_chart.png in the project directory.

## Challenge Summary

The challenge is to access data from the API and accomplish the following tasks:

1. Access data for the shifts from 10:00 to 17:00 on November 17th and 18th, 2023;
2. Count the number of occurrences of each beacon_id during these shifts;
3. Calculate the average time spent in each position. The unit duration in each position is calculated as last_seen_at - seen_at;
4. Generate a graph using Matplotlib;
5. Run the application in a Docker container.

## Requirements

- Python 3.12
- Docker

## Getting Started

1. Clone this repository:

```
bash git clone https://github.com/your-username/real-time-tracking-api.git
```

2. Navigate to the project directory:

```
cd real-time-tracking-api
```

3. Set up the Docker container:

```
docker build -t tracking-api .
```

4. Run the Docker container:

```
docker run -d -p 80:80 -e API_KEY=YOUR_API_KEY tracking-api
````

Replace YOUR_API_KEY with your API key

## File Structure
- **app/main.py**: Main file containing the FastAPI application setup
- **app/controllers/gateway_controller.py**: Controller for handling HTTP requests related to the gateway
- **app/repositories/gateway_repository.py**: Repository for fetching data from the API
- **app/services/gateway_service.py**: Service for processing data and generating the graph
- **Dockerfile**: Configuration file for building the Docker image
- **requirements.txt**: List of Python dependencies

## Contribution
Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. We welcome any feedback or suggestions for improvement.