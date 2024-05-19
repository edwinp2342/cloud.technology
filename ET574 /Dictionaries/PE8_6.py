stuInfo1 = {'name': 'John Doe', 'gpa': 3.5}
stuInfo2 = {'name': 'Jane Doe', 'gpa': 3.7}
stuInfo3 = {'name': 'Jim Doe', 'gpa': 3.2}
stuClass = [stuInfo1, stuInfo2, stuInfo3]
all_students_output = [f"{student['name']} - GPA: {student['gpa']}" for student in stuClass]
all_gpa_output = [student['gpa'] for student in stuClass]
stuClass[-1]['gpa'] = 4.0
stuClass.append({'name': 'Jill Doe', 'gpa': 3.9})
formatted_output = [f"{student['name']} - GPA: {student['gpa']}" for student in stuClass]
(all_students_output, all_gpa_output, formatted_output)
