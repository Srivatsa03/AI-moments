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


### 📝 Alternative Text Generation (AI-Powered)  
- When a user uploads an image, **Azure Vision API** generates a description.
- The generated **alt text** is stored in the `alt_text` column of the **Photo model** (`models.py`).
- If a user provides their own description, it **overrides** the AI-generated text.
- The **alt attribute** is automatically added to `<img>` elements for accessibility.

### 🔍 AI-Powered Image Search  
- Each uploaded image is **automatically tagged** using **Azure Vision API**.
- The detected objects are stored as **tags** in the `tags` column of the **Photo model**.
- Users can **search images** using **keywords that match tags**.
- **Example:** Searching "cat" will retrieve all images that contain cats.

## 🎨 User Interface Design Approach  

### 📝 Alternative Text (Automated but Editable)  
- **Default Behavior:** AI automatically generates alt text when an image is uploaded.
- **User Override:** Users can edit the AI-generated alt text if needed.
- **UI Interaction:** The alt-text field is pre-filled but **editable** before publishing.

### 🔍 Image Search (Fully Automated)  
- AI **automatically generates** tags for each image.
- Users can **search by keywords**, and matching images appear instantly.
- **No manual tagging required**—the system processes images in the background.

---

### 🔗 GitHub Repository Link & Commit

📌 GitHub Repo: https://github.com/Srivatsa03/AI-moments

📌 Latest Commit: https://github.com/Srivatsa03/AI-moments/commit/2006584f0c99229a1f8d55fda9ff2f253730823c

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

### 🔎 Verifying AI-Generated Alt Text

To verify the AI-generated alt text, follow these steps:
	•	Inspect the HTML source of an image:
Right-click → Inspect Element and check the <img> tag’s alt attribute.
	•	Use a screen reader:
Alt text will be read aloud for visually impaired users.

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

## ⚠️ Potential Harms & Mitigations

### 1️⃣ 🔍 **Incorrect Image Descriptions**  
- **Issue:** AI may **misidentify objects** and generate inaccurate alt text.
- **Mitigation:** Allow users to **edit** AI-generated descriptions.

### 2️⃣ 🎭 **Bias in AI Recognition**  
- **Issue:** Some AI models may **favor certain demographics** due to biased training data.
- **Mitigation:** Use a **diverse dataset** for AI model training and allow **manual tag corrections**.

### 3️⃣ 📈 **Scalability Concerns**  
- **Issue:** API requests may **slow down** with high traffic.
- **Mitigation:** Implement **batch processing** and **caching**.

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

## ⚙️ Production Challenges & Scalability  

### 🖥️ **Scalability Issues**
- **Problem:** If thousands of users upload images at once, **Azure API calls may slow down**.
- **Solution:** Implement **caching** and **asynchronous processing** for API calls.

### 💰 **Operating Costs**
- **Problem:** Frequent API calls **increase costs** over time.
- **Solution:** Reduce **unnecessary API requests** by storing **AI-generated tags in the database**.

### 🏗 **Infrastructure Scaling**
- **Problem:** Hosting a large number of images **increases storage requirements**.
- **Solution:** Use **AWS S3** or **Azure Blob Storage** instead of local storage.

---


## 📝 Contributors

👤 Srivatsa Kamballa.

📧 skamb10@uic.edu.

🔗 GitHub: https://github.com/Srivatsa03.
