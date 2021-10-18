# Testing

## Code Validation
- [W3C Mark-up Validation](https://validator.w3.org/) was used for checking for validity of html. There were [no errors](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/validation/html%20validation.jpg) or warnings in any of the HTML files.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used for checking errors in the CSS. There were [no errors](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/validation/CSS%20validation.jpg) in the CSS files. 
- [JSHint](https://jshint.com/) was used to check for validity of the JavaScript. There were [no errors](https://github.com/HinaChoudhry/Pawfect-Pets/blob/main/readme_images/validation/js%20validation.jpg) in the JavaScript files. 
- For Python code, I used the in-built Gitpod linter to validate code. There are three warnings which I have not addressed for the following reasons. For lines that were too long in the migration files, these have been created by Django and the issue has been marked as a "won't fix" by the Django Team. For avoiding using null=True on string-based fields - this is to avoid having two values for a field if left blank, but as blank values are needed for forms, null affect the database storage. The unused imports are still required as they link up other parts of code that is needed for the code to work. 

## User Story Tests

As a user 
- I want to be able to search for products 
    * Users are able to search for products via the search bar

- I want to be able to see the number of products found in a search result – 
    * The search result displays how many items have been found within a search

- I want to be able to navigate the website easily – 
    * There is a navbar with links for navigation to significant pages of the website. This navbar also shrinks down into a hamburger menu. The colors and fonts of the website were also carefully considered for readability 

- I want to be able to see a list of products 
    * All products are displayed on the Products page. These can be displayed, sorted by price, alphabetically and category if the user wishes. The products are also viewable, separated by category if the user clicks the relative Dog, Cat or Small Animal links. 

- I want to be able to see a further detailed summary of each product with descriptions, price and reviews
    * A product details page is part of the website. In this, there is a larger image of the selected product as well as name and description. The product details page also allows the user to purchase certain quantities of the product, and there is also a section of user reviews, with the ability to leave a review on the product’s page as well. 

- I want to be able to register an account for myself
    * Users are able to register themselves for an account. 
 
- I want to be able to log back into my account once I have registered
    * Users details are saved and they are able to log back in once they have registered. 

- I want to be able to write reviews for products
    * Users can write product reviews for any of the products but log in is required for this. 

- I want to be able to edit and/or delete reviews I have written
    * Users have the ability to edit and delete their own reviews as well but not other users. Log in is required to edit/delete reviews.

- I want to be able to see my previous orders and reviews
    * Users can see their default delivery details and order and review history on the ‘My Profile’ page. This gives a summary of previous orders and reviews with a more detailed delivery section. 

- I want social media links for the website so I can follow them
    * The footer contains social media links that open up into new tabs. 

- I want to be able to purchase products
    * Users can make ‘purchases’ via the website using the Test Stripe payment details. 

- I want to be able to select the quantity of products that I want to purchase 
    * The quantity of a product can be selected, ranging from 1-99. 

- I want to be able to view all of the items in my shopping bag before proceeding to the checkout
    * Users are brought to the shopping bag page before going to checkout. This page details a summary of the products that are currently in the shopping bag, which are to be purchased. 

- I want to be able to sort products by category, A-Z, price and by name
    * There is a sorter on the products page that allows users to sort by category, A-Z, price and by name. 

- I want to be able to view blog posts on the website
    * Users are able to view blog posts on the website on the Blog page and in more depth on the Blog detail page. 

- I want to be able to comment on blog posts
    * Logged in users are able to comment on individual blog posts 

- I want to be able to edit/delete my comment on the blog posts 
    * Registered users can amend and delete their comments on blog posts 

As an admin 
- I want to be able to add a product to the website
    * The admin can add a product to the website, with details and images being uploaded for the product. 

- I want to be able to edit/update a product
    * The admin can make amendments to individual products and save these changes to the product detail page. There is an edit button on both the product and products detail page to edit the product. 

- I want to be able to delete products
    * The admin is able to delete products from both the products page and product details page. 

- I want to be able to post blog posts
    * The admin is able to add a blog post to the website, including an image to go along with the post. 

- I want to be able to edit blog posts
    * The admin is able to amend previously written blog posts and save these changes made to the post. 

- I want to be able to delete blog posts
    * The admin is able to delete blog posts. 


## Manual Testing 

The website was manually tested for functionality and to see if apps worked as they should. 
### Home Page

- The search function searched for products via keyword and successfully returned results based on names and descriptions of products. 
- The “Shop Now – Dog/Cat/Small Animals” buttons successfully redirects the user to relevant products sorted by category according to which ‘Shop now’ button has been clicked. 
- Cart button redirects the user to their shopping cart with the correct number of items in the bag shown (or an empty cart shown if no items have been added). 
- The Account button results in a drop down of “my profile” and “logout” to the user, or “product management” as well if an admin user. 


### Shopping Bag

- On adding products to the shopping bag, items were correctly displayed in the pop up bag and in the bag on the actual shopping bag page
- Users are able to remove/edit products in their shopping bag as they like 
- Users are able to navigate to the checkout page via the “Secure checkout” button successfully

### Checkout 

- A test order was done to ensure the functionality of the checkout app was working correctly. 
- The correct items and quantity of items in the summary for the checkout page was displayed. 
- The test payment for the order was successful. 
- The order was added to the admin section of the website as well. 

### Products 

- As an admin, I was able to add, edit and delete products from the “Product Management” tab. 
- I was also able to edit and delete products from the “edit” and “delete” buttons on the product page. 
- I was able to edit and delete products from the “product detail” page. 
- Users can increase and decrease the quantity of a product in the shopping bag on the products detail page. 
- I was able to use the “sort by” function on the products page and successfully sort products by name, price and category. 

### Reviews

- I was able to add a review to products as a logged in user 
- I was able to edit my review and save the changes made to my review
- I was able to delete my own review
- I was unable to edit or delete other people’s reviews on products, which is the correct functionality. 

### Blog 

- As an admin, I was able to add, edit and delete blog posts. 
- As a logged in user, I was able to comment on individual blog posts. 
- I was able to edit and delete my own comments on blog posts. 

### My Profile

- I was able to see my delivery/payment information was correctly saved to my profile and also see a summary of my previous orders and review comments on my profile page. 


## Responsiveness

### Home Page 
#### Desktop 
On desktop, the Home Page spans the whole width of the viewport. The navbar is full, with there being a search bar, navbar text, account button and cart button as well as links to different sections of the website. Underneath, there is a hero image and hero text that again span the width of the viewport on desktop and under this there are 3 smaller images. These 3 images are displayed side by side and each contain a “shop now” button in the center of the image. The footer is divided into 3 sections with “About Us”, Social media links and Extra Reading sections that are again displayed side by side in a row. 

#### Tablet 
In the tablet viewport, in the landscape position, the navbar is the same as the desktop viewport, but in the portrait position, the navbar links have transformed into a hamburger menu and the search bar has turned into a search icon. The account and card button are still the same. 
The hero image and text are still displayed across the page but the 3 images that were in a row are now stacked on top of one another in a column. The footer is smaller but the information displayed is in a row as per the desktop viewport. 

#### Mobile 
The navbar is similar to the tablet viewport, with the width of it being the only difference. The hero image and text have shrunk down to fit the viewport and the 3 images are again, stacked on top of one another. The footer information is now also stacked onto each other rather than spanning across the screen. 

### Shopping Bag

#### Desktop 
On the left of the page is the product image and name, with the price and quantity on the right. If there is more than one product, the products are displayed in a list as just described. Under the products, on the right side of the page is the grand total with buttons underneath to keep shopping or to go to the checkout. 

#### Tablet 
On the tablet viewport, the layout is similar to the desktop with the image and product name being on the left and the price, quantity and grand total being on the right in a row. 

#### Mobile 
The image scaled down to the mobile viewport and the rest of information has also scaled down. 

### Checkout 

#### Desktop 
For the checkout page, the delivery section is on the left half while the summary of the products to be bought are on the right. These are side by side on the desktop viewport. 

#### Tablet 
On the tablet viewport, the summary of items to be bought is now stacked on top of the page and the delivery details section is underneath this so that they are be easily viewed by scrolling down the page. 

#### Mobile 
The layout of the checkout page on mobile view is similar to that of the tablet view with the order summary being at the top of the page and the delivery information form being underneath. 

### Products 

#### Desktop 
The navbar is full across the viewport, with the search bar being displayed along with the navbar text, icons and links. On the Products page, the product images are displayed with their names and prices. These products are displayed in columns of 4 on the desktop viewport. The footer is again divided into 3 sections of information, with these sections being displayed side by side. 

#### Tablet 
In the portrait position, the navbar has shrunk down to the hamburger menu and the icons rather than the full navbar and the products are displayed in columns of 2, side by side. The footer information is still displayed with the 3 sections being laid out side by side. In the landscape position, the navbar is full and like the desktop view but the products are in columns of 3 rather than 2 while the footer information is still the same as portrait mode. 

#### Mobile 
On the mobile viewport, the navbar collapses down to a hamburger menu and the navigational buttons. The products displayed are now in a column of 1, with the products being stacked on top of one another and the footer is the same. The 3 sections of information within the footer are also stacked up onto one another. 

### Product detail

#### Desktop
The product details page is split into 3 key pieces of the page. The product information, the reviews section and the “add a review” section. At the top of the page, there is a larger image of the product on the left of the page, while there is a name, description, price, category and quantity selector as well as buttons to the right side of the larger image. Underneath this s the reviews section. The reviews sections has the information inside it stacked up so the title is on one line, then the comment, then the username and date etc. Under this, there is  a form to leave a comment at the bottom of the page. 

#### Tablet 
The tablet view of the product detail page is very similar to the desktop view, with the information being split into 3 main sections. The product image and information are still side by side in the first row, then the reviews section is displayed in the second row and finally the form to leave a review is displayed on the third row. 

#### Mobile 

The layout for the product details page differs slightly on the mobile view. The product information section is not side by side anymore. Rather, the image of the product is displayed with the product information being underneath the image. The quantity selector and shopping buttons are displayed underneath this and then the reviews section and reviews form are stacked below. 

### Blog

#### Desktop  
The Blog page is split into two main sections – the blog container and the “add blog post” form. These are stacked up on another in rows. 

#### Tablet
The layout for the blog page on the tablet view is the same as the desktop, with the page being scaled down to match the size of the viewport. 

#### Mobile 
The mobile view for the blog page is also the same as the desktop and tablet views, with the page being scaled down to the fit width of the viewport. 

### Blog detail

#### Desktop
The Blog detail page has the title, image and blog content on its page, stacked on top of one another so that the image can be large rather than being in a row and having to shrink the image. 
The Comments sections below this, and under that, is the Add a Comment form. 

#### Tablet 
The layout for the tablet viewport is similar to the desktop, with the image being responsive and scaling down to the smaller screen. The rest of the page has also scaled down but is still on top of one another. 

#### Mobile 
The mobile layout for the blog detail page is similar again with the sections scaling down to fit the viewport but still being stacked on top of each other. 

### My Profile

#### Desktop 
On the desktop view, the profile page is split into 3 sections – default delivery information, order history and review history. These are displayed next to each other in one row in this viewport. 

#### Tablet 
On tablet, in the landscape position the profile page is the same as the desktop but in the portrait position, the layout changes. The 3 sections are now stacked onto one another, with the default delivery info being at the top, order history in the middle and review history at the bottom. 

#### Mobile
The layout on the mobile viewport is  similar to that on the portrait position with the profile sections being again, stacked up rather than being displayed in a row. 

## Browser Compatibility 

### Google Chrome
The website was built using Google Chrome and functionality has been tested on Chrome with the use of DevTools. The site is fully responsive and there are currently no bugs found (except for the one mentioned below).

### Firefox
The website was also responsive in Firefox with no bugs being found while browsing the website. 

### Microsoft  Edge
The website was again responsive on Microsoft Edge with no bugs found. 

## Bugs and solutions
- Hero text from index.html not appearing properly 
    * Removed the fixed top to allow it to be visible on the webpage

- Mobile navbar and desktop navbars were not displaying correctly 
    * Added the relevant closing div tag to correct this

- Mobile navbar was pushing images down below it rather than overlaying over them when clicked 
    * Changed position to absolute and gave the navbar a z-index in order to fix this 

- Links were not clickable
    * Removed the “data toggle” attribute from the links to enable clicking/dropdown functionality. 

- Stripe Country selector was not allowing users to correctly select which country they are in, instead only using a 2 letter term eg GB/UK. 
    * Changed the checkout model and form for the country field to a dropdown selection list instead of a charfield

- Form submission for reviews not working 
    * Resolved by correcting a misspelling in the reviews views.py

- Reviews were not rendering once submitted
    * Added “review=” and “review:review” to the product_detail function in the product views.py

- Changes made the to user reviews were not saving 
    * Resolved by swapping the order of “review_id” and “product_id” in the edit_review function in views.py, to match the order of the ids in the urls.py 

- Reviews were not deleting – 
    * Added “<int:review.id>” to the delete url path. 

- Edit and delete buttons were made for users to be able to delete and edit only their own reviews but the if statement written was hiding them for all users
    * Resolved by adding “userprofile” to the end of 'review.user  = review.user'

- When creating the blog template to post blogs, “blogpost” in the add_blog_post function in views.py was undefined
    * Resolved by importing model into the views.py

- Blog posts were not rendering 
    * Removed “args=blogpost.id” in the add_blog_post function to resolve this. 

- Users not able to edit blog comments 
    * Had to update  the url link to 'comment.id' rather than 'blogcomment.id'

- The 'Free Delivery' Banner was overflowing from the right side of the viewport
    * Resolved by adding a 'container-fluid' class div to the row and col

- The Blog and Blog Detail pages width was overflowing to the right side of the viewport
    * Resolved by adding a 'container-fluid' class div to the Blog row and col divs and to the Comments section in the Blog Detail template. 

- The add_review and edit_review templates were overflowing the viewport as well on the right side. 
    * The class 'container-fluid' was added in an extra div to resolve this. 

- When there were more than two comments on a blog post, the formatting was incorrect. 
    * Resolved by moving the location of the 'endfor' tag within the code.
    
## Unresolved bugs
- When trying to add a product via the Product Management tab, uploading a product without an image results in an error. However, if you navigate and search for the product just uploaded, it shows the product has been successfully uploaded but with the 'no image' image. 