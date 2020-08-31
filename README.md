# dexpense_tracker
A dynamic robust expense management system made with django with api endpoints.

## Setup
step 1. Install packages from requirements.txt <br/>
step 2. Make a superuser. <br/>
step 3. Make groups ["employee", "manager", "auditor"] from django admin dashboard or from shell<br/>
step 4. Assign the below permission to the above groups. <br/>
step 5. Create users either from the registration page or from the django admin panel and assign them to the necessary groups.<br/>
step 6. Create categories ["travel", "misc", "food", "accommodation", "training", "certification", "software purchase"] <br/>

## Roles
1. Manager can have all the expense and category permissions <br/> 
2. Employee can have only expense permission apart from change_status_expense <br/>
3. Auditor can have only can_view_approve_expense <br/>

## Tracker app functionality
Home page: It can be accesible by the employee and manager. It shows all the pending expenses and rejected expenses. Status can be changed which can only be done by a manager.<br/>
Approved expenses page: It can be viewed by everyone it shows the expenses which has been approved. <br/>
Create expenses page: Expenses can be created only by the admins and by the employees. Status is automatically set to pending and submitted by is set to backend automatically. <br/>


## Tracker API endpoints
    api_urls = {
        'List': '/expense-list',
        'Detail View': '/expense-detail/<str:pk>/',
        'Create': '/expense-create/',
        'Update': '/expense-update/<str:pk>',
        'Delete': '/expense-delete/<str:pk>'
    }
 
## Improvements to be made
<strong>WEB</strong>  <br/>
1> Make a page to view individual submitted expenses.<br/>
2> Make a feature for employees to pick their designated manager from the department<br/>

<strong>API</strong>  <br/>
1> Use Django Rest Framework authentication to handle the endpoints to see who is logged in and show results based on the roles. <br/>
