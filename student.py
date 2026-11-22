class Student:
    def __init__(self, student_id: str, full_name: str, department: str, semester: int):
        self.__student_id = student_id
        self.__full_name = full_name
        self.__department = department
        self.__semester = semester
        self.__gpa = 0.0
        self.__enrolled_courses = []

    def register_course(self, course_code: str) -> None:
        if course_code not in self.__enrolled_courses:
            self.__enrolled_courses.append(course_code)
            print(f"[SUCCESS] {self.__full_name} registered for course: {course_code}")
        else:
            print(f"[INFO] {self.__full_name} is already registered for {course_code}")

    def drop_course(self, course_code: str) -> None:
        if course_code in self.__enrolled_courses:
            self.__enrolled_courses.remove(course_code)
            print(f"[SUCCESS] {self.__full_name} dropped course: {course_code}")
        else:
            print(f"[ERROR] Course {course_code} not found in enrolled courses.")

    def update_gpa(self, new_gpa: float) -> None:
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            print(f"[SUCCESS] GPA updated to {self.__gpa:.2f}")
        else:
            print("[ERROR] Invalid GPA. Please enter a value between 0.00 and 4.00.")

    def is_honor_student(self) -> bool:
        return self.__gpa >= 3.00

    def get_student_profile(self) -> None:
        honor_status = "Yes (Honor Student)" if self.is_honor_student() else "No"
        courses_list = ", ".join(self.__enrolled_courses) if self.__enrolled_courses else "None"
        
        print("\n==========================================")
        print("           STUDENT PROFILE CARD           ")
        print("==========================================")
        print(f"Student ID       : {self.__student_id}")
        print(f"Full Name        : {self.__full_name}")
        print(f"Department       : {self.__department}")
        print(f"Semester         : {self.__semester}")
        print(f"Current GPA      : {self.__gpa:.2f}")
        print(f"Honor Status     : {honor_status}")
        print(f"Enrolled Courses : {courses_list}")
        print("==========================================\n")


if __name__ == "__main__":
    student1 = Student("20231604", "Umut Caliskan", "Information System Engineering", 7)

    student1.register_course("AII003 - Software Engineering")
    student1.register_course("ISE401 - System Analysis")
    student1.update_gpa(3.55)
    
    student1.get_student_profile()
    
    student1.drop_course("ISE401 - System Analysis")
    student1.get_student_profile()
