# DenSys
## Frontend Details
- Frontend is written with Vue 3 and TailwindCSS 3
- To download dependencies, inside of `front` folder type `npm install`
- To start frontend server, inside of `front` folder type `npm run serve`
- If you change some css in the frontend you need to recompile css by `npx tailwindcss -i ./src/input.css -o ./src/output.css --watch`. It will stay as server and listens to changes in css and automatically recompile it
- Index Page has nothing yet. Go straight to '<homepage>/admin'
- On the Admin Page you have 4 Admin actions to click on the sidebar
- Test them (start the backend server first). If they work I will push to the main branch
- Some fields on the registration page are predefined. This is done for quick test iterations. But everything works - you can change any field
- Red Circle means required
- Black Circle means disabled (cannot be changed)
- Some fields have validation. Try to test that as well. Most probably something does not work
- For the patient registration IIN, tries to match the date when you type 12 digits. Technically you can submit without INN/date match. Doctor Registration does not have this feature
- Table has clickable rows that lead to Patient/Doctor profiles where you can edit them
- No Login Page for Admin yet

## Backend Details
- Backend is written with Django 4 and REST framework
- To download dependencies, inside of `back` folder type `pip install django djangorestframework`
- To start backend server, inside of `back` folder type `python manage.py runserver`
- Backend has custom User model in /back/accounts, both Patient and Doctor inherit from it
- IIN is the primary key for User
- '<server page>/api/' is the main page that frontend refers to for the data
- '<server page>/api/patient/<iin>' for getting a Patient
- '<server page>/api/patients' for getting all Patients
- '<server page>/api/doctor/<iin>' for getting a Doctor
- '<server page>/api/doctors' for getting all Doctors
- You can go these links and test whether api contains anything
- When you register/update/view Patients/Doctors, the frontend sends requests that may fail
- For example, when you register a Patient with existing IIN, it fails
- Server spits some information to the terminal that helps see whats wrong
- Admin superuser does not exist and there is no authentication yet
- '<server page>/admin' does nothing except default behavior
- Any request to the api does not require permissions yet

## Some git commands
To work in bk branch
- `git push --set-upstream origin bk` \# was needed to push change
- `git checkout bk` \# switch to bk branch
To get this repo:
- `git clone https://github.com/DaniiarS/DenSys.git`
- `cd DenSys`
To change something:
- `git remote add DenSys https://github.com/DaniiarS/DenSys.git` \# sometimes needed to push changes
- `git add <some files>`
- `git add .` \# to add all files
- `git status` \# to see the branch and what was modified
- `git commit -m "My message"`
- `git push`
- your github username
- password is the token

