# **AWS FileDrop**

A simple Flask web app that allows users to upload files through a web interface.
Uploaded files are stored directly in an **Amazon S3 bucket**.

This project demonstrates:

* Flask web development
* AWS S3 integration
* Hosting on an **AWS EC2 instance**

---

## **Features**

* Upload files from a browser
* Files are stored in S3 with timestamped filenames
* Lightweight and beginner-friendly project
* Can be deployed locally or on EC2

---

## **Tech Stack**

* Python 3 + Flask
* AWS S3 (for file storage)
* AWS EC2 (for deployment)
* boto3 (AWS SDK)

---

## **Project Structure**

```
aws-filedrop/
│
├── app.py             # Main Flask app
├── requirements.txt   # Python dependencies
├── venv/              # Virtual environment (local)
└── README.md
```

---

## **Setup (Local Development)**

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/aws-filedrop.git
cd aws-filedrop
```

2. **Create virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure AWS credentials**

```bash
aws configure
```

(Make sure the IAM user has `AmazonS3FullAccess`.)

5. **Run the app**

```bash
python app.py
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## **Deploying on EC2**

1. Launch an **Ubuntu EC2 instance**.
2. SSH into EC2.
3. Install Git & Python:

```bash
sudo apt update
sudo apt install git python3-venv -y
```

4. **Clone your repo**

```bash
git clone https://github.com/<your-username>/aws-filedrop.git
cd aws-filedrop
```

5. **Create virtual environment and install requirements**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. **IAM Role:** Attach an **IAM Role** to the EC2 instance with `AmazonS3FullAccess`.

7. **Run Flask**

```bash
python app.py
```

8. **Security Group:**
   Open port `8000` in your EC2 Security Group.

Now access it in your browser:

```
http://<EC2-PUBLIC-IP>:8000
```

---

## **Requirements**

`requirements.txt`:

```
flask
boto3
```

---

## **Future Improvements**

* Use Gunicorn + Nginx for production
* Pre-signed URLs for private file access
* Add a frontend UI with Bootstrap or React
* HTTPS using AWS Certificate Manager and Load Balancer

---

## **License**

This project is for learning purposes.

---

Would you like me to also create a **requirements.txt file content**,
and a **bucket policy example for public access**, so that your uploads open directly from the browser?
