# Milestone Project 4 – Pawfect Pets

My fourth and final milestone project is for Pawfect Pets, a full stack e-commerce website for pet toys. It contains a homepage, products page, product detail page, shopping bag, checkout page, user profile page and a blog page. This is a full stack e-commerce website using HTML, CSS, JavaScript, Python and the Django Framework. The aim of the website is to sell products to potential customers and have them regularly use the site as a means of buying pet toys for their pets. 
[Pawfect Pets](https://pawfect-pets.herokuapp.com/) 
Please note that the card payment details for Stripe should be entered as 4242 recurring as otherwise, it will show as invalid card details. 


# Table of contents

1. [UX](#ux)

    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Design](#design)
    * [Font](#font)
    * [Colours](#colours)

2. [Features](#features)

3. [Database](#database)

4. [Testing](#testing)

5. [Technology used](#technology-used)

6. [Deployment](#deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)
    

## UX <a name=”ux”></a>
The website is for pet lovers who want to buy toys for their pets. The site caters to dogs, cats and small animals currently with appropriate toys. The overall layout chosen was to attract users to the website without it looking too busy and without there being too much for the user to look at, at one time. 

### User Stories <a name=”user-stories”></a>

As a user 
- I want to be able to search for products
- I want to be able to see the number of products found in a search result
- I want to be able to navigate the website easily
- I want to be able to see a list of products 
- I want to be able to see a further detailed summary of each product with descriptions, price and reviews
- I want to be able to register an account for myself 
- I want to be able to log back into my account once I have registered
- I want to be able to write reviews for products
- I want to be able to edit and/or delete reviews I have written
- I want to be able to see my previous orders and reviews
- I want social media links for the website so I can follow them
- I want to be able to purchase products
- I want to be able to select the quantity of products that I want to purchase 
- I want to be able to view all of the items in my shopping bag before proceeding to the checkout
- I want to be able to sort products by category, A-Z, price and by name
- I want to be able to view blog posts on the website
- I want a FAQ section to see information about the website
- I want to be able to read a blog
- I want to be able to comment on the blog
- I want to be able to edit/delete my comments on the blog

As an admin 
- I want to be able to add a product to the website
- I want to be able to edit/update a product
- I want to be able to delete products
- I want to be able to post blog posts
- I want to be able to edit blog posts
- I want to be able to delete blog posts

### Wireframes <a name=”wireframes”></a>

The Balsamiq programme was used to create my wireframes for my project. Building the wireframes before starting to build my project allowed me to plan what I was aiming to make and also allowed me to discuss the layout of the website with my mentor in advance. 

Desktop Wireframes

- [Blog]( https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Blog%20Desktop.png)
- [Cart]( https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Cart%20Desktop.png)
- [Checkout](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Checkout%20Desktop.png)
- [Homepage](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Home%20page%20Desktop.png)
- [Log In](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Log%20In%20Desktop.png)
- [Product Item](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Product%20Item%20Desktop.png)
- [Products](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Products%20desktop.png)
-  [Sign Up](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Sign%20Up%20Desktop.png)
- [Successful checkout](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/Successful%20Checkout%20Desktop.png)
- [User Profile](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/desktop/User%20Profile%20Desktop.png)

Tablet Wireframes

- [Blog](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Blog%20Tablet.png)
- [Cart](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Cart%20Tablet.png)
- [Checkout](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Checkout%20Tablet.png)
- [Homepage](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Home%20page%20Tablet.png)
- [Log In](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Log%20In%20Tablet.png)
- [Product Item](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Product%20Item%20Tablet.png)
- [Products](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Products%20Tablet.png)
- [Sign Up](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Sign%20Up%20Tablet.png)
- [Successful checkout](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/Successful%20Checkout%20Tablet.png)
- [User Profile](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/tablet/User%20Profile%20Tablet.png)


Mobile Wireframes

- [Blog](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Blog%20Mobile.png)
- [Cart](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Cart%20Mobile.png)
- [Checkout](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Checkout%20Mobile.png)
- [Homepage](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Home%20page%20Mobile.png)
- [Log In](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Log%20In%20Mobile.png)
- [Product Item](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Product%20Item%20Mobile.png)
- [Products](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Products%20Mobile.png)
- [Sign Up](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Sign%20In%20Mobile.png)
- [Successful checkout](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/Successful%20Checkout%20Mobile.png)
- [User Profile](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/mobile/User%20Profile%20Mobile.png)


### Design <a name=”design”></a>
For my third milestone project, I received some constructive criticism that there was too much going on visually with the website and that it was a bit much and so for this project, I decided to go with a simplistic theme, somewhat similar to that of my first milestone project. Instead of adding images as wallpapers, I added smaller, individual pictures to different pages with a white background so that these pictures would add some colour to the pages, rather than adding loud backgrounds. I also wanted to add a touch of playfulness to the site to mirror the playful nature of animals, done so with the use of animal imagery. 


### Font <a name=”font”></a>
I used Google Fonts for my project and have used DM Serif Text for the navbar logo text while the rest of the website uses Quicksand. Again, from my third milestone project I was advised to not use overly-cursive fonts as they made reading some of the text difficult. I chose Quicksand as the main font used throughout the site as I felt it was a readable, yet playful text and brought the element of simplicity to the fonts. This was paired with Dm Serif Text for the main nav logo text as I felt it was bold and immediately drew the user to the text, therefore indicating what the website is about. 

### Colors <a name=”colors”></a>
The colours of the website were chosen in order to keep the design simple, yet attractive. From looking at different e-commerce websites, I noticed that many used a palette of white and black with one more colour and so I decided to do something similar. For my palette, I went for #000, #FFF, #88daf3 and #d9f3f57e; which is black, white, bright blue and a calm blue. Initially, I went with green instead of blue but it resembled the Pets At Home website too much so I changed this for the blue. 

## Features <a name=”features”></a>
### Existing Features

### Homepage
The homepage is the first page that appears when the user enters the website. It contains a ‘free delivery’ banner at the very top of the page, with a main navbar below. Underneath the main navbar there is a hero image with hero text laid over it of different animals with a simple, white background so it isn’t too noisy. Below this, there are 3 images of animals with “Shop Now” buttons on each image, redirecting the user to the specific animal’s category based on the button they click. These images are side by side on larger viewports but stack on top of one another on smaller viewports. 
Under this, there is a footer with basic information about the fictional company and social media links, as well as a link to the FAQ page. 

### Navbar
The main navbar has the name of the website centralised and at the top, with a search bar on the left and profile and cart links to the right. Underneath this, there are links to products, differing in all products, dog, products, cat products and small animal products. There is also a link for the blog here. The navbar collapses down on mobiles, shrinking into a hamburger menu with a search icon, profile icon and cart icon that are all clickable. 

### Footer
The footer is divided into 3 columns with each column containing different text for differing areas of the website. On the left, there is an “About Us” paragraph that gives a description of what the website is aiming to do. In the middle section, there are social media links for different websites and the right column has a link to the FAQ page. 

### Products Page
There is a h1 at the top of the products page and below there are cards of the products in a number of columns, based on the viewport. On desktop, the cards show in rows of 4, tablet – in 3 and on mobile – 2 or 1 depending on the screen. The Products page initially shows all the products, but these can be either narrowed down to dog, cat or small animal products or can be sorted by certain criteria. 
On each card, there is an image, name, price and category of each product and these cards can be seen in more detail on the Product Details page. 

### Product Details Page
The Products detail page has a more in depth look at the selected product. The image here has gotten larger and there is now a description for the product visible as well. Under the product details, such as price, name and category, there is a ‘quantity’ box which allows the user to select the number of the item that they want to purchase and then there is an ‘Add to cart’ button. 
Below these, there is a reviews section where users can read and upload reviews of products. 

###  Shopping Bag Page
The shopping bag page shows a summary of items that have been added to the shopping bag and the option to update the quantity, or remove the item completely from the bag. The page also gives a summary of price of items, subtotal, delivery and a grand total. There are 2 buttons below this to either continue shopping or checkout securely. 

### Checkout Page
The checkout page has a form on the left and an order summary on the right of the page. The form is there for the user to input their personal details such as name, delivery address and payment details in order to place the final order. 

### Log In Page
The log in page is a simple form with fields for the user’s username/email address and password, in order for them to gain access to their personal accounts. 

### Sign In Page
The Sign in Page is similar to the login, with it being a simple form. Although, the user can register here by filling in the fields of email address, email confirmation, username, password and password confirmation. 

### Order Confirmation
The order confirmation page appears when an order has been successfully fulfilled. It contains h1 of ‘Order Confirmation’ and then a summary below of the items purchased. Below this there are buttons to continue shopping or to view previous orders. 

### User Profile Page
The Personal profile page welcomes the user back, with previous orders and previous reviews being available to view. 

### Blog Page
The Blog page gives a taster of what blogs are available for users to read, with the title and introduction of the blog being visible here. If the user wishes to read a full blog post, there is a ‘read more’ link that redirects the user to the full article. The Blog page also allows superusers to upload new blog posts via a form. 

### Blog Detail Page

The blog detail page is where users can read blog posts in full as well as leave comments. The Blog Detail page includes a related image to the blog post, a title, author, date posted and text sections. Logged in users can also leave comments here on the blog post. 

## Database schema  <a name=”database”></a>
![db schema](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/database/database%20schema.png)


## Technologies Used  <a name=”technology-used”></a>
- [HTML](https://en.wikipedia.org/wiki/HTML) To enable the basic building on the website.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) for styling the website 
- [JavaScript](https://www.javascript.com/) for the interactivity  
- [Bootstrap](https://getbootstrap.com/) for structure, responsiveness and pre-made classes. 
- [GitHub](https://github.com/) Where I can have my repository saved for my project. 
- [Gitpod](https://www.gitpod.io/) My preferred IDE for building the website.
- [GIT](https://git-scm.com/) for version control.
- [Google Fonts](https://fonts.google.com/)   to choose and use different fonts for the website.
- [Font Awesome](https://fontawesome.com/)   For different icon elements used.
- [jQuery](https://jquery.com/) and [Popper.js](https://popper.js.org/) To use alongside Bootstrap.
- [Python](https://www.python.org/)For the backend functionality of the wesite
- [Django]( https://www.djangoproject.com/) as the Framework and for back-end coding. 
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) – For the account functionality of the project. 
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Used for all forms in the website
- [Stripe](https://stripe.com/) For the payment section
- [Heroku](https://signup.heroku.com/) For deployment of the website
- [AWS](https://aws.amazon.com/) For storing images and static files from the website. 
- [Balsamiq](www.balsamiq.com) To create wireframes for the website.  
- [DBDiagrams](dbdiagrams.io) to the build the database schema 
- [Imgur](imgur.com) to host the image_urls for the product model




## Testing  <a name=”testing”></a>
Testing information can be found at [TESTING.md]( https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/TESTING.md).

## Deployment  <a name=”deployment”></a>


### Deployment to Heroku

To deploy the website to Heroku the following steps were taken. 

* Create an app on Heroku - 

    * Click on the ‘new’ button
    * Click on the ‘new app’ link
    * Name the app and choose the region closest to you
    * Select ‘create app’

* Set up the postgres database
    * Go to app resources section in Heroku, search for postgres
    * Add the chosen project and choose the free plan
    * Install dj_database_url and psycopg2 in GitPod using the command ‘pip install’ 
    * Add the dependencies to the requirements file by typing in ‘pip3 freeze > requirements.txt’
    * Import dj_database_url in the settings.py 
* Comment out the current database settings and replace with the postgres database (this is an environmental variable and should not be shown in version control).
    *Next, in order to migrate the models to the new database use the command – ‘python manage.py migrate’
* Set up a superuser using the command – “python3 manage.py createsuperuser”
    * Commit the changes making sure not to include the environmental variables in version control. 
    * Then, I created an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and otherwise use the default database in gitpod.
    ```
    if "DATABASE_URL" in os.environ:
            DATABASES = {
                "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
    ```
* The postgres database should now be ready for use.




* To tell Heroku the app is a web app, the following steps were taken -   
	* Install Gunicorn by using the command ‘pip3 install Gunicorn’      
    * Create a Procfile by using the command ‘touch Procfile’
    * In the Procfile, it needs to know to use a webserver – use the command - 
        “web: gunicorn <appname>.wsgi:application”
	* Next, connect Heroku to the GitPod terminal by using the following command – ‘heroku login -I’
	* Log in with the email and password used to create an account on Heroku.
    * then, I disabled the collection of static files temporarily until AWS has been set up.
        * `heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>`
        * the --app command is used when you have more than one app in your heroku account


In Settings, add Heroku to the list of allowed hosts and localhost using the following - 
`“ALLOWED_HOSTS = ["<heroku appname>.herokuapp.com", "localhost"]”`
* Push the changes to GitHub
* Then push the Heroku by using `heroku git:remote -a <heroku appname>`
* Push the app to GitHub using -`git push heroku master` and Heroku should now build the app.

    
* Next, On the Heroku Website, go the deploy selection of the relevant app 
* When selected and connect click ‘enable automatic deploys' and GitHub should now automatically push changes to Heroku too
    
* Amazon AWS was used to store both static and media files of the website –
* Create an AWS Account and/or sign in
    * To create a bucket search for the aws s3 service
    * Click on ‘create bucket’
* Name the bucket and select your region, unchecking ‘block public access’ and also acknowledge the bucket will be public. 
    * click create bucket.
        * Amend the Bucket settings as such - 
        * Go to the bucket Properties section and turn on static web hosting
        * In the index and error text inputs add index.html and error.html, then click ‘save’.  
                
* Next, go to the bucket Permissions section.
* In the cors config paste in the below:
```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposedHeaders": [

            ]
        }
    ]
```
    * In bucket policy, click “generate policy”
    * Select S3 bucket policy
    * Add * to the field to select all principals
    * select action to get object
    * Paste in your ARN (found on the bucket policy page)
    * click “add statement” then the “generate policy button”
* Copy and paste the new policy into your bucket policy, adding /* to the end of the resources key and click ‘save’. 
                  
    * Go to the Access Control List section.
    * Set list objects permission to “everyone.”
	* On the admin page for AWS, search “IAM” to add a new user
	* Create a new group by clicking “new group” and give it a name
	* Create a group policy by clicking “policy” and then “create policy”
	* Search for s3 and select Amazon3fullaccess and then import. 
	* Past in the ARN used in the resources section and click “review policy”
	* Fill the name and description and click “generate”
	* Then, click “permissions” and attach the policy.
	* To create a user, select users and click on “add user”
	* Create a username and select “programmatic access” then “next”. 
	* Select the group and click “create user”. 
	* Download the CVS file
	* Connect to Django by installing two packages to the IDE with the commands - 

    ```
                pip3 install boto3
                pip3 install django-storages
              ```
* Add these to the requirements.txt with the command - `pip3 freeze > requirements.txt`

USE_AWS, an environmental variable needs to be set up to run code on Heroku. The settings should be as below in settings.py - 
```
    if "USE_AWS" in os.environ:
        # Bucket configurations
        AWS_STORAGE_BUCKET_NAME = "bucket name"
        AWS_S3_REGION_NAME = "bucket region"
        AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") 
        AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") 
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # static and media files
        STATICFILES_STORAGE = "custom_storages.StaticStorage"
        STATICFILES_LOCATION = "static"
        DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
        MEDIAFILES_LOCATION = "media"

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```
* Back in heroku click on settings tab and then click reveal config vars.
* Then set up the environmental variables as required.
* Back in the IDE, we need to create a custom storages.py to tell django that in production we want to use Amazon S3 to store our static and media files
* import S3Boto3Storage at the top of the custom_storages.py file.
* Set up classes to tell django where to store the files as shown below:
    * ```
                class StaticStorage(S3Boto3Storage):
                    location = settings.STATICFILES_LOCATION
                
                class MediaStorage(S3Boto3Storage):
                    location = settings.MEDIAFILES_LOCATION
              ```
    * push all the changes to Github 
    
    * Add Media files to AWS
        * in your AWS bucket, create a new folder called media
        * select “upload” and upload your image files, then select “grand public access”. 
	* Next, click “upload”       

 

### Setting the project up locally

* Find your github repository and on the dropdown menu click “Download zip”, then extract the files to your repository. 
            
* Open your IDE and open the folder containing the code and download the requirements needed to run the project with the command -` pip3 install -r requirements.txt `
* Next, set up the below environmental variables - 
    ``` DJANGO_SECRET_KEY = *YOUR SECRET KEY*
    STRIPE_PUBLIC_KEY = *YOUR STRIPE PUBLIC KEY*
    STRIPE_SECRET_KEY = *YOUR STRIPE SECRET KEY
    STRIPE_WH_SECRET = *YOUR STRIPE WEBHOOK SECRET KEY*
    IN_DEVELOPMENT = True
    ```

* Migrate your database model with the following 4 commands –
	
    * `python3 manage.py makemigrations --dry-run`
            
    * `python3 manage.py makemigrations`
           
    * `python3 manage.py migrate --plan `
            
    * `python3 manage.py migrate`

* Next, create a superuser with the command - 
        ` python3 manage.py createsuperuser `
    * enter your own username and password
    * Run the app if you now like with the command “python3 manage.py runserver”. 




## Credits  <a name=”credits”></a>
### Images
The images used for this website were obtained from [Shutterstock](www.shutterstock.com) and  [Unsplash](www.unsplash.com) except for the product images. These were obtained from [Amazon](amazon.co.uk)
### Content 
The blog articles were taken from [Pets at Home Pet Talk articles]( https://www.petsathome.com/pet-talk) and the product titles, descriptions and prices were all slightly amended versions of products on [Amazon](amazon.co.uk).
### Code

This website was made following the Code Institute Boutique Ado tutorial videos by Chris Zielinski. I used these videos as guidance to build my website and built on these tutorials. 


### Acknowledgements
I would like to thank my mentor, Precious Ijege, for his time, advise and comments in working with me to build my project. As this is my final project with Code Institute, I would like to further thank Precious for his guidance and mentorship throughout the whole course and for helping me get to a stage where I have submitted all four milestone projects. 
 I would like to thank the Code Institute Slack forum for all their help and in particular the #peer-review-code channel for the input for my project and the #full-stacks-framework channel for helping with bugs and general advice. I would also like to thank the tutors at Code Institute for their help, guidance, advice, time and patience throughout the whole course.  
## Disclaimer  <a name=”disclaimer”></a>
The content and images on this website are for educational purposes only.
