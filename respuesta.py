commands = {
    "/ping" : "pong"
}

def Respuesta(request):
    for command in commands.keys():
        if request["message"] in command:
            return commands[command]
        else:
            return None