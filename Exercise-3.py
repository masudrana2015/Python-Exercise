
student_data = [("Alice", 101, 85), ("Bob", 102, 92), ("Charlie", 103, 78), ("David", 104, 95)]


sorted_student_data = sorted(student_data, key=lambda x: x[2], reverse=True)


print(sorted_student_data)
