# 🧩 Nginx Reverse Proxy with Flask Backend and Static Frontend

This project demonstrates how to set up a **secure Nginx reverse proxy** to serve a **Flask backend** and a **vanilla HTML/JS/CSS frontend** running in separate Docker containers.

The setup includes:

- Nginx reverse proxy
- HTTPS using self-signed certificates
- Backend (Flask API)
- Frontend (static HTML/JS/CSS)
- Clean routing (`/api` → backend, `/` → frontend)

---

---

## ⚙️ How It Works

### Nginx Reverse Proxy

- Routes `/api/*` to the **Flask backend** container.
- Routes `/` to the **frontend** container.
- Serves everything securely over **HTTPS (port 443)**.
- Automatically redirects HTTP → HTTPS.

### Backend (Flask)

- A simple API endpoint `/random-color` that returns a random HEX color.
- CORS enabled for local development (can be disabled once proxied via Nginx).

### Frontend (Vanilla JS)

- Displays a button that, when clicked, fetches a random color from the backend.
- Updates the background color dynamically.

---

## 🐳 Docker Compose Overview

### `docker-compose.yml`

- **nginx** — reverse proxy and SSL termination
- **frontend** — static file server (nginx:alpine)
- **backend** — Flask app running on Python Slim

All services are on the same custom bridge network (`app_network`).

---

## 🔧 Setup Instructions

### 1. Generate SSL Certificates

You can generate self-signed certificates with OpenSSL:

```bash
mkdir -p nginx/certs
openssl req -x509 -newkey rsa:4096 -keyout nginx/certs/server.key -out nginx/certs/server.crt -days 365 -nodes -subj "/CN=localhost"
```

### 2. Build and Run Containers

```
docker-compose up --build
```

3. Access the App

- Frontend: https://localhost
- Backend (via proxy): https://localhost/api/random-color

### It would look like this if you have set it up correctly
<img width="1907" height="1009" alt="image" src="https://github.com/user-attachments/assets/21854f7b-24f9-4041-9c74-881d61f4b811" />
