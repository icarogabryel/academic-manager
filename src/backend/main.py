import academic as ac

def main():
    # Creating two teachers
    john = ac.Teacher("John", 1, "Algebra")
    steve = ac.Teacher("Steve", 2, "Geometry")

    # Creating two subjects
    algebra = ac.Subject("Algebra", john)
    geometry = ac.Subject("Geometry", steve)

    # Creating three students
    mary = ac.Student("Mary", 3, 20)
    marcos = ac.Student("Marcos", 4, 21)
    tom = ac.Student("Tom", 5, 22)

    # Creating two classes
    geometry_class = ac.SubjectClass(1)
    geometry_class.add_student(mary)
    geometry_class.add_student(marcos)
    geometry_class.add_test(mary, 90, 0.5)

    geometry.add_class(geometry_class)

    algebra_class = ac.SubjectClass(2)
    algebra_class.add_student(mary)
    algebra_class.add_student(tom)
    algebra_class.add_test(tom, 80, 0.5)

    algebra.add_class(algebra_class)

    # Creating a course
    math_course = ac.Course("Math")

    # Adding teachers, students, and subjects to the course
    math_course.add_teacher(john)
    math_course.add_teacher(steve)

    math_course.add_student(mary)
    math_course.add_student(marcos)
    math_course.add_student(tom)

    math_course.add_subject(algebra)
    math_course.add_subject(geometry)

    print("Classes IDs in algebra:")
    algebra.show_classes()
    print("\nClasses IDs in geometry:")
    geometry.show_classes()

    print("\nStudents in algebra")
    algebra_class.show_students()
    print("\nTests in algebra")
    algebra_class.show_tests()

    print("\nStudents in geometry")
    geometry_class.show_students()

    print("\nTests in geometry")
    geometry_class.show_tests()

if __name__ == "__main__":
    main()