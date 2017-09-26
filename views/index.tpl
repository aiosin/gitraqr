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
                    <h2 class="issuetitle" >{{item[2]}} {{ item[0] }}</h2>
                    <p class="issueage" > {{item [3]}} time ago </p> 
                    <p class="issuedescr"> {{item[1]}}</p> 
                </li>
                
            {% endfor %}
        </ul>
    </main>
</body>