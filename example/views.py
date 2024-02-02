# example/views.py
from datetime import datetime
from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Blog</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }}

            header {{
                background-color: #007bff;
                color: #fff;
                text-align: center;
                padding: 1em 0;
            }}

            section {{
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}

            h1 {{
                color: #333;
            }}

            p {{
                color: #555;
            }}

            footer {{
                background-color: #007bff;
                color: #fff;
                text-align: center;
                padding: 1em 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }}
        </style>
    </head>

    <body>
        <header>
            <h1>Welcome to Buddhiraj's vercel</h1>
        </header>

        <section>
            <h1>Blog Post 1</h1>
            <p>This is the content of the first blog post. Kil the fucker with a sword.</p>
            <p>Posted Time : { now } |</p>
        </section>

       

        <!-- Add more blog posts as needed -->

        <footer>
            &copy; {now.year} My Blog
        </footer>
    </body>

    </html>
    '''
    return HttpResponse(html)

