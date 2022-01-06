def status_code(code):
    match code:
        case 200: return "OK"
        case 404: return "Not Found"
        case _: return "Unknown"