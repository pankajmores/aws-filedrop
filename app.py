from flask import Flask, request, render_template_string
import boto3
from datetime import datetime

app = Flask(__name__)
s3 = boto3.client('s3')
BUCKET = "filedrop-demo-project"  # replace with your bucket name

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AWS FileDrop</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(120deg, #74ABE2, #5563DE);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background: #fff;
      padding: 30px 25px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
      text-align: center;
      width: 320px;
      animation: fadeIn 0.8s ease;
    }
    h2 {
      margin-bottom: 20px;
      color: #333;
    }
    input[type="file"] {
      margin: 15px 0;
      padding: 6px;
    }
    button {
      background: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s ease;
    }
    button:hover {
      background: #45a049;
    }
    p {
      margin-top: 20px;
    }
    a {
      color: #4CAF50;
      font-weight: bold;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .success {
      color: green;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="card">
    <h2>Upload a File</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file" required>
      <br><br>
      <button type="submit">Upload</button>
    </form>
    {% if url %}
      <p class="success">Uploaded!</p>
      <p><a href="{{ url }}" target="_blank">Open File</a></p>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    url = None
    if request.method == "POST":
        file = request.files['file']
        filename = datetime.now().strftime("%Y%m%d-%H%M%S-") + file.filename
        s3.upload_fileobj(file, BUCKET, filename)
        url = f"https://{BUCKET}.s3.amazonaws.com/{filename}"
    return render_template_string(HTML, url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
