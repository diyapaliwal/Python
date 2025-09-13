def http_status(status):
    match status:
        case 200:
            return "Ok"
        
        case 404:
            return "Not Found"
        
        case 500:
            return "Internal Server Error"
        
        case _:
            return "Unknown Status"
        
# Usage
print(http_status(200))
print(http_status(500))
print(http_status(100))
print(http_status(404))