from flask import Flask, request, render_template_string
import boto3
from datetime import datetime

app = Flask(__name__)

# Specify region if needed (replace 'ap-south-1' with your bucket region)
s3 = boto3.client('s3', region_name='ap-south-1')

BUCKET = "filedrop-demo-project"  # Must match your exact bucket name

HTML = """
<h2>Upload a File</h2>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="file">
  <button type="submit">Upload</button>
</form>
{% if error %}
<p style="color:red;">Error: {{ error }}</p>
{% endif %}
{% if url %}
<p>Uploaded! <a href="{{ url }}" target="_blank">Open File</a></p>
{% endif %}
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
            print("ERROR:", e)  # Will show full error in EC2 terminal
            error = str(e)
    return render_template_string(HTML, url=url, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
