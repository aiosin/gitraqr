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
                <li>
                    <h2>{{item[2]}} {{ item[0] }}</h2>
                    <p> {{item [3]}} time ago </p> 
                    <p> {{item[1]}}</p> 
                </li>
                
            {% endfor %}
        </ul>
    </main>
</body>