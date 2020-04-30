# Find Your Artifact

## By Stephen Whittington

[![Build Status](https://travis-ci.org/StephenWhittington/Fullstack-Milestone-Project.svg?branch=master)](https://travis-ci.org/StephenWhittington/Fullstack-Milestone-Project)


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

* **User Login**: An exsisting user can click on the login link enter the information
they registered with and it will log them into the page.

* **logout**: A user can logout via the link in the navbar, which then logs
the user out and their basket will be empty if they had anything added.

* **Create/Update Customer Profile**: when the user clicks on the customer link if
they havent added any details the button 'add details' will be seen that takes them
to a form to add them. Or if a user has added details already they see the
'edit details' button if they want to update their shipping details.

# Features 

## Existing Features

