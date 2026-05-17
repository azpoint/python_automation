import fitz

with fitz.open("input/students.pdf") as file:
    # page1 = file[0].get_text()
    # print(page1)
    text = ""
    for page in file:
        # print(30 * "-")
        text = text + page.get_text()
        print(text)
