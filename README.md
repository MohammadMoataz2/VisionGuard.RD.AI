![image](https://github.com/user-attachments/assets/7d591761-bd83-462e-9748-fc2f1c4146b4)# AI Vision: Personalized User Experiences Using Computer Vision and AI

## Authors

- [Mohammad Moataz](https://github.com/MohammadMoataz2)
- [Masa Aladwan](https://github.com/MasaAladwan)


AI Vision is a cutting-edge project aimed at delivering personalized user experiences through the integration of advanced computer vision, machine learning, and microservices. By analyzing real-time user attributes like age, gender, race, and emotions, this platform provides tailored recommendations for products, services, and content. The system is implemented with a robust tech stack to address challenges in retail, advertising, and online services.


![image](![image](https://github.com/user-attachments/assets/a387d0d9-4bc3-40bf-86f0-7fa59bee43f9)
)




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

![image](![image](https://github.com/user-attachments/assets/285df6f1-9605-48df-bd55-c0300820aba7)
)

## **Frontend Framework:** Reflex (for dynamic web apps)

![image](![image](https://github.com/user-attachments/assets/2eb72c73-3c14-48f3-b0ce-abc232ad6b80)
)

## **Database:** MongoDB, Redis
![image](![image](https://github.com/user-attachments/assets/a4874939-ae00-4652-b53b-c07ebdefade5)
)


![image](![image](https://github.com/user-attachments/assets/63d45453-d5a2-4537-96be-c31d2e3ec4ae)
)

![image](c)

## **Computer Vision:** OpenCV, DeepFace



## **Machine Learning Models:** Hugging Face (NLP), Custom Models
## **MLOps:** MLflow, MinIO, MySQL

![image](![image](https://github.com/user-attachments/assets/b7fc6241-7d57-4e28-9c3e-2df40142abda)
)

![image](![image](https://github.com/user-attachments/assets/9712713c-2045-4ebd-bea3-78a6a82bb425)
)

## **Deployment:** Docker, Microservices

![image](![image](https://github.com/user-attachments/assets/a2bf61c3-08e0-48f2-b857-b73041bbc1ff)
)




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
