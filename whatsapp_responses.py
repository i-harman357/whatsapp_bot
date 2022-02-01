def response(input_message):
    message = input_message.lower()

    if message == 'nice':
        return 'thanks'
    elif message == 'hello':
        return 'Hello'
    elif message == 'aur suna':
        return 'sab badia'
    elif message == 'hi':
        return 'hi'
    elif message == 'thank you':
        return 'your welcome'
    else:
        return 'ok'