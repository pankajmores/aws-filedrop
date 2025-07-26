
# **AWS FileDrop**

AWS FileDrop is a simple Flask-based web app that allows users to upload files from their browser.
Uploaded files are stored directly in an **Amazon S3 bucket**.

It’s a lightweight project ideal for learning **Flask, AWS S3, and EC2 deployment**.

---

## **Features**

* Upload files from any browser
* Files stored in S3 with **timestamped filenames**
* Runs locally or on AWS EC2
* Beginner-friendly and easy to deploy

---

## **Tech Stack**

* **Python 3 + Flask** – Web framework
* **AWS S3** – File storage
* **AWS EC2** – Hosting
* **boto3** – AWS SDK for Python

---

## **Project Structure**

```
aws-filedrop/
├── app.py             # Main Flask app
├── requirements.txt   # Python dependencies
└── README.md
```

*(Do not commit `venv/`)*

---

## **Run Locally**

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/aws-filedrop.git
   cd aws-filedrop
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure AWS credentials:

   ```bash
   aws configure
   ```

   (Use an IAM user with `AmazonS3FullAccess`.)

5. Run the app:

   ```bash
   python app.py
   ```

   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## **Deploy to AWS EC2**

### 1. Launch an EC2 Instance

* Ubuntu 22.04 (Free Tier)
* In **Security Group**, add inbound rule:
  **Custom TCP → Port 8000 → Source 0.0.0.0/0**

### 2. Connect via SSH

```bash
ssh -i "your-key.pem" ubuntu@<EC2-PUBLIC-IP>
```

### 3. Install dependencies on EC2

```bash
sudo apt update
sudo apt install -y git python3-venv
```

### 4. Pull your code

```bash
git clone https://github.com/<your-username>/aws-filedrop.git
cd aws-filedrop
```

### 5. Create virtual environment & install packages

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 6. Attach IAM Role

Attach an **IAM Role with AmazonS3FullAccess** to this EC2 instance.

### 7. Run Flask

```bash
python app.py
```

### 8. Open in browser

```
http://<EC2-PUBLIC-IP>:8000
```

---

## **requirements.txt**

```
flask
boto3
```

---

## **Optional: Public Bucket Policy**

If you want uploaded files to be accessible via direct URLs:

1. Go to **S3 → Bucket → Permissions → Bucket Policy**
2. Add this policy (replace `your-bucket-name`):

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::your-bucket-name/*"
       }
     ]
   }
   ```

---

## **Keep the App Running**

To keep the app running after SSH logout:

```bash
nohup python app.py &
```

Or for production:

```bash
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

---

## **Next Steps**

* Use **Gunicorn + Nginx** for production
* Add a frontend (Bootstrap/React)
* Use **pre-signed URLs** for private file access
* Add HTTPS with AWS Certificate Manager

---

## **License**

This project is for learning purposes.


