from flask import Flask, request, render_template_string
import boto3
from datetime import datetime

app = Flask(__name__)
s3 = boto3.client('s3')
BUCKET = "filedrop-demo"  # same as your bucket

HTML = """
<h2>Upload a File</h2>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="file">
  <button type="submit">Upload</button>
</form>
{% if url %}
<p>Uploaded! <a href="{{ url }}" target="_blank">Open File</a></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    url = None
    if request.method == "POST":
        file = request.files['file']
        filename = datetime.now().strftime("%Y%m%d-%H%M%S-") + file.filename
        s3.upload_fileobj(file, BUCKET, filename, ExtraArgs={"ACL": "public-read"})
        url = f"https://{BUCKET}.s3.amazonaws.com/{filename}"
    return render_template_string(HTML, url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
