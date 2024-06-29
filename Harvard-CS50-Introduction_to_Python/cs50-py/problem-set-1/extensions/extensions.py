def main():
    out_var = input("File name: ")

    file_name = out_var.lower().strip()

    mime_type = extensions(file_name)
    
    print(mime_type)

































def extensions(filename):

    allowed_extensions = (".gif", ".jpg", ".jpeg", ".png", ".pdf", ".zip", ".txt") #makes conditionals much shorter and more convenient to access

    if filename.endswith(allowed_extensions):
        suffix = filename.split(".")[-1]

        match suffix:
            case "jpg" | "jpeg" :
                return ("image/jpeg")

            case "gif" | "png" :
                return (f"image/{suffix}")

            case "pdf" | "zip":
                return (f"application/{suffix}")

            case "txt":
                return ("text/plain")

    else:
        return ("application/octet-stream")




main()
