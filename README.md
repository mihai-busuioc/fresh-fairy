# Fresh Fairy



The Fresh Fairy is a web application, designed, built and deployed by me, Mihai Busuioc, to satisfy the requirements of the final project for the Code Institute Full Stack Web Development diploma.

The website is intended to be a custom built base for The Fresh Fairy Cleaning company, allowing the owners to list and manage services for sale whilst also creating an attractive, smooth and effortless online shopping experience for customers. 
The site also offers interactive features such as product reviews and ratings to encourage user activity and maximise user experience. 

## Demo
A live demo can be found [here](https://fresh-fairy.herokuapp.com/).

## Table of Contents
- [UX](#ux)
  * [User Stories](#user-stories)
  * [Design](#design)
- [Features](#features)
  * [Existing Features](#existing-features)
  * [Features Left to Implement](#features-left-to-implement)
- [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Libraries](#libraries)
  * [Databases](#databases)
  * [Tools](#tools)
- [Information Architecture](#information-architecture)
- [Testing](#testing)
  * [Automated Testing](#automated-testing)
  * [Manual Testing](#manual-testing)
  * [User Stories Testing](#user-stories-testing)
  * [Bugs](#bugs)
- [Deployment](#deployment)
  * [To run the project locally](#to-run-the-project-locally)
  * [Deploying to Heroku](#deploying-to-heroku)
- [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## UX

### User Stories
#### Registration and User Accounts 
| ID  | As a …                | I want to be able to…                                                              | So that I can…                                                                                        |
| ----| --------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1   | public user           | easily register for an account                                                     | have a personal acount and view my profile                                                            |
| 2   | registered user       | receive an email confirmation after registering                                    | verify my account registration was successful                                                         |
| 3   | registered user       | easily log in and out                                                              | access my personal acount information                                                                 |
| 4   | registered user       | easily recover my password if I forget it                                          | regain access to my acount                                                                            |
| 5   | registered user       | have a personalised user profile                                                   | View my order history, order confirmation and payment information                                     |
| 6   | registered user       | rate and review a product                                                          | provide feedback to store owner and other shoppers                                                    |


#### Viewing and navigation
| ID  | As a …                | I want to be able to…                                                              | So that I can…                                                                                        |
| ----| --------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
|  7  | site user (all users) | view a list of all services                                                        | select some to purchase                                                                               |
|  8  | site user (all users) | view individual product details                                                    | identify the product description, price, image, rating and corresponding product reviews              |
|  9  | site user (all users) | easily view total of shopping basket                                               | avoid spending too much                                                                               |


#### Purchasing and Checkout
| ID  | As a …                | I want to be able to…                                                              | So that I can…                                                                                        |
| ----| --------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 10  | site user (all users) | easily select the  service to add to my shopping cart                              | purchase the amount of products I want                                                                |
| 11  | site user (all users) | view items in my cart                                                              | review the items I intend to purchase and identify the total cost                                     |
| 12  | site user (all users) | remove items or change the quantity of individual items in my cart                 | amend my order before checkout                                                                        |
| 13  | site user (all users) | easily enter my personal and payment information                                   | check out quickly with no problems                                                                    |
| 14  | site user (all users) | feel confident that my personal data is safe and secure                            | provide the information required to complete my purchase                                              |
| 15  | site user (all users) | view order confirmation                                                            | verify that I haven't made any mistakes                                                               |
| 16  | site user (all users) | receive an email confirmation after checkout                                       | Keep a record of what I have purchased                                                                |

##### Admin and Store Management
| ID  | As a …                | I want to be able to…                                                              | So that I can…                                                                                        |
| ----| --------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 17  | Store Owner           | add products                                                                       | list items for sale                                                                                   |
| 18  | Store Owner           | edit / update a product                                                            | adjust product details where necessary                                                                |
| 19  | Store Owner           | delete a product                                                                   | remove items that are no longer available                                                             |


### Design 
Inspired by the clean look, The Fresf Fairy website has an overall clean, crisp, neutral feel . The following design choices were made with this in mind:

#### Fonts
The primary font 'Merriweather' was chosen for the main text of the site because of it clear readability and clean, crisp style providing a neutral, yet friendly appearance. This font also looks good in uppercase to add emphasis to the buttons.
 

#### Icons
To keep the site uncluttered, clean and minimalist, a small number of icons were carefully selected and implemented across the site. 

The shopping basket icons was used in the navigation bar as it is conventionally used in this setting and would be what the user expects to see.

Star icons are utilised for users to rate products in the review section and add visual emphasis when displaying the average rating of a product as per convention.
 
The chevrons arrows and the lock all  are conventional, clean and would be what the user expects to see.

#### Colours


* White `#fff`
* Black `#000`
* Light Blue `#24ADE3`

The white, black and light blue color scheme was chosen to create a clean, crisp theme. 

#### Images
Images  were carefully selected to appeal to users senses whilst not detracting from the overall theme.

#### Styling
Rounded corners were implemented on all form, image and button elements to create the desired  appearance. 




## Features

### Existing Features

#### Navbar
The Navbar features on every page across the site so to ensure users are able to easily navigate from wherever they are.  

On desktop view there is a fixed top nav featuring the brand Logo to the far left and three large menu items to the right providing options to access account  view the services and go to home page also a icon of the  shopping basket.    

On smaller devices including mobiles and tablets  the main navbar has been collapsed behind a bootstrap toggler button (burger icon) in its place.  

#### Home Page
The landing page features a opaque card displaying '5 STAR RATED NATIONWIDE CLEANING SERVICES' resembling a ladder 
and a button to 'CHOOSE A SERVICE' directing users straight to the services results.  Users can scroll down the page to information about the company. 

#### Fresh Fairy Store
##### Add Product
Store Owners can add new products to the shop, by navigating to the 'My Profile' menu and selecting 'Add Product'. This directs the user to a simple form for them to enter all the service details required. 

##### Product Results
Products are displayed using bootstrap cards, with a large service style  image at top and the service name, price, and rating  detailed in the card body beneath. The large image is intended to draw attention to the product. 

Results are listed in rows of 4 on extra large screens and rows of 2 on tablets whilst products are stacked on top of each other on mobile view. Rows are separated by a transparent horizontal rule to improve user experience.

Store owners will also have the ability to edit or delete products from the store by clicking on the small 'Edit' or 'Delete buttons on each product.

##### Back to Top button
Users will note a small button with a arrow point up at the bottom right of their view. When scrolling down the results, users can click on this button to return to the top quicky and easily.

#### Product Detail Page
Users can click on a product image to view full details for that particular product. On desktop view, users are presented with the product image to the left and all the product information on the right, whilst on mobile view the image is stacked on top of the product information. 

##### Quantity Select
From the product detail page, users can select the date they want  the service done to add to their cart. 

##### Product Review Function
At the bottom of the product detail page, users can view reviews that have been left for that particular product. Logged in users will also be presented with a simple form including a star rating system to enable them to write a review and rate the product from 1-5, whilst those not currently logged in will be prompted to register or login in order to leave a review. 

Individual star ratings are used to calculate the average product rating which are displayed on product results and on the product detail page. 

#### Shopping Basket
The shopping basket icon is located to the far right of the navigation bar. Once a user (whether logged in or not) has added at least one item to their basket, the grand total appears next the icon. This feature enables users to easily see the total cost of the items in their basket so they can keep track of their spending.  Users are also able to click on the icon to view the contents of their shopping cart. 

On the shopping basket page, desktop users will see a card containing the product image, name, date selected, price, Quantity and subtotal. Different products are displayed in different rows. In the quantity column, users have the ability to adjust the number or remove the item from the cart. 

At the bottom users can see a summary of the cost broken down into  Total, Discount and Grand Total, as well as buttons to continue to the secure checkout or keep shopping.

#### Secure Checkout
On the secure checkout page, users can view an order summary and enter their shipping and payment details. There is also a checkbox users can select to save their delivery details to their profile. This will enable faster payments in the future as delivery details will be pre-populated with their information. 

At the bottom, two buttons provide options to either 'adjust cart' or 'complete order' following which they will be directed to checkout success page notifying them that a confirmation email has been sent to their email address and detailing their order summary below. As indicated users should find a confirmation email in their inbox.   


#### My Account
Authentication and authorisation is implemeted here using the django Allauth package. 

Public users will click on the 'My Account' icon to find options to 'register' for or 'login' to an account. By clicking Register users are redirected to a sign up page containing a registration form requiring the following details:

* Email address
* Email address confirmation
* Username
* First Name
* Last Name
* Password 
* Password confirmation

Form validation is implemented to prevent users from omitting information or an invalid email address or password. If a password is too common or has less than 8 characters they will receive an error meesage. When a user successfully completes the registration form they will be redirected to a page requesting that they verify their email address by clicking on the link contained within their email to finalise the sign up process. 

The login page requires just a username / email and their passsword.

Once a user is logged in, they will find clicking on the 'My Account' provides options to access 'My Profile' or 'Logout'.  

#### My Profile
Registered users can view their profile by clicking on the link under My Account. The My Profile page includes the users  delivery information and order history. Here they can change their  default delivery information and name, as well as see a list of all their previous orders the store owners can see  here the add product button. 

#### Messages
Messages have been implemented to provide feedback to the user when adding, editing or deleting products from the cart as well as when they leave a review. Users will recive confirmation of a successful action or else be notified that an error has occured. 

#### Footer
Bootstrap Footer has been used to provide the user with just the  copyright information. 

Although  Privacy Policy and Terms and Conditions pages documents are a legal requirement of any online shop, this is just a education website so i didn't implement them.

### Features Left to Implement

* Social Account Login - Giving users the ability to register and login via their social media account, thus streamlining the process. Additionally this will enable store owners to track users activity which will assist with email marketing and advertising.  

* Favourites - This would give logged in users the ability to add their favourite products to a 'wish list' which they can view, edit and delete. 

* Additional payment methods - Allowing users to make payments with Paypal, apple pay or google pay.

## Technologies
All the languages, frameworks, libraries, and tools used to construct this project are listed below. I have also provided a relevant link and a brief overview of its usage.

### Languages
* <a target="_blank" href="https://en.wikipedia.org/wiki/HTML5">HTML5</a> – Used to write customised front-end content for the application.
* <a target="_blank" href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets">CSS3</a> – Used to customise the style of the web application. 
* <a target="_blank" href="https://en.wikipedia.org/wiki/JavaScript">JavaScript</a> - Used to add an onclick event to my cancel and return buttons within the application.
* <a target="_blank" href="https://www.python.org/">Python</a> - Used to build the back-end functionality.


### Frameworks
* <a target="_blank" href="https://getbootstrap.com/">Bootstrap v5.0</a> - A framework used to create the responsive grid system and various components within the site including the navbar, buttons and cards. 
* <a target="_blank" href="https://www.djangoproject.com">Django</a> - A python web framework used to construct and render pages within the application quickly and easily.


### Libraries
* <a target="_blank" href="https://jquery.com/">jQuery</a> - A JavaScript library used here to simplify DOM manipulation when initializing specific Bootstrap components within the application.
* <a target="_blank" href="https://fonts.google.com/">Google Fonts</a> – The font used was obtained from Google Fonts.
* <a target="_blank" href="https://fontawesome.com/">Font Awesome</a> - All icons used within the web application were sourced from Font Awesome.
* <a target="_blank" href="https://jinja.palletsprojects.com/en/2.11.x/">Jinja</a> - A templating language used to simplify the displaying of back-end data in a HTML markup format that is returned to the user via an HTTP response.


### Databases
* <a target="_blank" href="https://www.postgresql.org">PostgreSQL</a> - Used for production, provided by heroku.
* <a target="_blank" href="https://www.sqlite.org/index.html">SQlite3</a> - Used for development, provided by django.


### Tools 
* <a target="_blank" href="https://www.gitpod.io/">GitPod</a> – The online Integrated Development Environment (IDE) used for the development of this project.
* <a target="_blank" href="https://pip.pypa.io/en/stable/installing/">PIP</a> - For installation of tools needed in this project.
* <a target="_blank" href="https://django-crispy-forms.readthedocs.io/en/latest/">Django Crispy Forms</a> – to control the rendering behavior of Django forms in an elegant way.
* <a target="_blank" href="https://stripe.com">Stripe</a> – as payment platform to validate and accept credit card payments securely.
* <a target="_blank" href="https://aws.amazon.com">AWS S3 Bucket</a> – AWS S3 Bucket to store images entered into the database.
* <a target="_blank" href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">Boto3</a> – to enable creation, configuration and management of AWS S3.
* <a target="_blank" href="https://pypi.org/project/django-heroku/">Django Heroku</a> – to ensure a seamless deployment and development experience.
* <a target="_blank" href="https://django-storages.readthedocs.io/en/latest/">Django Storages</a> – a collection of custom storage backends with django to work with boto3 and AWS S3.
* <a target="_blank" href="https://pypi.org/project/gunicorn/">Gunicorn</a> – WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
* <a target="_blank" href="https://pillow.readthedocs.io/en/stable/">Pillow</a> – as python imaging library to aid in processing image files to store in database.
* <a target="_blank" href="https://pypi.org/project/psycopg2/">Psycopg2</a> – as PostgreSQL database adapter for Python.
* <a target="_blank" href="https://www.google.co.uk/chrome/">Google Chrome</a> - This browser and its' developer tools were used throughout the development of the app.  
* <a target="_blank" href="https://github.com/">Git</a> – Used for version control
* <a target="_blank" href="https://github.com/">GitHub</a> – GitHub was used for hosting my repository
* <a target="_blank" href="https://github.com/">Heroku</a> – A cloud platform used for deployment
* <a target="_blank" href="https://validator.w3.org/">W3c Markup Validation Service</a> - The HTML code for this project was checked and validated by the W3c Markup Validation Service
* <a target="_blank" href="https://jigsaw.w3.org/css-validator/">W3c CSS Validation Service</a> - The CSS code for this project was checked and validated by the W3c CSS Validation Service


## Information Architecture

During development the project utilised the standard sqlite3 database installed with Django whilst on deployment it uses the PostgreSQL database provided by Heroku.

### Data Models

#### User
This project uses the standard User model provided by django.contrib.auth.models. Each user can:

* have one profile
* make numerous orders
* add numerous product reviews


#### Products App
This app has two models;  Services and Review which hold the data for the service itself and product reviews. The Services model uses a package called Pillow to store all image files in an AWS S3 bucket.


##### Services Model
| Name         | Key in DB    | Validation                                       | Field Type                |
|--------------|--------------|--------------------------------------------------|---------------------------|
| Sku          | sku          | max_length=254, null=True, blank=True            | CharField                 |
| Name         | name         | max_length=254                                   | CharField                 |
| Description  | description  |                                                  | TextField                 |
| Price        | price        | max_digits=6, decimal_places=2                   | DecimalField              |
| Image url    | image_url    | max_length=1024, blank=True                      | URLField                  |
| Image        | image        | blank=True                                       | ImageField                |

##### Review Model
Each product can have numerous reviews but each review corresponds to just one product. 

| Name          | Key in DB     | Validation                                               | Field Type                |
|---------------|---------------|----------------------------------------------------------|---------------------------|
| Stars         | stars         | validators=MaxValueValidator(5), null=False, default=0 | PositiveSmallIntegerField |
| Title         | title         | max_length=100                                           | CharField                 |
| Review text   | review_text   |                                                          | TextField                 |
| Date Reviewed | date_reviewed | default=timezone.now                                     | DateTimeField             |
| User          | user          | on_delete=models.CASCADE                                 | ForeignKey to User        |
| Service       | service       | on_delete=models.CASCADE                                 | ForeignKey to Services    |


#### Checkout App
This app has two models; Order and OrderLineItem. An instance of the Order model is created before any OrderLineItems, as the OrderLineItem relies on the Order as a ForeignKey.

##### Order Model
| Name            | Key in DB       | Validation                                                              | Field Type                |
|-----------------|-----------------|-------------------------------------------------------------------------|---------------------------|
| Order Number    | order_number    | max_length=32, null=False, editable=False                               | CharField                 |
| User Profile    | user_profile    | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to UserProfile |
| Full Name       | full_name       | max_length=50, null=False, blank=False                                  | CharField                 |
| Email           | email           | max_length=254, null=False, blank=False                                 | EmailField                |
| Phone number    | phone_number    | max_length=20, null=False, blank=False                                  | CharField                 |
| Country         | country         | blank_label='Country *', null=False, blank=False                        | CountryField              |
| Postcode        | postcode        | max_length=20, blank=True                                               | CharField                 |
| Town or city    | town_or_city    | max_length=40, null=False, blank=False                                  | CharField                 |
| Street address1 | street_address1 | max_length=80, null=False, blank=False                                  | CharField                 |
| Street address2 | street_address2 | max_length=80, null=False, blank=False                                  | CharField                 |
| County          | county          | max_length=80, null=False, blank=False                                  | CharField                 |
| Date            | date            | auto_now_add=True                                                       | DateTimeField             |
| Discount        | discount        | max_digits=6, decimal_places=2, null=False, default=0                   | DecimalField              |
| Order total     | order_total     | max_digits=10, decimal_places=2, null=False, default=0                  | DecimalField              |
| Grand total     | grand_total     | max_digits=10, decimal_places=2, null=False, default=0                  | DecimalField              |
| Original cart   | original_cart   | null=False, blank=False, default=''                                     | TextField                 |
| Stripe pid      | stripe_pid      | max_length=254, null=False, blank=False, default=''                     | CharField                 |

##### OrderLineItem Model
An instance of OrderLineItem is created for each unique product in the users basket. It links to the users existing Order, the relevant product and the quantity the user wishes to buy.

| Name            | Key in DB      | Validation                                                                  | Field Type            |
|-----------------|----------------|-----------------------------------------------------------------------------|-----------------------|
| Order           | order          | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey to Order   |
| Service         | service        | null=False, blank=False, on_delete=models.CASCADE                           | ForeignKey to Services|
| Service_date    | service_date   | max_length=99, null=True, blank=True                                        | CharField             |
| Quantity        | quantity       | null=False, blank=False, default=0                                          | IntegerField          |
| Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False     | DecimalField          |


#### Profiles App
This app has one model; UserProfile. Each user can have one profile and each profile links to one user. 

##### UserProfile Model
| Name                    | Key in DB               | Validation                                   | Field Type    |
|-------------------------|-------------------------|----------------------------------------------|---------------|
| User                    | user                    | on_delete=models.CASCADE                     | OneToOneField |
| Default street address1 | default_street_address1 | max_length=80, blank=True                    | CharField     |
| Default street address2 | default_street_address2 | max_length=80, blank=True                    | CharField     |
| Default town or city    | default_town_or_city    | max_length=40, blank=True                    | CharField     |
| Default county          | default_county          | max_length=80, blank=True                    | CharField     |
| Default postcode        | default_postcode        | max_length=20, blank=True                    | CharField     |
| Default country         | default_country         | blank_label='Country', null=True, blank=True | CountryField  |
| Default phone number    | default_phone_number    | max_length=20, blank=True                    | CharField     |




## Testing
GitPod's preview, google chrome developer tools, Safari developer tools  were utilised throughout the development of the project to identify and successfully address any bugs, errors or style issues affecting UX on various screen resolutions. 

### Automated Testing
[W3c Markup](https://validator.w3.org/), [CSS Validation Services](https://jigsaw.w3.org/css-validator/) and [PEP8 online](http://pep8online.com) were used to check the validity of my HTML, CSS and python code.  However, the W3c validator throws errors in the HTML files where Jinja templating syntax is found. All other code returned fine. 

### Manual Testing
After the site was deployed, I tested it across various browsers including Chrome, Safari, Internet Explorer, FireFox, and on multiple devices (Samsung Galaxy J3, iPhone 7, 8, 11 pro, iPad 3, iPad Air, MacBook Air and iMac) as well as on Responsinator to ensure compatibility and responsiveness. Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

#### Elements on every page
##### Navbar
* On desktop, confirm that the navbar displays the Brand Logo to top left, the , 'HOME", 'SERVICES', 'CLIENT PORTAL'  and 'cart' icon to the top right . 
* On mobile, confirm that the navbar displays the toggler / burger icon to top right. 
* Confirm that the 'CLIENT PORTAL' dropdown options "Register" and "Login" are visible to public users and that "My Profile" and "Logout" are not.
* Login to the site, confirm that options "My Profile" and "Log out" are visible and that "Register" and "Log in" are not.
* Add an item to the shopping cart, confirm that the  grand total is displayed. 
* Click on the cart icon and confirm that it leads you to the Shopping Cart page
* Login as a superuser, click the "My Profile" link in the navbar and confirm that 'Add Product' is also listed in the My Profile view.
* Click each link in the navbar to confirm that it leads to the correct page.


#### Home Page
* Confirm Home Page loads as expected
* Hover over call to action buttons and confirm the color changes as expected.
* Click on the 'Choose a service' button and confirm that it leads to the services results page


#### Register Page
* Try to go to the register url when already logged in, confirm that the user is redirected to the home page.
* Logout then go to the register page again. Confirm that the register form is displayed as expected.
* Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
* Fill in the email input with a non-email address, confirm the user is shown an error asking them to use an email address.
* Fill in the form with two different emails, confirm the error is caught and the user is informed of their mistake.
* Fill in the form with two different passwords, confirm the error is caught and the user is informed of their mistake.
* Fill in the registration form correctly, confirm that the user is automatically directed to the verify email page.

#### Login Page
* Attempt to login with a username not in the database, confirm the relevant error message is shown.
* Attempt to login with a correct username but wrong password, confirm the relevant error message is shown.
* Login with a correct username and password, confirm that the user is logged in and that they are redirected to the home page.
* Try to return to the login page url when already logged in, confirm that the user is redirected to the home page.

#### Logout Page
* Click the 'Logout' link and confirm that it leads to the signout page.
* Click 'Signout' button and confirm that the user is logged out of their account
* Login again and add a new product to the shopping basket. Logout and confirm that the user is logged out and their basket has been cleared.

#### Add Service Page
* Logout then attempt to navigate to the add product url and confirm that user is redirected to login page. 
* Login in to an account without superuser status, attempt to navigate to the add product url and confirm that error message is displayed alerting user that they are not authorised. 
* Login as a superuser and navigate to the add product page. Confirm that the product form and background image display as expected. 
* Hover over the form and confirm that the opacity changes as expected. 
* Click on the category field and check all product categories are listed. 
* Click on the select image button and confirm it works as expected. 
* Attempt to submit form without completing required fields and confirm validation errors. 
* Complete form correctly. Confirm success message displayed and user redirected to the new product detail page. Check details are listed correctly. 

#### Services Page
* Navigate to the 'Services' page and confirm that services are displaying .
* Confirm that the service image and details are displaying as expected, with the details underneath the image. 
* Confirm that where there is an average rating it is displayed or else the text 'no rating' is displayed. 
* On desktop view, confirm that there are four services listed in a row and that rows are separated with a transparent horizontal rule
* Confirm that the number of products listed in each row reduces as the screen size gets smaller, first down to two and than to  one service per row on mobile views. 
* Check that there are no duplicates or missing products.  
* Login as a superuser and confirm that the 'Edit' and 'Delete' links are displaying. Click the edit link and confirm that the edit service page is displayed.  
* Hover over a service image and confirm that the curser changes to a pointer. 
* Click on service images and confirm that it redirects to that specific service detail page. 

#### Service Detail Page
* Navigate to a service detail page and confirm that the page is displayed as expected. On desktop, the image should be displayed on left and service info on the right, whilst on mobile view the image is stacked on top of the service info. 
* Confirm that the Image, name, price, and description match those in the database for the service.
* Adjust the quantity using the button and confirm that the highest number available to select matches the maximum set number of 8.
* Confirm that the 'Keep Shopping' and 'Add to cart' buttons work as expected. 
* Attempt to type in a quantity above the number in stock, press enter or 'Add to cart' and confirm that validation message is received.
* Click the "add to cart" button. Confirm that the success message is launched, stating the name and quantity of the service added.
* Try to add a service without selecting a date confirm that validation message is received.

##### Reviews
* Under the product details confirm that the reviews section is displaying any previous reviews or else the text 'No reviews'. 
* Confirm that the 'write review' form is displayed for logged in users and a message "Please Register or login to leave a review." is displayed if user is not logged in. 
* Confirm that the 'register' and 'login' links work as expected. 
* Once logged in, hover over the stars in the review form and confirm that they change colour as expected.
* Click the desired number of stars and confirm that the number of stars have changed colour. 
* Try to submit the form with the title and review fields empty and confirm validation errors
* Try to submit the form without the stars selected and confirm validation error
* Complete the form correctly, click post and confirm that success message is displayed and review is now listed. Also confirm service rating has updated. 

#### Edit Service Page
* Logout, then attempt to navigate to the edit service url and confirm that user is redirected to login page. 
* Login to an account without superuser status, then attempt to navigate to the edit service url and confirm that error message is displayed alerting user that they are not authorised. 
* Login as a superuser and navigate to the edit service page. Confirm that the edit service form and background image display as expected, with the fields pre-populated with the specified service.
* Hover over the form and confirm that the opacity changes as expected. 
* Select new image, save and confirm image has been updated.
* Click to remove the image, save and confirm the image has been removed and the 'no image' pic is displayed instead. 
* Remove data from a required field, attempt to save it and confirm validation errors.
* Edit and complete form correctly. Confirm success message displayed and user redirected to the updated service detail page. Check service details are listed correctly. 

#### Cart Page
* Go to the shopping cart page with nothing added, confirm "Your cart is empty" message and 'keep shopping' button redirects to service results.
* Add items to the cart and return to the shopping cart page, confirm that all items in the cart are displayed correctly, with the correct amounts requested by the user.
* Confirm that the cart total, delivery and grand total are displaying the correct amount. 
* Adjust the quantity field, confirm that the shopping cart subtotal is updated to reflect the change.
* Click the remove link on a item, confirm that the cart is reloaded with that item removed.
* Remove all items from the cart, confirm that the shopping cart page is reloaded to reflect the empty cart.

#### Secure Checkout Page
* Navigate to the checkout page url without anything in the cart. Confirm that the user is redirected to the service results page and error message appears notifying user that cart is empty.
* Navigate to the checkout page url with items in the cart. On desktop view, confirm that the Details, Discount and Payment form are displayed on the left and order summary on the right. On mobile view confirm that the order summary is diaplayed first and that the form is stacked underneath. 
* Confirm Order Summary is diaplaying correctly
* Click the 'Adjust cart' button and confirm taht it redirects to the shopping cart page.
* Try to send the form without all the required fields filled in. Confirm that the appropriate error message is given to the user.
* Use the stripe checkout test card numbers to check the various responses to different errors.
* Complete order and confirm that user is directed to the Checkout Success page, detailing their order information. Click the "keep shopping" button, confirm that the user is taken back to the service results page.

#### Profile Page
* Go to the profile page of a newly created user. On desktop, confirm that the page loads with the forms on the left and Order History on the right. On mobile confirm that forms are stacked on top of the order history. 
* Confirm logon details form is populated with the users username and email address. 
* Confirm that password field contains asterisks and 'Edit' button. Click button and confirm that user is taken to change password page. 
* Attempt to change password using wrong password and confirm validation messgae.
* Create new password using less than 8 characters and confirm validation message. 
* Create new password similar to username and confirm validation message.
* Complete change password form as required and confirm success message received. 
* Fill in the My Delivery Information form and click update. Confirm that "Profile updated successfully" success message is shown to the user and that the reloaded form is now populated with the new data.
* Confirm that a user with no previous orders has no orders displayed in the Orders section.
* Make an order on the website, return to the profile page and confirm that the orders are displayed in date order the Order History section. Click on the order number to show the full details.
* Confirm that all data in the orders on the profile page are accurate.


### User Stories Testing
#### Registration and User Accounts 
| ID  | As a …                | I want to be able to…                              | So that I can…                                                          | Testing |
| ----| --------------------- | -------------------------------------------------- | ----------------------------------------------------------------------- | ------- |
| 1   | public user           | easily register for an account                     | have a personal acount and view my profile                              | Achieved; by clicking 'register' link from the 'My Account' navbar icon and completing the registration form |
| 2   | registered user       | receive an email confirmation after registering    | verify my account registration was successful                           | Achieved; user should find a confirmation email to verify their email address after successful submitting the form. |
| 3   | registered user       | easily log in and out                              | access my personal acount information                                   | Achieved; by selecting the login / logout links from the 'My Account' Navbar icon and completing the specified steps |
| 4   | registered user       | easily recover my password if I forget it          | regain access to my acount                                              | Achieved; users can click on the 'Forgot Password' link on the login page, enter their email address and they will then receive an email containing a link to the change password page. Users can then complete the form to select a new password |
| 5   | registered user       | have a personalised user profile                   | View my order history, order confirmation and payment information       | Achieved; by logging into your account and selecting the 'My Profile' link from the 'My Account' navbar icon, then clicking on the order number to view full details |
| 6   | registered user       | rate and review a product                          | provide feedback to store owner and other shoppers                      | Achieved; logged in users will find a 'Write Review' form including a star rating system at the bottom of the product detail page to complete. |

#### Viewing and navigation
| ID  | As a …                | I want to be able to…                 | So that I can…                                                                           | Testing |
| ----| --------------------- | --------------------------------------| ---------------------------------------------------------------------------------------- | ------- |
| 7   | site user (all users) | view a list of all services           | select some to purchase                                                                  | Achieved; users can select 'Services' from the menu in the navbar to view a list of all the services available. |
| 8   | site user (all users) | view individual product details       | identify the product description, price, image, rating and corresponding product reviews | Achieved; users can click on a product to view all the product info and any related product reviews. |
| 9   | site user (all users) | easily view total of shopping cart    | avoid spending too much                                                                  | Achieved; the grand total of the shopping cart is displayed under the basket icon in the navbar, so it can be seen from any page on the site. |

#### Purchasing and Checkout
| ID  | As a …                | I want to be able to…                                                | So that I can…                                                    | Testing |
| ----| --------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------- | ------- |
| 10  | site user (all users) | easily select the date for a service to add to my shopping cart      | purchase the amount of products I want                            | Achieved; users can select the date by using the datepicker  or by typing in the date they want. | 
| 11  | site user (all users) | view items in my cart                                                | review the items I intend to purchase and identify the total cost | Achieved; by clicking on the cart icon in the navbar. |
| 12  | site user (all users) | remove items or change the quantity of individual items in my cart   | amend my order before checkout                                    | Achieved; users can use the buttons to adjust the quantity and the click the update link below. Alternatively they can click the remove link to delete items. |
| 13  | site user (all users) | easily enter my personal and payment information                     | check out quickly with no problems                                | Achieved; the secure checkout page has a simple form to submit delivery and payment details. Delivery info can also be saved to pre-populate the form for future orders. |
| 14  | site user (all users) | feel confident that my personal data is safe and secure              | provide the information required to complete my purchase          | Achieved; users can feel assured the the checkout system is secure. |
| 15  | site user (all users) | view order confirmation                                              | verify that I haven't made any mistakes                           | Achieved; after completing a purchase, users will see a summary of their order on the checkout success page or by navigating to their profile. |
| 16  | site user (all users) | receive an email confirmation after checkout                         | Keep a record of what I have purchased                            | Achieved; after completing the order, users should find they have an email confirmation of their order. |

##### Admin and Store Management
| ID  | As a …                | I want to be able to…                                      | So that I can…                                                                     | Testing |
| ----| --------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- |
| 17  | Store Owner           | add products                                               | list items for sale                                                                | Achieved; superusers can list items for sale by clicking on the 'Add Product' link in the 'My profile"  menu and then completing the form. | 
| 18  | Store Owner           | edit / update a product                                    | adjust product details where necessary                                             | Achieved; superusers can edit products in the store by clicking the relevant 'edit' link either on the product results page or the product detail page. |
| 19  | Store Owner           | delete a product                                           | remove items that are no longer available                                          | Achieved; superusers can remove products by clicking the relevant 'delete' link either on the product results page or the product detail page. |


## Deployment
Before starting you must have Git, PIP and Python3 installed on your machine. You will also need to ensure you have created free accounts with the following services: [Stripe](https://dashboard.stripe.com/register), [AWS](https://aws.amazon.com) including setting up an [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html). Please click the links for documentation on how to set these up and retrieve the necessary environment variables.

### To run the project locally

1. Go to [my GitHub repository](https://github.com/mihai-busuioc/fresh-fairy) and click on the green 'Code' button at top right of the repository and copy the URL for the repository in the 'Clone with HTTPs' section.

2. Now open your prefered Integrated Development Environment (I used GitPod for this project) and with Git installed on your system, you can clone the repository with the following command in the terminal.

`git clone https://github.com/mihai-busuioc/fresh-fairy`

3. If needed, upgrade pip locally with
`pip3 install --upgrade pip`

4. Install all required modules with the command
`pip3 -r requirements.txt`

5. Set up the environment variables within your IDE by creating an env.py file and entering the environment variables listed below:

SECRET_KEY= "<enter_your_secret_key>"

STRIPE_PUBLIC_KEY= "<enter_your_secret_key>"

STRIPE_SECRET_KEY= "<enter_your_secret_key>"

STRIPE_WH_SECRET= "<enter_your_secret_key>"

Ensure the env.py is living in the root of your project directory and then add it to .gitignore to ensure your secret details aren't exposed. Then restart your machine to activate your environment variables or your code will not be able to see them.

6. Migrate the admin panel models to create your database template with the terminal command:
`python3 manage.py migrate`

7. Create your superuser to access the django admin panel and database with the following command:
`python3 manage.py createsuperuser`
and then follow the steps to add your admin username and password

8. Run the following command in the terminal to launch the Django project:
`python3 manage.py runserver`
Click the URL link that appears and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.

9. Once the application is running in a browser, add `/admin` to the end of the url and log in to the admin panel with your superuser account.  

10. Create instances of Products, Cocktails and Blog Posts within the new database so the local site runs as expected. 

### Deploying to Heroku
Having followed the steps above to run the project locally, you can then deploy the project to Heroku for hosting. In order to achieve this, follow the step below: 

1. Create a new app on the [Heroku website](https://id.heroku.com/login) by clicking the 'New' button on dashboard. Give the app a name and set the region to that nearest to you. 

2. Then, select the 'Resources' tab on the Heroku dashboard, search for Heroku Postgres in the 'Add-Ons' section and select the free Hobby level.

3. From the heroku dashboard, click on 'Settings' > 'Reveal Config Vars' and then add the following config vars:

| Key | Value |
| ----- | ------- |
| AWS_ACCESS_KEY_ID | <"your secret key"> |
| AWS_SECRET_ACCESS_KEY | <"your secret key"> |
| DATABASE_URL | <"your postgres database url"> |
| EMAIL_HOST_PASS | <"your secret key"> |
| EMAIL_HOST_USER | <"email address"> |
| SECRET_KEY | <"your secret key"> |
| STRIPE_PUBLIC_KEY | <"your secret key"> |
| STRIPE_SECRET_KEY | <"your secret key"> |
| STRIPE_WH_SECRET | <"your secret key"> |
| USE_AWS | True |

4. Migrate the database models using the command `python3 manage.py migrate` in the terminal.

5. Create a superuser using the command `python3 manage.py createsuperuser` and entering a username and password.

6. Create a `Procfile` file  with the command `echo web: python app.py > Procfile`

7. Commit the code to a local Git repository using the `git add` and `git commit -m 'message'` commands. 

8. Push the code to the [GitHub repository](https://github.com/mihai-busuioc/fresh-fairy) using `git push`, initalise the heroku repository using `heroku git:remote -a your_app_name` and then push to Heroku using `git push heroku master`.

9. From the heroku dashboard click on 'Deploy' > "Deployment method" and select GitHub, ensuring you confirm the correct GitHub repository and then select 'Enable Automatic Deploys'. 

10. Once the app has finished building, click the 'Open App' button provided.

11. Add `/admin` to the end of the website url, log in to the admin panel with your superuser account and then create instances of Products, Cocktails and Blog Posts within the new database to the site runs as expected. 


## Credits

### Content
* The product images and detail were taken from [FreshFairy](http://freshfairy.ro/).

### Media
* All other photographs used throughout this site were found on [FreshFairy](http://freshfairy.ro/).

### Acknowledgements

This YouTube video tutorial,  <a target="_blank" href="https://www.youtube.com/watch?v=4mfPjGb6y84">CSS Star Rating System - No JavaScript by UM Tutorial</a> was used to create the CSS Star Review system for this project. 

I have also made use of a number of websites in my pursuit to wire the all the functions necessary for this app, but particularly
* [Stack Overlflow](https://stackoverflow.com/)
* [W3School](https://www.w3schools.com/)


**This is for educational use.** 