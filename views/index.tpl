<head>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header>
        <h1 id="overscript">gitraqr</h1>
    </header>
    <main>
        {{variable}}
        <ul>
            {% for item in seq %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    </main>
</body>