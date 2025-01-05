# AI Vision: Personalized User Experiences Using Computer Vision and AI

## Authors

- [Mohammad Moataz](https://github.com/MohammadMoataz2)
- [Masa Aladwan](https://github.com/MasaAladwan)


AI Vision is a cutting-edge project aimed at delivering personalized user experiences through the integration of advanced computer vision, machine learning, and microservices. By analyzing real-time user attributes like age, gender, race, and emotions, this platform provides tailored recommendations for products, services, and content. The system is implemented with a robust tech stack to address challenges in retail, advertising, and online services.


![image](https://private-user-images.githubusercontent.com/123085286/400207094-a2bab993-cdaa-4770-b6c2-f77dcd33ff40.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MDk0LWEyYmFiOTkzLWNkYWEtNDc3MC1iNmMyLWY3N2RjZDMzZmY0MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04OTVkZGQ4ZjFkNDU3Y2RkZjhkZjQ1OTY1OWFhYjg3NGI2MzRkZTEzMDllOTUwOGU3YzgxZWQ3YTFlNzFjYmJkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aRmeHsPtZEoHLldvI0g3Qb8KGTqLmhvl4bs6Ad3akeI)




## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [System Workflow](#system-workflow)
- [Project Objectives](#project-objectives)
- [Getting Started](#getting-started)

---

## Introduction
In a fast-paced digital era, personalization is key to enhancing user engagement. AI Vision leverages computer vision and AI to analyze user attributes from live video or images and deliver tailored recommendations. This project bridges the gap in personalization, enabling organizations to create custom solutions for various goals.

---

## Key Features
- **User Attributes Detection:** Analyze age, gender, race, emotions, and other characteristics in real-time.
- **Personalized Ads & Recommendations:** Display tailored ads and search results based on user preferences.
- **Dashboard for Monitoring:** Track user interactions and ad performance.
- **Custom Search & Query:** Refine search results based on user preferences.
- **MLOps Integration:** Manage the ML lifecycle with tools like MLflow and MinIO.
- **Microservices Architecture:** Scalable, modular design based on SOLID principles.

---

## Technology Stack
## **Backend Framework:** FastAPI

![image](https://private-user-images.githubusercontent.com/123085286/400207102-ebaf436d-55af-4e35-8d4f-93b5a08cac85.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTAyLWViYWY0MzZkLTU1YWYtNGUzNS04ZDRmLTkzYjVhMDhjYWM4NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZjM5MzI4OTUzNDE4MjgwODU1NTQ1ZDdiNTcxNjU1ZGIyNTljMzllNTg1MmRjNmVkM2VjODExM2Y4OTAxMjFhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.F28fQNc9YmUxf7Y7GCysPQTBkA3YFvjxVPm8AGcno48)

## **Frontend Framework:** Reflex (for dynamic web apps)

![image](https://private-user-images.githubusercontent.com/123085286/400207107-8865fff8-0e44-4cff-a9a2-d8cf4d037a41.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTA3LTg4NjVmZmY4LTBlNDQtNGNmZi1hOWEyLWQ4Y2Y0ZDAzN2E0MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMjA5OTI3NzA4ZTJkZjMyMDQwY2UwZDNmYTU3OTlkNjhmOWFlODAyYTZiMjdjNzdiYjIzNGU5MzIwODBhNmU0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.bjwQgADP0V99rkMWtuIkkjrCobYcblLb0vLXAjpbDq8)

## **Database:** MongoDB, Redis
![image](https://private-user-images.githubusercontent.com/123085286/400207113-96da17dc-fe82-4fca-bc41-0f135cd2c920.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTEzLTk2ZGExN2RjLWZlODItNGZjYS1iYzQxLTBmMTM1Y2QyYzkyMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kOGQzMGNiODY4YzEzMjE0NjAxMzk0ZGUyZTEwNTVlZTE1MTMzMTgyOTA1ZmFkNDEyZTc3NDEyNTNlYjM4NjI2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.OFUGJLCciSzXZ0WB4jteSDkhaWZGHGcIBofUhlZyXmE)


![image](https://private-user-images.githubusercontent.com/123085286/400207115-ef9b6051-167a-446e-aeba-229d51511a34.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTE1LWVmOWI2MDUxLTE2N2EtNDQ2ZS1hZWJhLTIyOWQ1MTUxMWEzNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNTI2Y2I1MGMyY2M0YjAzNjNmMDA4NWJiY2NmZWNmNTg0ODM4OTAzNzFlOGI4NWVkYjgzNDg0MzYyNGJhZTZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.9j5s1awSlE-JzL6BgnOJj9LEPU3r3cNj1zlKcB9zWvU)

![image](https://private-user-images.githubusercontent.com/123085286/400207120-5860f7f1-a8d4-42f6-9910-8f2572848fe2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTIwLTU4NjBmN2YxLWE4ZDQtNDJmNi05OTEwLThmMjU3Mjg0OGZlMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZTdhNWU5Njk5OGVkNDRmZTU1YjJlOWYyNzNiZWU0NjhlMzQ2ZDkxNzFhMzQ0NTI5NzEyYTQzMjgyODlmNWVkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Vp9Dn8ygdNbBghBcEakJPlEAf06BnWbc71pjnw8HP0I)

## **Computer Vision:** OpenCV, DeepFace



## **Machine Learning Models:** Hugging Face (NLP), Custom Models
## **MLOps:** MLflow, MinIO, MySQL

![image](https://private-user-images.githubusercontent.com/123085286/400207128-6f768b12-187b-4901-a18a-8c530537fd92.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTI4LTZmNzY4YjEyLTE4N2ItNDkwMS1hMThhLThjNTMwNTM3ZmQ5Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kNTU0YzNhY2YyMTlhMjdlN2U0MWQxYjA4MmEyZTc5YjJkNmMzM2E4ZTY5ZGI2MTI3YWI1Y2VkYjBmODA4NTFkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.3s8Q_yrVwHukWQ9-mOA0hbYT6QwmI1OtC4JeS-w7mh0)

![image](https://private-user-images.githubusercontent.com/123085286/400207132-5a5e4d31-091d-4d20-be5e-ec2c9b6127fe.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTMyLTVhNWU0ZDMxLTA5MWQtNGQyMC1iZTVlLWVjMmM5YjYxMjdmZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yNTg5NzY3OTVjYjk5NGQwMzE3N2ExODdmMWY0YTViMjdmMzhlMzRhNTc2MjIwMmM3NjdjNWRjYjk0YTgwZDlhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.OX7LOWLGsaRKrAPJpuQItCIwSu9KvWDT4zche2Oouoo)

## **Deployment:** Docker, Microservices

![image](https://private-user-images.githubusercontent.com/123085286/400207124-5e955a53-ee03-4421-bb0e-2262f85dab15.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODc4MjMsIm5iZiI6MTczNjA4NzUyMywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA3MTI0LTVlOTU1YTUzLWVlMDMtNDQyMS1iYjBlLTIyNjJmODVkYWIxNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDMyMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZWEzNjI5MTE0YjFiODU4ZTE1NDg5MzE5NTUzZGQ2MGU5YzY2MDMxY2Q1Yjc1YzU4MTdhZjQ3Yjg1NTZjZmY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.IfXxlMvV1nvomzi3L0et-lch49yIhqvXHnrwq6as_bo)




---

## Architecture
AI Vision employs a microservices architecture to separate tasks into independent components. Each service handles a specific function, such as image processing, user interactions, or database management. This design ensures scalability, maintainability, and seamless communication between services.

---

## System Workflow
1. **Data Collection:** Capture user data via live video or images.
2. **Feature Analysis:** Detect attributes like age, gender, and emotions using OpenCV and DeepFace.
3. **Recommendation Engine:** Analyze detected attributes and fetch relevant ads or search results.
4. **Caching:** Use Redis for faster response times and reduced database load.
5. **Feedback System:** Continuously refine recommendations based on user interactions.

---

## Project Objectives
1. Detect user characteristics and interests.
2. Provide real-time recommendations.
3. Improve the relevance of ads and search results.
4. Offer customizable solutions for businesses.
5. Apply AI knowledge to real-world challenges.

---

## Getting Started
### Prerequisites
- Python 3.10+
- Docker

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammadMoataz2/VisionGuard.RD.AI.git
   ```
   Update the `.env` file with your configuration.
2. Run the application:
   ```bash
   make
   ```

### Usage
Access the api  at `http://localhost:8000/docs`.
Access the web application at `http://localhost:3000`.
