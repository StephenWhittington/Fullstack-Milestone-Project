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

### How it looks/works on different browsers and screen sizes

My project runs smoothly on all screen sizes mainly due to the impact
of the bootstrap column design and bootstrap forms. I tested the page
on the three most common web browsers Chrome/IE and Mozzila Firefox and i am happy
with how it looks.

## Bugs And Problems







