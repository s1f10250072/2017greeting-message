from datetime import datetime

name = "Inoue"

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    main_message = message + name + '-san!'
    
    print(message)
