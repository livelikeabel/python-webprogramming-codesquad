class Text:
    def __init__(self, str): #생성자
        self.text = str

    def __str__(self):  # str메소드 오버라이딩
        return "Object: " +  self.text

t = Text("This is some text")
print(t)
print(t.text)
