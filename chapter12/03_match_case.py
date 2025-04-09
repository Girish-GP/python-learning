#mase case is similar to switch case in another language
def check_http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal server error"
        case _: #default case
            return "Unknown status"
        
print(check_http_status(200)) #ok
print(check_http_status(404)) #Not found
print(check_http_status(500)) #Internal server error
print(check_http_status(2003)) #Unknown status