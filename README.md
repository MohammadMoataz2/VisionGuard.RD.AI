# AI Vision: Personalized User Experiences Using Computer Vision and AI

## Authors

- [Mohammad Moataz](https://github.com/MohammadMoataz2)
- [Masa Aladwan](https://github.com/MasaAladwan)


AI Vision is a cutting-edge project aimed at delivering personalized user experiences through the integration of advanced computer vision, machine learning, and microservices. By analyzing real-time user attributes like age, gender, race, and emotions, this platform provides tailored recommendations for products, services, and content. The system is implemented with a robust tech stack to address challenges in retail, advertising, and online services.


![image](https://private-user-images.githubusercontent.com/123085286/400205196-93778a97-9b20-4ff4-a358-2c762368e85b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODYxMzgsIm5iZiI6MTczNjA4NTgzOCwicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA1MTk2LTkzNzc4YTk3LTliMjAtNGZmNC1hMzU4LTJjNzYyMzY4ZTg1Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDAzNThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jNjQzMGE4MWFkZmZkMjNmYjIxYThmOTRlNGEwZWFlMDFkZTRjNDJlM2Q2ZThiZjZhYzA4MjUyZWM2YWM0Zjg2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.yx2WLAe-yLRlCiKXjxDx7YwwknWO8BzN7_Ie1rUMGHI)




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

![image](https://private-user-images.githubusercontent.com/123085286/400205506-e1d59a60-0b5e-4204-87c3-826fe66c71b6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODYzMzIsIm5iZiI6MTczNjA4NjAzMiwicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA1NTA2LWUxZDU5YTYwLTBiNWUtNDIwNC04N2MzLTgyNmZlNjZjNzFiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDA3MTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05NWZkZGZkZDE2ZjVlMjUzMGNkZDQyY2JjYjEzOGQ1YThmZTI5MmE3NDRkZTQ0OWNhMTQ3NDY4MjUwNTAzZWYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.kWeGEqsdAnNybSNfPYuVycgMJuftkPeyUiZtjLYZ8ZU)

## **Frontend Framework:** Reflex (for dynamic web apps)

![image](https://private-user-images.githubusercontent.com/123085286/400205699-4484dd2d-8bdb-48ff-ad16-f58f378d7c70.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY1MzYsIm5iZiI6MTczNjA4NjIzNiwicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA1Njk5LTQ0ODRkZDJkLThiZGItNDhmZi1hZDE2LWY1OGYzNzhkN2M3MC5qcGVnP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDEwNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMDVUMTQxMDM2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZmZkYzlmNmFiNGMwNTJjZDlkOTJjZTA2MzZlMDY3ODI3NDc0Mjk0NTdjZWMwY2M0Zjk4NjZlZWY0MGYwNTljZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.uXFQfRmkYPIDRNt6yuGGJoI5-EnZ2dLReioGhl64r7U)

## **Database:** MongoDB, Redis
![image](https://private-user-images.githubusercontent.com/123085286/400205823-24fe7e29-5078-43a8-bf2d-3f2e2f35327d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY2NTcsIm5iZiI6MTczNjA4NjM1NywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA1ODIzLTI0ZmU3ZTI5LTUwNzgtNDNhOC1iZjJkLTNmMmUyZjM1MzI3ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDEyMzdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05ZTcyMzQ4YWQ3YjIxMjBkY2VlOWE2MGM0Mzc2N2UyM2QyMDEwYmRmZTJmYTczZThhNDUzZDdhZmJlMjU1YTMyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ITO8cleCXcSsIOZsjCrmPJa6YoQJI7mMDGvmUe_Ocw0)


![image](https://private-user-images.githubusercontent.com/123085286/400205885-46461dcd-9225-4f86-9d1f-10a809c44df3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY3MDgsIm5iZiI6MTczNjA4NjQwOCwicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA1ODg1LTQ2NDYxZGNkLTkyMjUtNGY4Ni05ZDFmLTEwYTgwOWM0NGRmMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDEzMjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05NDg2NDU1N2UwNjg0YjRiZGVkMjIzMjkyMDE5ZDdhYTBkOTdlZjNiZjk3MWNiZjFjYzY5OGEzYzJmZmVjNjEwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2SbPD1Ax2i6rIZcqtwJmo88Dj3vFiZrhpE73TH6X8kM)

![image](https://private-user-images.githubusercontent.com/123085286/400205955-e00d7d83-7598-4526-a218-76d7dc78a397.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY3NzgsIm5iZiI6MTczNjA4NjQ3OCwicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA1OTU1LWUwMGQ3ZDgzLTc1OTgtNDUyNi1hMjE4LTc2ZDdkYzc4YTM5Ny5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDE0MzhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNmM2Zjg4NzJkZjI1OWM2YTMzYWJmMTU4YTgwODI1MzA3MWNmYmYxM2ZkODgxYjUzYmUwZjI5NTE4OGZhOTUwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.zHa4JvatxLG6eeBQatKTQEZS_K3h0WyfVJeUMBb6otc)

## **Computer Vision:** OpenCV, DeepFace



## **Machine Learning Models:** Hugging Face (NLP), Custom Models
## **MLOps:** MLflow, MinIO, MySQL

![image](https://private-user-images.githubusercontent.com/123085286/400206087-cc333438-4c97-4b77-aa4e-ab3478934f10.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY4OTcsIm5iZiI6MTczNjA4NjU5NywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA2MDg3LWNjMzMzNDM4LTRjOTctNGI3Ny1hYTRlLWFiMzQ3ODkzNGYxMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDE2MzdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00YjU4NWZmZGUyZDMzNTEzMGFjMTFhYjcxOWFkODQxODdkZjhkYjBjNjQxM2ZhZTBiMTM3YmEzMWNhYTVkY2ZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ot5cXnwqcmrjASXoUPxQbpssdPPXfO5h1I50Y9-U6Ds)

![image](https://private-user-images.githubusercontent.com/123085286/400206167-6e2465be-97b0-48ac-83fb-acfa19b02021.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY5NzMsIm5iZiI6MTczNjA4NjY3MywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA2MTY3LTZlMjQ2NWJlLTk3YjAtNDhhYy04M2ZiLWFjZmExOWIwMjAyMS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDE3NTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNDE5MzZhMzczNzBjMzkzMGE4ZTkwZjU3OWYwM2I5ZjZiYWYxZWFkZmI4MmUzNTI5Mjc4MWM4Y2YzZDY4MDA0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.H0WFGMqme72WvL7pM3-X_xu0DnEqnaAKZCjHsACOx-M)

## **Deployment:** Docker, Microservices

![image](https://private-user-images.githubusercontent.com/123085286/400206018-350d29ae-0ccc-4bde-8db6-d66073925b09.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYwODY4NDMsIm5iZiI6MTczNjA4NjU0MywicGF0aCI6Ii8xMjMwODUyODYvNDAwMjA2MDE4LTM1MGQyOWFlLTBjY2MtNGJkZS04ZGI2LWQ2NjA3MzkyNWIwOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwNVQxNDE1NDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYTFkNDU0YjdlMjhkY2MzM2MzMjQ5YTQ3YTc4OGJiNDFkNzdmZTMwMGViZDFmNzJkZjQxODVkM2MyMjU2OThhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Lgnk-As13QHBCbvSyI6_tn99iAAgFN8FB80T559BavI)




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
