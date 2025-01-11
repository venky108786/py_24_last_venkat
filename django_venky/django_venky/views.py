from django.http import HttpResponse

def landing_page(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <title>Coffee Day</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .background {
            background-image: url('https://images.unsplash.com/photo-1511920170033-f8396924c348');
            height: 80vh;
            width: 70vw;
            background-size: cover;
            background-position: center;
            margin: auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        h1 {
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            text-align: center;
            font-size: 3rem;
        }
        .button{
        border-radius: 10px;
            background-color: skyblue;
            color: white;
            padding: 10px 20px;
            border: none;
            flex-direction:center;
            justify-content: center;
             cursor: pointer;"
    </style>
</head>
<body>
    <div class="background">
        <h1>COFFEEDAY</h1>
        <button class="button">click here to order</button>
    </div>
</body>
</html>
''')
