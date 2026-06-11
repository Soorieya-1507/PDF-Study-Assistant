# 📚 AI PDF Assessment Generator

An AI-powered educational tool that automatically generates assessment questions from uploaded PDF study materials using a local Large Language Model (LLM) through Ollama.

The system extracts content from PDF documents, analyzes the study material, generates exam-oriented questions, and serves as a foundation for automated assessment creation and Google Forms integration.

---

## 🚀 Features

### Current Features

* PDF Upload using Streamlit
* PDF Text Extraction
* Local AI Processing using Ollama
* Automatic Question Generation
* Exam-Oriented Question Creation
* No API Key Required
* Fully Offline AI Processing

### Planned Features

* Multiple Question Types

  * MCQs
  * Short Answer Questions
  * Long Answer Questions

* Difficulty Levels

  * Easy
  * Medium
  * Hard

* Question Bank Generation

* Assessment Export

* Google Forms Automation

* Student Assessment Distribution

* Result Collection and Analytics

---

## 🎯 Problem Statement

Teachers and educators often spend significant time preparing assessments from study materials.

This project automates the process by:

1. Reading PDF study materials
2. Understanding the content using AI
3. Generating assessment questions
4. Preparing assessments automatically

The future version will directly create Google Forms for student evaluations.

---

## 🏗️ System Architecture

```text
Teacher Uploads PDF
        │
        ▼
PDF Text Extraction
        │
        ▼
Content Processing
        │
        ▼
Ollama (Llama 3.2)
        │
        ▼
Question Generation
        │
        ▼
Assessment Creation
        │
        ▼
Google Forms Automation
        │
        ▼
Assessment Link
```

---

## 🛠️ Technologies Used

| Technology   | Purpose             |
| ------------ | ------------------- |
| Python       | Backend Development |
| Streamlit    | User Interface      |
| Ollama       | Local LLM Runtime   |
| Llama 3.2    | Question Generation |
| PyPDF        | PDF Text Extraction |
| Git & GitHub | Version Control     |

---

## 📂 Project Structure

```text
PDF-Question-Generator/
│
├── app.py
│
├── uploads/
│
├── generated_questions/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/pdf-question-generator.git

cd pdf-question-generator
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download Ollama:

https://ollama.com

Install Llama 3.2 Model

```bash
ollama pull llama3.2
```

Verify Installation

```bash
ollama run llama3.2
```

If the model responds, installation is successful.

---

## ▶️ Run Application

Start Ollama

```bash
ollama serve
```

Open another terminal

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

## 📖 Usage

1. Upload a PDF study material.
2. Click "Generate Questions".
3. AI extracts important concepts.
4. Questions are generated automatically.
5. Questions are displayed in the Streamlit interface.

---

## 📋 Sample Output

```text
1. Explain Optical Fiber Communication.

2. What are the advantages of Fiber Optics?

3. Describe the working principle of LASER.

4. Explain Total Internal Reflection.

5. Compare Single Mode and Multi Mode Fibers.

6. What is Numerical Aperture?

7. Explain Wavelength Division Multiplexing.

8. Discuss Optical Losses in Fiber.

9. Explain Fiber Optic Sensors.

10. Describe applications of LASER technology.
```

---

## 🔮 Future Enhancements

### Phase 1

* MCQ Generation
* Question Bank Storage
* Download Questions

### Phase 2

* Bloom's Taxonomy Question Generation
* Chapter-wise Assessment Generation
* Difficulty-based Question Generation

### Phase 3

* Google Forms API Integration
* Automatic Form Creation
* Student Assessment Links
* Response Collection

### Phase 4

* AI-Based Answer Evaluation
* Performance Analytics Dashboard
* Personalized Learning Recommendations

---

## 🎓 Educational Applications

* Schools
* Colleges
* Universities
* Online Learning Platforms
* Competitive Exam Preparation

---

## 📈 Learning Outcomes

This project demonstrates:

* Python Programming
* PDF Processing
* Generative AI
* Large Language Models
* Streamlit Development
* Prompt Engineering
* Educational Technology
* AI Automation

---

## 👨‍💻 Author

Developed as a Mini Project for Educational Assessment Automation using Artificial Intelligence and Large Language Models.

---

## ⭐ Future Vision

Transform static study materials into intelligent assessments automatically, reducing manual effort for educators and enabling scalable AI-powered learning experiences.
