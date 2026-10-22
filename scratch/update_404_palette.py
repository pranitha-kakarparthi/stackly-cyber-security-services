for path in ['404.html', 'pages/404.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace('background-color: #030508;', 'background-color: #250109;')
    text = text.replace("'rgba(167, 139, 250, ' : 'rgba(94, 234, 212, '", "'rgba(217, 119, 6, ' : 'rgba(190, 18, 60, '")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated palette in {path}")

