<head>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header>
        <h1 id="overscript">gitraqr</h1>
        <br> <a href="/random" style="padding-left:30px"> random </a>
    </header>
    <main>
        <ul>
            {% for item in loopdata %}
                <div class='tagcolor{{item[2]}}'>
                   <h2 class="issuetag" >{{item[2]}} </h2>
                </div> 
                <div class='isscontent'>
                    <li>
                        <h3 class="issuetitle" > {{ item[0] }} </h3>
                        <p class="issuedescr"> {{item[1]}}</p> 
                        <a href="{{item[4]}}"> Link to issue </a>
                    </li>
                </div>
            {% endfor %}
        </ul>
    </main>
</body>