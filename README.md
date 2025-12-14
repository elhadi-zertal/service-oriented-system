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

