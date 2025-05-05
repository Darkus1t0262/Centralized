# Centralized
This project demonstrates a basic **centralized architecture** using Docker Compose with:

- An **API Service** (Flask) that handles user requests and performs logic directly
- A **Worker Service** that is part of the same system and communicates internally
- Shared communication without message queues — everything is centralized

## 🐳 Docker Images
Images available on Docker Hub:

darkjus/api-service

darkjus/worker-service

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CentralizedArch.git
cd CentralizedArch
```bash
docker-compose up --build

For testing need to do a POST to http://localhost:5000/send-task with JSON like

```bash
{
  "task": "do something important"
}
