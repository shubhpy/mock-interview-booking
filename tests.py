import requests
import subprocess

subprocess.run(["find", ".", "-path", '"*/migrations/*.py"', "-not", "-name", '"__init__.py"',  "-delete"])
subprocess.run(["find", ".", "-path", '"*/migrations/*.pyc"', "-delete"])
subprocess.run(["rm", "db.sqlite3"])
subprocess.run(["python", "manage.py", "makemigrations"])
subprocess.run(["python", "manage.py", "migrate"])

print("---------------------Test Case 1---------------------")
print("Showing systemconfig right now")
print(requests.get('http://127.0.0.1:8000/admin/systemconfig/').text)
print()

print("---------------------Test Case 2---------------------")
print("Adding a systemconfig for real time access to system configs")
print(requests.post('http://127.0.0.1:8000/admin/systemconfig/', json={"students_free_mock_interviews_allowed": 15 }).text)
print()

print("---------------------Test Case 3---------------------")
print("Showing all students")
print(requests.get('http://127.0.0.1:8000/students/').text)
print()

print("---------------------Test Case 4---------------------")
print("Adding student 1")
print(requests.post('http://127.0.0.1:8000/students/', json={"name": "Shubhanshu", "email": "shubh1910@gmail.com"}).text)
print()

print("---------------------Test Case 5---------------------")
print("Adding student 2")
print(requests.post('http://127.0.0.1:8000/students/', json={"name": "Vincy", "email": "vincy0@gmail.com"}).text)
print()

print("---------------------Test Case 6---------------------")
print("Adding interviewer 1")
print(requests.post('http://127.0.0.1:8000/interviewers/users/', json={"name":"Director", "email": "director@gmail.com"}).text)
print()

print("---------------------Test Case 7---------------------")
print("Adding interviewer 2")
print(requests.post('http://127.0.0.1:8000/interviewers/users/', json={"name":"Manager", "email": "manager@gmail.com"}).text)
print()

print("---------------------Test Case 8---------------------")
print("Adding interviewer 3")
print(requests.post('http://127.0.0.1:8000/interviewers/users/', json={"name":"HR", "email": "hr@gmail.com"}).text)
print()

print("---------------------Test Case 9---------------------")
print("Adding an interview slot for interviewer 1 Director")
schedule_json = {"start_date_time":"2020-07-11 04:00","end_date_time":"2020-07-11 05:00", "interviewer_id": 1}
print(schedule_json)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/', json=schedule_json).text)
print()

print("---------------------Test Case 10---------------------")
print("Adding interview slot for interviewer 2 Manager")
schedule_json = {"start_date_time":"2020-07-11 06:00","end_date_time":"2020-07-11 07:00", "interviewer_id": 2}
print(schedule_json)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/', json=schedule_json).text)
print()

print("---------------------Test Case 11---------------------")
print("Adding interview slot for interviewer 3 HR")
schedule_json = {"start_date_time":"2020-07-11 08:00","end_date_time":"2020-07-11 09:00", "interviewer_id": 3}
print(schedule_json)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/', json=schedule_json).text)
print()

print("---------------------Test Case 12---------------------")
print("Showing all available interview slots for student 1 Shubhanshu")
get_available_slots = {"student_id":1, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 13---------------------")
print("Showing all available interview slots for student 2 Vincy")
get_available_slots = {"student_id":2, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 14---------------------")
print("Booking a slot of id 1 for student 1 Shubhanshu")
book_slot = {"student_id":1, "interviewer_slot_id": 1}
print(book_slot)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/book/', json=book_slot).text)
print()

print("---------------------Test Case 15---------------------")
print("Showing all available interview slots for student 1 Shubhanshu in the same dates")
print("Already booked appointment with interviewer 1 Director, So It is not there")
get_available_slots = {"student_id":1, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 16---------------------")
print("Showing all available interview slots for student 2 Vincy")
print("2 are there, coz 1 is booked by Shubhanshu")
get_available_slots = {"student_id":2, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 17---------------------")
print("Booking a slot of id 2 for student 1 Shubhanshu")
book_slot = {"student_id":1, "interviewer_slot_id": 2}
print(book_slot)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/book/', json=book_slot).text)
print()

print("---------------------Test Case 18---------------------")
print("Showing all available interview slots for student 1 Shubhanshu in the same dates")
print("Already booked appointment with Director and Manager, So now Only with HR showing")
get_available_slots = {"student_id":1, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 19---------------------")
print("Showing all available interview slots for student 2 Vincy")
print("Vincy can also see only HR now")
get_available_slots = {"student_id":2, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 20---------------------")
print("Showing all interviews booked or completed in the system")
print(requests.get('http://127.0.0.1:8000/interviews/').text)
print()


print("---------------------Test Case 21---------------------")
print("Completing the interview id 1 with grades 0")
complete_interview = {"grades":0,"completed_at":"2020-07-12T00:00:00Z","note":"Not prepared"}
print(complete_interview)
print(requests.post('http://127.0.0.1:8000/interviews/1/complete/', json=complete_interview).text)
print()

print("---------------------Test Case 22---------------------")
print("Completing the interview id 2 with grades 1")
complete_interview = {"grades":1,"completed_at":"2020-07-12T00:00:00Z","note":"Not prepared"}
print(complete_interview)
print(requests.post('http://127.0.0.1:8000/interviews/2/complete/', json=complete_interview).text)
print()

print("---------------------Test Case 23---------------------")
print("Showing all available interview slots for student 1 Shubhanshu in the same dates")
print("As his last two grades are <=1, now none is showing")
get_available_slots = {"student_id":1, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()

print("---------------------Test Case 24---------------------")
print("Showing all available interview slots for student 2 Vincy")
print("Vincy can still see slot for HR")
get_available_slots = {"student_id":2, "start_date_time": "2020-07-11T00:00:00", "end_date_time": "2020-07-12T00:00:00"}
print(get_available_slots)
print(requests.post('http://127.0.0.1:8000/interviewers/slots/available/', json=get_available_slots).text)
print()
