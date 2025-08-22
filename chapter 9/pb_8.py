with open('./chapter 9/file.txt', 'r') as file:
    content = file.read()

    with open('./chapter 9/file_copy.txt', 'w') as file:
        file.write(content)
    print("File copied successfully.")