# Problem Statement
Interview Kickstart (IK) offers 15 mock interviews to every student who enrolls in our course. We need to build an API that can service requests from any client and either return all interview slots available for the student's search criteria or return no slots available. The constraints are
- The Interviewers provide their own availability. They are not available 24/7 for any slot that the student requests.
- A student should not be able to see any interviews if they have already completed their 15
- A student should only see slots from an interviewer who has not interviewed the student before.
- A student should only see additional interviews if their last 2 interview grades are > 1. (We have a grading scale from 0 - 5).

The input request looks like this
`{"studentId": 123, "startDateTime": "2020-06-05T13:00:00", "endDateTime": "2020-06-05T14:00:00"}`

What we are looking for are the following.
1. Data models or DB Tables for the entities involved in servicing this request.
2. The API Code that handles the request and does the constraint checking and returning the slots.
3. During the interview, a discussion on how we would handle race conditions.
4. All optimizations that we can apply to scale the number of requests handled


# Solution Description
1. I have created a django application named ik_backend containing 4 apps (students, interviewers, systemconfigs and interviews)
2. Each entity's model, views, serializers and urls are defined in their respective apps files.
3. ## Running Instructions

    ### Terminal 1

    `virtualenv shubhanshu_interviews_booking -p python3`

    `cd shubhanshu_interviews_booking`

    `source bin/activate`

    extract zip content in this folder here, `mock-interview-booking-master` folder from zip file should be extracted here

    `cd mock-interview-booking-master`

    `pip install -r requirements.txt`

    `python manage.py makemigrations`

    `python manage.py migrate`

    `python manage.py runserver`

    ### Terminal 2
    `cd shubhanshu_interviews_booking`

    `source bin/activate`

    `cd mock-interview-booking-master`

    `python tests.py`

4. We will keep running runserver in one terminal and will run tests.py in another.
6. testcases will explain all the constraints needed in the problem statement. Can we refer to code if needed.
7. In tests.py, I am deleting the db.sqlite3 and all migrations to start over.
8. If need to carry on existing data filled by tests, those subprocess commands should be comment out.


# Future Scope
1. Could return each id's name for better transparency.
2. Interviewers Slot definition is kind of repetitive for now, i.e. If I am available for 2-4 everyday in next week then right now I will have to create 5 slots which could be done in just 1 keeping startdate and enddate and times at each date kind of structure.
3. Booking slots is saving 3 different entities at once, that step has to be in a transition.
4. Before booking, a dry run/lock is needed so one slot is processed by one request at a time.
