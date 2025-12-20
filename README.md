# service-oriented-system

## Overview

This project is a **minimal infrastructure-focused application** built to practice:

- Docker
- Docker Compose
- Nginx (reverse proxy)
- Python (as a backend program)
- SQL database (PostgreSQL)


The goal is to understand how services communicate in a real-world setup.

---

## Architecture

Client (curl / browser)
        ↓
      Nginx
        ↓
   Python App (Flask)
        ↓
     PostgreSQL


- **Nginx** receives requests and forwards them
- **Python app** listens on a port and returns text
- **Database** stores and responds to SQL queries
- **Docker Compose** connects everything together

---

## Technologies Used

- Docker
- Docker Compose
- Nginx
- Python 3
- Flask (minimal usage)
- PostgreSQL
- SQL

---


## Prerequisites
- Docker Desktop (or Docker Engine + Docker Compose)

## Installation

- Clone the repository with : git clone https://github.com/elhadi-zertal/service-oriented-system.git
                              cd service-oriented-system

- Start the services with : docker-compose up --build

- The system will:

Build the Python backend image

Start PostgreSQL with initial data

Start Flask backend

Start Nginx reverse proxy

## Testing the Service

- Test Nginx is responding: curl http://localhost:8080/
- Test backend health through Nginx: curl http://localhost:8080/health
- Retrieve all logs: curl http://localhost:8080/api/logs
- Add a new log entry: curl -X POST http://localhost:8080/api/log/test-service
- View all log data: docker-compose exec postgres psql -U postgres -c "SELECT * FROM system_logs ORDER BY created_at DESC;"
