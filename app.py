from flask import Flask, request, render_template_string
import boto3
from datetime import datetime

app = Flask(__name__)

# S3 Configuration
s3 = boto3.client('s3', region_name='ap-south-1')
BUCKET = "filedrop-demo-project"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Uploader</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to right, #667eea, #764ba2);
            color: #fff;
            display: flex;
            height: 100vh;
            align-items: center;
            justify-content: center;
            margin: 0;
        }
        .container {
            background: rgba(0, 0, 0, 0.4);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
            text-align: center;
            width: 100%;
            max-width: 400px;
        }
        h2 {
            margin-bottom: 20px;
        }
        input[type="file"] {
            background: #fff;
            color: #333;
            border: none;
            padding: 10px;
            border-radius: 8px;
            width: 100%;
            margin-bottom: 20px;
        }
        button {
            background-color: #fff;
            color: #333;
            padding: 10px 24px;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background-color: #ddd;
        }
        a {
            color: #ffeb3b;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        p {
            margin-top: 15px;
        }
    </style>
</head>
<body>
  <div class="container">
    <h2>Upload a File</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file" required>
      <br>
      <button type="submit">Upload</button>
    </form>
    {% if error %}
    <p style="color:#f44336;">Error: {{ error }}</p>
    {% endif %}
    {% if url %}
    <p>Uploaded! <a href="{{ url }}" target="_blank">Open File</a></p>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    url = None
    error = None
    if request.method == "POST":
        try:
            file = request.files['file']
            filename = datetime.now().strftime("%Y%m%d-%H%M%S-") + file.filename
            s3.upload_fileobj(file, BUCKET, filename)
            url = f"https://{BUCKET}.s3.amazonaws.com/{filename}"
        except Exception as e:
            print("ERROR:", e)
            error = str(e)
    return render_template_string(HTML, url=url, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
