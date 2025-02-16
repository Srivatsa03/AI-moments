# 📸 Moments - AI-Powered Image Sharing

Moments is a Flask-based image-sharing platform that **leverages AI** to automatically generate **alternative text** and **searchable image tags** using **Azure Vision API**.

---

## 🚀 Features

✅ **AI-Generated Alt Text** - Automatically adds descriptions to images for accessibility  
✅ **Smart Image Tagging** - AI identifies objects in images and stores them as searchable tags  
✅ **Image Search** - Users can search images using AI-generated tags  
✅ **Manual Tagging** - Users can manually add or edit tags  
✅ **User Authentication** - Secure user login and profile management  
✅ **Image Uploading & Commenting** - Share and engage with photos  

---

## 🛠 Installation Guide

Follow these steps to set up and run the project locally.

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd moments
```

### 2️⃣ Create a Virtual Environment & Activate It
💻 macOS/Linux:
```bash
python3 -m venv venv  
source venv/bin/activate  
```
🖥 Windows:
```bash
python -m venv venv  
venv\Scripts\activate  
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---

## 🔑 API Key Setup

This project uses Azure Vision API for image processing. Follow these steps to set it up:

### 1️⃣ Sign up for Azure Cognitive Services
•	Go to Azure Portal

•	Create a Computer Vision resource

•	Copy the API Key and Endpoint URL

### 2️⃣ Create a .env file in the root directory and add:
```bash
AZURE_VISION_API_KEY="your-api-key-here"
AZURE_VISION_ENDPOINT="your-endpoint-here"
```
🚨 Do NOT commit your .env file! Keep API credentials secret.

---

## 🚀 Running the Application

Once the setup is complete, start the Flask server:
```
flask run
```
📌 Access the web app at:

👉 http://127.0.0.1:5000

---

## 🖼 Uploading & Searching Images

### 📸 Upload an Image
1.	Click “Upload”
2.	Select an image
3.	AI will generate alt-text and tags automatically

### 🔍 Searching Images
•	Use the search bar to find images by AI-generated tags

•	Example: Searching “cat” will return images with cats

### ✏ Manually Add/Edit Tags
1.	Go to an image page
2.	Click “Add Tags”
3.	Enter a tag and save
4.	
---
### 🎭 Demo Test Account

You can use this test account to explore Moments:

📧 Email: admin@helloflask.com

🔑 Password: moments

---

## 🛠 Technology Stack

🔹 Python & Flask - Backend framework

🔹 SQLAlchemy - Database ORM

🔹 Azure Vision API - AI-powered image recognition

🔹 Bootstrap 5 - Frontend styling

🔹 WTForms - Form handling

🔹 Flask-Login - User authentication

---

### 🛡 Security & Best Practices

✅ No credentials are committed to GitHub.

✅ Uses environment variables for API keys.

✅ Sanitization & validation for user inputs.

---

### 📌 Known Issues & Future Improvements
•	🔧 Optimize API Calls - Batch process images for efficiency.

•	📈 Scalability Enhancements - Migrate to cloud-based infrastructure for better performance.

•	🏷 Better Tag Management - Improve AI tagging accuracy.

---

## 📝 Contributors

👤 Srivatsa Kamballa.

📧 skamb10@uic.edu.

🔗 GitHub: https://github.com/Srivatsa03.
