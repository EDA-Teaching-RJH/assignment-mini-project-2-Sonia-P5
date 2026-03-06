txt_data="I Like pizza"
file_path="output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file path} was created")
