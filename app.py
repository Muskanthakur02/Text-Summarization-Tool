from flask import Flask, request, render_template_string
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Text Summarization Tool</title>
<style>
body{
    font-family: Arial;
    background:#f4f6f9;
    text-align:center;
    padding:40px;
}

.container{
    background:white;
    width:70%;
    margin:auto;
    padding:30px;
    border-radius:15px;
    box-shadow:0 0 15px rgba(0,0,0,0.1);
}

textarea{
    width:80%;
    height:150px;
    padding:10px;
    font-size:16px;
}

button{
    background:#007bff;
    color:white;
    border:none;
    padding:12px 25px;
    border-radius:8px;
    cursor:pointer;
    margin-top:10px;
}

button:hover{
    background:#0056b3;
}

.summary{
    margin-top:20px;
    padding:15px;
    background:#eef;
    border-radius:10px;
}
</style>
</head>

<body>

<div class="container">
<h1>AI Text Summarization Tool</h1>

<form method="POST">
<textarea name="text"></textarea><br>
<button type="submit">Summarize</button>
</form>

{% if summary %}
<div class="summary">
<h2>Summary</h2>
<p>{{summary}}</p>
</div>
{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""

    if request.method == "POST":
        text = request.form["text"]
        sentences = sent_tokenize(text)
        summary = " ".join(sentences[:2])

    return render_template_string(HTML, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)