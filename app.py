from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        job = request.form.get("job", "").lower()

        words = ["pay money", "registration fee", "easy money", "work from home"]
        result = "⚠️ FAKE JOB" if any(w in job for w in words) else "✅ GENUINE JOB"

    return f"""
    <html>
    <head><title>Fake Job Detection</title></head>
    <body style="text-align:center;font-family:Arial">
        <h1>Fake Job Detection</h1>
        <form method="post">
            <textarea name="job" rows="8" cols="35"
            placeholder="Enter job description"></textarea><br><br>
            <button type="submit">Check Job</button>
        </form>
        <h2>{result}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
