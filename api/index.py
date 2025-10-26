from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret-for-flash-messages"

TEMPLATE = """
<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
    <style>body{font-family:sans-serif;background:#0f172a;color:white}</style>
  </head>
  <body class="text-center">
    <h1 class="mt-5" data-aos="fade-up">Gia Đình Việt</h1>
    <p data-aos="fade-up" data-aos-delay="200">Website Flask demo trên Vercel</p>
    <a href="https://vercel.com" target="_blank" class="btn btn-light mt-3">Powered by Vercel</a>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
    <script>AOS.init()</script>
  </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, title="Gia Đình Việt")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    flash(f'Cảm ơn {name}! Chúng tôi sẽ liên hệ qua {email}.', 'success')
    return redirect(url_for('index'))
