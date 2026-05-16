# Harmonized Middleware Platform

Enterprise-grade middleware platform for Harmonized APIs using Django REST Framework, Python 3.14, and Oracle 23c.

---

# Overview

The **Harmonized Middleware Platform** is designed to act as a translation and orchestration layer between:

- Frontend/API consumers using harmonized specifications
- Existing legacy backend systems

The platform dynamically transforms harmonized API payloads into backend-compatible formats, executes business logic using Python and Oracle PL/SQL, and returns standardized API responses.

---

# Core Objectives

- Build enterprise-grade REST APIs
- Support hybrid Python + Oracle PL/SQL processing
- Dynamically load metadata and mappings into memory
- Create inquiry APIs for backend data retrieval
- Implement enterprise OOP architecture
- Reduce database calls using caching
- Support scalable middleware processing

---

# Features

## RESTful API Middleware
- Django REST Framework APIs
- Modular enterprise architecture
- Scalable API design

---

## Hybrid Processing Engine
Supports:
- Python business logic
- Oracle SQL execution
- Oracle PL/SQL packages/procedures
- Combined orchestration workflows

---

## Dynamic Metadata-Driven Architecture
Configuration is dynamically loaded from Oracle tables.

Examples:
- Field mappings
- Validation rules
- API metadata
- Response mappings
- Feature flags

---

## In-Memory Metadata Cache
High-performance lookup engine using:
- Singleton cache manager
- Dynamic Oracle metadata loading
- Cached mappings
- Reduced DB roundtrips

---

## Inquiry APIs
Supports:
- Account inquiry
- BO inquiry
- Holdings inquiry
- Transaction inquiry
- KYC inquiry
- Bank detail inquiry

---

## Enterprise OOP Design
Implements:
- Repository Pattern
- Service Layer Pattern
- Factory Pattern
- Strategy Pattern
- Singleton Pattern
- Abstract Base Classes

---

## Oracle Integration
- Oracle 23c support
- Oracle connection pooling
- SQL + PL/SQL hybrid execution
- High-performance backend interaction

---

# Technology Stack

| Layer | Technology |
|---|---|
| Backend Framework | Django |
| REST APIs | Django REST Framework |
| Language | Python 3.14 |
| Database | Oracle 23c |
| Oracle Driver | python-oracledb |
| Authentication | JWT |
| Documentation | Swagger/OpenAPI |
| Caching | In-Memory Singleton Cache |
| Containerization | Docker |
| Logging | Python Logging / Loguru |

---

# System Architecture

```text
Frontend / API Consumer
            ↓
Django REST Framework APIs
            ↓
Controller Layer
            ↓
Processor Factory
            ↓
Validation Engine
            ↓
Dynamic Mapping Engine
            ↓
Service Layer
            ↓
Repository Layer
            ↓
Hybrid SQL / PL-SQL Engine
            ↓
Oracle 23c Backend
```

---

# Project Structure

```text
depository_gateway/
│
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── inquiry/
│   │
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── processors/
│   │   ├── validators/
│   │   ├── mappers/
│   │   ├── cache/
│   │   ├── serializers/
│   │   └── urls.py
│   │
│   ├── accounts/
│   ├── transactions/
│   ├── kyc/
│   ├── audit/
│   └── auth/
│
├── common/
│   ├── db/
│   ├── constants/
│   ├── exceptions/
│   ├── responses/
│   └── utils/
│
├── requirements.txt
│
└── docker-compose.yml
```

---

# Metadata-Driven Processing

## Oracle Mapping Table

```sql
CREATE TABLE API_FIELD_MAPPING (
    API_NAME            VARCHAR2(100),
    FIELD_NAME          VARCHAR2(100),
    HARMONIZED_VALUE    VARCHAR2(100),
    BACKEND_VALUE       VARCHAR2(100),
    ACTIVE_FLAG         CHAR(1)
);
```

---

## Example Mapping Data

| API_NAME | FIELD_NAME | HARMONIZED_VALUE | BACKEND_VALUE |
|---|---|---|---|
| ACCOUNT_CREATE | GENDER | MALE | M |
| ACCOUNT_CREATE | GENDER | FEMALE | F |

---

# In-Memory Cache Example

```python
{
    "ACCOUNT_CREATE": {
        "GENDER": {
            "MALE": "M",
            "FEMALE": "F"
        }
    }
}
```

---

# Example API Flow

## Request

```json
{
  "clientId": "C12345",
  "gender": "MALE",
  "accountType": "INDIVIDUAL"
}
```

---

## Mapping Engine Output

```json
{
  "clientId": "C12345",
  "gender": "M",
  "accountType": "I"
}
```

---

## Backend Processing
- Python orchestration
- Oracle SQL
- PL/SQL execution
- Response transformation

---

## Response

```json
{
  "status": "SUCCESS",
  "message": "Account created successfully",
  "data": {
    "accountNumber": "1209988877"
  }
}
```

---

# OOP Design Patterns Used

| Pattern | Purpose |
|---|---|
| Repository Pattern | Database abstraction |
| Service Layer | Business orchestration |
| Factory Pattern | Dynamic processor creation |
| Strategy Pattern | API-specific processing |
| Singleton Pattern | Metadata cache |
| Abstract Base Classes | Common contracts/interfaces |

---

# Example Modules

| Module | Description |
|---|---|
| Account APIs | Account creation/modification |
| Inquiry APIs | Fetch backend data |
| Transaction APIs | Holdings/transactions |
| KYC APIs | KYC processing |
| Mapping Engine | Harmonized transformations |
| Validation Engine | Dynamic validations |
| Audit Module | Request/response logging |

---

# Oracle Connection Pooling

```python
import oracledb

pool = oracledb.create_pool(
    user="username",
    password="password",
    dsn="localhost:1521/FREEPDB1",
    min=2,
    max=10,
    increment=1
)

def get_connection():
    return pool.acquire()
```

---

# Example Inquiry API

## Endpoint

```http
GET /api/inquiry/account/C12345
```

---

## Example Response

```json
{
  "status": "SUCCESS",
  "message": "Data fetched successfully",
  "data": {
    "clientId": "C12345",
    "clientName": "ROHAN",
    "gender": "MALE",
    "status": "ACTIVE"
  }
}
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd depository_gateway
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Django Server

```bash
python manage.py runserver
```

---

# Future Enhancements

- Redis distributed cache
- Kafka/RabbitMQ integration
- Celery async jobs
- Docker/Kubernetes deployment
- API Gateway integration
- Prometheus/Grafana monitoring
- CI/CD pipelines
- Microservice migration

---

# Security

- JWT Authentication
- Request validation
- Exception masking
- Audit logging
- Role-based access control
- Secure Oracle connection handling

---

# Performance Optimizations

- Oracle connection pooling
- In-memory metadata cache
- Reduced DB roundtrips
- Bulk SQL processing
- Efficient repository pattern usage

---

# Target Use Cases

- Depository middleware systems
- Financial API gateways
- Harmonized API processing
- Legacy backend modernization
- Oracle-backed enterprise systems
- BFSI middleware architecture

---

# Development Roadmap

## Phase 1
- Django setup
- Oracle integration
- Inquiry APIs
- Connection pooling

## Phase 2
- Dynamic mappings
- Metadata cache
- Validation engine
- OOP refactoring

## Phase 3
- JWT authentication
- Audit framework
- Swagger/OpenAPI
- Dockerization

## Phase 4
- Async processing
- Redis cache
- Kafka integration
- Monitoring stack

---

# Author

Enterprise Middleware Platform for:
- Harmonized APIs
- Backend Integration
- Oracle-based BFSI Systems

Built using:
- Django REST Framework
- Python 3.14
- Oracle 23c
- Enterprise OOP Architecture
