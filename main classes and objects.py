class Student:
    def __init__(self, name, age, track, score):
        self.name = str(name)
        self.age = int(age)
        self.track = [track]
        self.score = float(score)
        
    def change_name(self, replace_name):
        self.name = replace_name
        replace_name = input("What is the name of the new student?: ")
        print(f"The student's name is updated to {replace_name}")
        
    def change_age(self, replace_age):
        self.age = replace_age
        replace_age = input("What is the age of the new student?: ")
        print(f"The student's age is updated to {replace_age} ")
        
    def add_track(self, replace_track):
        self.track = replace_track
        replace_track = input("What is the track of the new student?: ")
        print(f"The student's track is updated to {replace_track}")
        
    def get_score(self, replace_score):
        self.score = replace_score
        replace_score = input("What is the score of the new student?: ")
        print(f"The student's score is updated to {replace_score}")
        

Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(2.5)
