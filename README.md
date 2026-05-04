# 🚀 BPCL Dealer Management & Safety Portal

A production-ready **microservices-based web application** designed for managing BPCL dealers, safety rules, and complaint tracking.

---

## 🏗️ Architecture

This project follows a **Microservices Architecture** with API Gateway pattern:

* **Frontend** → Nginx (Static UI)
* **API Gateway** → Nginx Reverse Proxy
* **Backend Services (Flask)**:

  * Dealer Service
  * Complaint Service
  * Auth Service
* **Database** → MySQL (Containerized)

---

## 📁 Project Structure

```
bpcl-portal/
│
├── frontend/
├── gateway/
├── services/
│   ├── dealer-service/
│   ├── complaint-service/
│   ├── auth-service/
│
├── docker-compose.yml
├── .env.example
├── .dockerignore
└── README.md
```

---

## ⚙️ Features

* 🔐 Email-based Login (restricted to @bharatpetroleum.in)
* 📊 Dashboard UI
* 🛢️ Dealer List with Search
* 🛡️ Safety Rules Section
* 📝 Raise Complaint
* 📌 Complaint Tracking System

---

## 🐳 Docker Setup

### Step 1: Clone Repository

```
git clone <your-repo-url>
cd bpcl-portal
```

### Step 2: Create .env file

```
cp .env.example .env
```

Update values in `.env`:

```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=bpcl
MYSQL_USER=bpcluser
MYSQL_PASSWORD=bpclpass
```

---

### Step 3: Run Application

```
docker-compose up -d --build
```

---

## 🌐 Access Application

Open browser:

```
http://<VM-IP>
```

Example:

```
http://20.11.9.25
```

---

## 🔐 Security

* Database port not exposed
* Environment variables used for secrets
* Nginx secure headers configured
* Microservices isolation via Docker network

---

## 📦 Services Overview

| Service           | Description           |
| ----------------- | --------------------- |
| frontend          | UI served via Nginx   |
| gateway           | Reverse proxy routing |
| dealer-service    | Dealer data APIs      |
| complaint-service | Complaint APIs        |
| auth-service      | Email validation      |

---

## 🧠 DevOps Concepts Used

* Docker & Docker Compose
* Microservices Architecture
* API Gateway Pattern
* Environment Configuration
* Container Networking
* Reverse Proxy (Nginx)

---

## 🚀 Deployment (Azure VM)

1. SSH into VM:

```
ssh azurerm@<VM-IP>
```

2. Install Docker:

```
sudo apt update
sudo apt install docker.io docker-compose -y
```

3. Clone repo:

```
git clone <your-repo-url>
cd bpcl-portal
```

4. Run:

```
docker-compose up -d --build
```

---

## 📌 Future Enhancements

* CI/CD using Azure DevOps
* Kubernetes deployment
* Role-based authentication
* Logging & Monitoring (Prometheus + Grafana)

---

## 👨‍💻 Author

DevOps Engineer | Azure | Docker | Microservices

---

## ⭐ Note

This project is built for **learning + interview demonstration + real-world deployment practice**.
