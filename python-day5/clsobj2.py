class school:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.SSLC_Mark = int(input("Enter your 10th Mark: "))

    def group(self):
        if self.SSLC_Mark > 500:
            print("You are going to Group1")
            self.stream = "Group1"
        elif 400 < self.SSLC_Mark <= 500:
            print("You are going to Group2")
            self.stream = "Group2"
        elif 300 <= self.SSLC_Mark <= 400:
            print("You are going to Group3")
            self.stream = "Group3"
        else:
            print("Not eligible for any group")
            self.stream = None

        self.HSC_Mark = int(input("Enter your 12th Mark: "))


class college(school):
    def courses(self):
        if self.stream == "Group1" and self.HSC_Mark > 600:
            print("You are eligible to become a Doctor or Engineer")
        elif self.stream == "Group2" and self.HSC_Mark > 500:
            print("You are eligible to become a Nurse or Teacher")
        elif self.stream == "Group3" and self.HSC_Mark > 400:
            print("You are eligible to become a Manager or Accountant")
        else:
            print("Not eligible for selected courses")


# Object creation
student = college()
student.group()
student.courses()
