text = input("File name: ").strip().lower()

# print(text.endswith(".gif"))

if text.endswith(".gif"):
    print("image/gif")
elif text.endswith(".jpg") or text.endswith(".jpeg"):
    print("image/jpeg")
elif text.endswith(".png"):
    print("image/png")
elif text.endswith(".pdf"):
    print("application/pdf")
elif text.endswith(".txt"):
    print("text/plain")
elif text.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")