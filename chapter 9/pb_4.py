word = "Donkey"

with open('./chapter 9/file.txt', 'r') as file:
    content = file.read()
    
    new_content = content.replace(word, '######')

    with open('./chapter 9/file.txt', 'w') as file:
        file.write(new_content)
    print("Word replaced successfully.")