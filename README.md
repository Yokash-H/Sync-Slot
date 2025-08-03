# Sync-Slot
Sync slot is a web app designed to help friends find common free time in their daily time table

What are its features? Dead Simple: Plug in your weekly timetable with an easy-to-use interface. Smart Syncing: Our backend magic compares everyone’s schedules in real-time to spot common free times. Crystal Clear: Shows you the exact time slots when everyone’s good to go. Built to Impress: Crafted with Flask (Python) and HTML/CSS for a clean, smooth vibe.

Why We Built It? Coordinating schedules in college is tough. Between classes, clubs, and life, finding time to meet up shouldn’t be a chore. Sync Slot takes the stress out of planning by doing the hard work for you. It’s perfect for students who want a quick, private way to sync up with friends or project groups.

SyncFree is a web app built using Python (Flask), HTML, and MySQL to help students find common free slots among friends. On the homepage, users enter their name, registration number, and select the slots they’re occupied in. When submitted, this data is saved in a MySQL database.

The backend (app.py) processes the selected slots and compares them with other students' data stored in the database. It then returns a list of students who are not free during those slots, helping users identify overlapping class times.

Everything is connected through Flask, the frontend (form.html) collects input, the backend handles logic, and MySQL stores the data. This makes it easy and interactive for students to manage and compare schedules with friends.
