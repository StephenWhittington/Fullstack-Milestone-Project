# Find Your Artifact

## By Stephen Whittington

The survey from Travis says:
[![Build Status](https://travis-ci.org/StephenWhittington/Fullstack-Milestone-Project.svg?branch=master)](https://travis-ci.org/StephenWhittington/Fullstack-Milestone-Project)

(Pull requests will be ignored. This is an educational project and needs to remain a solo effort.)

Find Your Artifact is a single ecommerce web page built with
the django framework that saves data to the postgresql
database app on heroku, along with python and the stripe
api for submitting payments. The user can register,login,reset-password and
purchase an artifact from start to finish. The site is easy to navigate 
with a simple layout and is responsive on mobile and desktop. 

## UX Process

[Link to my figma mockup](https://github.com/StephenWhittington/Fullstack-Milestone-Project/blob/master/static/images/Find%20Your%20Artifact.png)

I started with a desktop mockup using figma by focusing on the core aspects
of what the user should experience, a well responsive and easy to use webpage.
With easy navigation, saving data forms that tell the user when and where
they can do things. My datbase design was to start with registering a user
then allowing them to log in and only checkout if authenticated, Also
being able update their customer profile and add artifacts to the basket.

The user wants to be able to view the artifacts and add them to the basket
but be required to register and log in if they want to go any further.
The site is built with easy navigation and layout so the user can easily
navigate around it without any issues.

### User Stories

#### **list of user stories.**

* **Register a User**: The user clicks on the register link or redirect from the login
page, it takes them to the registration page where they fill out the mandatory fields click
register then saves their details to the database and logs them in.

* **User Login**: An existing user can click on the login link enter the information
they registered with and it will log them into the page.

* **logout**: A user can logout via the link in the navbar, which then logs
the user out and their basket will be empty if they had anything added.

* **Create/Update Customer Profile**: when the user clicks on the customer link if
they havent added any details the button 'add details' will be seen that takes them
to a form to add them. Or if a user has added details already they see the
'edit details' button if they want to update their shipping details.

# Features 

## Existing Features

* **Responsive nav/sidebar** - A responsive and easy to use navbar that collapses into a side bar when screen is viewed
on mobile.

* **Background Image** - A background image that looks good with the navbar and panel-body element on the page.

* **Buttons** - Buttons when selected that either save/edit/add to the database, also taking the user to the correct
path with no difficulty.

* **Responsive Columns For Artifacts** - All of the artifacts added have been put into bootstrap columns for 
responsive design on mobile and dekstop.

* **User Input Forms** - easy to navigate and fill out forms with the recommended information for the user.

* **Django Password Reset** - A user enters their email into the forgotten password field which then sends them
an email for a password reset.

* **Search Bar** - Users can search for artifacts by name or entering any text related in the search bar.

## Features Left To Implement 

* Adding one to one user links between customer details and checkout form

* Add another page showing more information on artifacts along with comments

* An order history page that shows the user what they have ordered

# Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  
    * The website uses Semantic Markup Language as its foundation.   

* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

    * The website uses Cascading Style Sheets to implement design and customization.
    
* [Python3](https://www.python.org/download/releases/3.0/)

    * The website uses python3 a high-level, interpreted, interactive and object-oriented scripting language,
    which is highly readable and uses English keywords frequently whereas the other languages use punctuations.

* [jQuery](https://jquery.com/)

    * The website uses JQuery The Document Object Model (DOM) to simplify manipulation.

* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
  
    * The website uses the bootstrap framework for responsive mobile-first design

* [Django](https://www.djangoproject.com/)
  
    * The main framework driving force behind find_your_artifact

* [Stripe](https://stripe.com/gb)
  
    * Handles all the user payments

* [Amazon Web Services](https://aws.amazon.com/)
  
    * AWS hosts the static and media files using S3

* [PostgreSQL](https://www.postgresql.org/)
  
    * I have used PostgreSQL to store and retrieve the data.

* [Travis CI](https://travis-ci.org/)
  
    * I have used Travis to test my code each push to GitHub.

* [Gunicorn](https://gunicorn.org/)
  
    * I have used Gunicorn to allow me to connect to Heroku.

# Testing 

### User Story Tests Completed   

1. **Register**:
    1. Click on the register link.
    2. A form is shown to enter username,email,password/confirm.
    3. Confirmed that when the details are entered the form is ready for submitting.
    4. Confirm that when register is clicked it saves the details to the database and logs in.

1. **Login**:
    1. Click on the login link.
    2. A form is shown to enter username or email.
    3. Confirmed that when the details are entered the form is ready for submitting.
    4. Confirm that when login is clicked it saves the details to the database and logs user in.

1. **Checkout authenticated Test**:
    1. Enter a quantity and add a artifact.
    2. A artifact is shown in the basket ready for checkout
    3. Clicking on checkout without being loged in redirects to the login page
    4. Confirm that a customer cannot checkout an artifact without being authenticated.

1. **Customer Details Add/Edit**:
    1. Click on the customer link.
    2. Takes the user to a customer profile page that shows shipping details with current loged in user
    3. {{if not user.customer}} it shows the 'add details' button, and {% if user.customer %} the 'edit details' button.
    4. Confirm that when the user clicks either of these it sends them to a form then saves it to the database.

1. **Customer Checkout**:
    1. Select quantity and add a artifact to the basket.
    2. Basket then shows that it has however many items ready for checkout.
    3. Go to basket and ammend quantity if necessary, once done click checkout. 
    4. Confirm that when checkout is clicked it brings you to an order/payment form.
    5. The user enters the form data and the credit card details, then clicks submit payment.
    6. Confirm that when the user clicks submit paymanet button the order is processed and renders a success page.

1. **Collapse Navbar**:
    1. Click on the nav icon when in mobile or tablet view.
    2. navbar collapses showing the links to the user and they can select which page they want to
    visit.
    3. Confirmed that the webpage has a responsive collapsing navbar that is easy to use and goes to the correct paths.

1. **Password Reset**:
    1. Go to password reset page
    2. Try to submit the form with all inputs valid and verify that a success message appears.
    3. Then the user gets an email they open it and click the link to go to change their password
    4. Try to submit the form with all inputs valid and verify that a success message appears.
    5. Confirm that when the user goes to log back in they can use their new password.

### How it looks/works on different browsers and screen sizes

My project runs smoothly on all screen sizes mainly due to the impact
of the bootstrap column design and bootstrap forms. I tested the page
on the three most common web browsers Chrome/IE and Mozzila Firefox and i am happy
with how it looks.

## Compatibility

To make sure users have a broad range of accessibility, i have tested my project on 3 major browsers in both desktop and mobile size.

* Chrome
* Mozilla Firefox
* Internet Explorer

## Bugs And Problems

I havent come across any bugs yet but more problems with adding different apps to my project
but due to time frame, I havent got enough time to add them before submission which is why i have
focused on the core aspect having a user sign up and purchase an artifact with no errors.

I have had a problem with the django testing framework when i try to do my tests i get an 
error. I understand how to do automated testing but havent had chance to implement them,
so i have done most of my tests manually.

    * **Got an error creating the test database: permission denied to create database**

But apart from those parts above my project runs fine without any major errors.

# Deployment

My source code was all done via GitHub, You can find my repository here:
    
* **Repository**:[https://github.com/StephenWhittington/Fullstack-Milestone-Project](https://github.com/StephenWhittington/Fullstack-Milestone-Project)

The deployment and live version is hosted via Heroku:

* **Heroku**:[https://find-your-artifact.herokuapp.com/](https://find-your-artifact.herokuapp.com/)
    
    * First I created a new app and named it and set the region. 
    
    * Then I logged into heroku via git with `heroku login` and connected git to the new app location using
    `heroku git:remote`.

    * I then created a `requirements.txt` and `Procfile`:
        
        * `sudo pip3 freeze > requirements.txt`
        * `echo web: gunicorn find_your_artifact.wsgi:application > Procfile`
    
    * Then added all my project files using `git add .` and commited with `git commit -am "make it better"`
    
    * The project was then pushed using `git push heroku master` and scaled the app dynos using `heroku ps:scale web=1`.
    
    * I then went to Heroku settings clicked on Config Vars and added my
     `AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_ADDRESS,EMAIL_PASSWORD, HOSTNAME_HEROKU, SECRET_KEY, STRIPE_PUBLISHABLE and STRIPE_SECRET`.
    
    * These are also ignored and hidden by a `.env` file in my workspace.
    
I can confirm that there are no differences from the deployed and the development version.

## How Developers can download and work on my project

    * Click on Clone or Download on my repository.
    * Create your own enviorment variables  
    * Clone the project in your workspace using git clone
    * Devs can also link it with gitpod if you use the `gitpod.io#` url or browser extension.

# Credits
 
 **Content**

 For this project i decided to go back to bootstrap 4 as the inbuilt form views
 suited for this type of ecommerce web page. Becuase of the time frame i decided
 to focus mainly on the customer experience from start to end. My CSS styling
 remained simple as i used the same class objects, but maintained a responsive
 and easy readable page. Any problems i encounted during the project i went to slack
 or contacted tutor support and also tried to sorce the answer myself.

 **Media**
 
 * The media images for this project were sorced from [Pixabay](https://pixabay.com/)
 and are for educational purposes only.

  **Acknowledgements**

I received inspiration for this project from the django ecommerce mini project,
I then built the project using my own idea instead of the examples given
and i feel like i understand python,django,stripe a lot better now using it based off my own inspiration.

A huge thanks to my mentor Ignatius Ukwuoma for his time, suggestions, and constructive feedback for this project!






