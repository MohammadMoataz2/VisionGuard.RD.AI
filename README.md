# AI Vision: Personalized User Experiences Using Computer Vision and AI

## Authors

- [Mohammad Moataz](https://github.com/MohammadMoataz2)
- [Masa Aladwan](https://github.com/MasaAladwan)


AI Vision is a cutting-edge project aimed at delivering personalized user experiences through the integration of advanced computer vision, machine learning, and microservices. By analyzing real-time user attributes like age, gender, race, and emotions, this platform provides tailored recommendations for products, services, and content. The system is implemented with a robust tech stack to address challenges in retail, advertising, and online services.


![image](https://github.com/user-attachments/assets/22fd24f7-02a3-4ce6-a276-f9c1ec897b9d)





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

![image](https://github.com/user-attachments/assets/e5917426-3f9a-4fcb-8c04-dc73d648f9bb)

## **Frontend Framework:** Reflex (for dynamic web apps)

![image](https://github.com/user-attachments/assets/4500b7ee-9dcf-4f9a-80f5-136e776c8af8)

## **Database:** MongoDB, Redis
![image](https://github.com/user-attachments/assets/8c6a1deb-3aaa-47b0-accd-e466f1872528)


![image](https://github.com/user-attachments/assets/3d1c2338-9b9e-4079-8e19-250fd7877c67)

![image](https://github.com/user-attachments/assets/73bb3335-7f6f-440d-9c31-a7cf7d426fc4)

## **Computer Vision:** OpenCV, DeepFace



## **Machine Learning Models:** Hugging Face (NLP), Custom Models
## **MLOps:** MLflow, MinIO, MySQL

![image](https://github.com/user-attachments/assets/79b68d82-60f8-4267-be6d-3b4066e49898)


![image](https://github.com/user-attachments/assets/c1858236-f54f-46a0-b6be-aabf1a1c7fe0)


## **Deployment:** Docker, Microservices

![image](https://github.com/user-attachments/assets/749505bd-0202-40cf-9471-98c1fc88bc6e)




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
