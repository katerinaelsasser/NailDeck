# Nail Deck [![Build Status](https://travis-ci.org/katerinaelsasser/NailDeck.svg?branch=master)](https://travis-ci.org/katerinaelsasser/NailDeck)

Nail Deck is an online website for selling hand made nail polishes to customers. Their polishes are inspired by pirates which includes the names of the products.

## Content

- [UX](https://github.com/katerinaelsasser/NailDeck#ux)
  - [Aim](https://github.com/katerinaelsasser/NailDeck#aim)
    - [Target Audience](https://github.com/katerinaelsasser/NailDeck#target-audience)
    - [Visitor Goals](https://github.com/katerinaelsasser/NailDeck#visitor-goals)
    - [Online Shop Goals](https://github.com/katerinaelsasser/NailDeck#online-shop-goals)
  - [Strategy](https://github.com/katerinaelsasser/NailDeck#strategy)
  - [Structure](https://github.com/katerinaelsasser/NailDeck#structure)
  - [Skeleton](https://github.com/katerinaelsasser/NailDeck#skeleton)
  - [Scope](https://github.com/katerinaelsasser/NailDeck#scope)
  - [Research](https://github.com/katerinaelsasser/NailDeck#research)
  - [User Stories](https://github.com/katerinaelsasser/NailDeck#user-stories)
    - [Site User](https://github.com/katerinaelsasser/NailDeck#site-user)
    - [Site Owner](https://github.com/katerinaelsasser/NailDeck#site-owner)
  - [Surface](https://github.com/katerinaelsasser/NailDeck#surface)
  - [Design Choices](https://github.com/katerinaelsasser/NailDeck#design-choices)
    - [Overall](https://github.com/katerinaelsasser/NailDeck#overall)
    - [Fonts](https://github.com/katerinaelsasser/NailDeck#fonts)
    - [Icons](https://github.com/katerinaelsasser/NailDeck#icons)
    - [Colours](https://github.com/katerinaelsasser/NailDeck#colours)
    - [Images](https://github.com/katerinaelsasser/NailDeck#images)
  - [Wireframes/Flowchart](https://github.com/katerinaelsasser/NailDeck#wireframesflowchart)
- [Features](https://github.com/katerinaelsasser/NailDeck#features)
  - [Existing Features](https://github.com/katerinaelsasser/NailDeck#existing-features)
  - [Future Features](https://github.com/katerinaelsasser/NailDeck#future-features)
- [Information Architecture](https://github.com/katerinaelsasser/NailDeck#information-architecture)
  - [Database choice](https://github.com/katerinaelsasser/NailDeck#database-choice)
  - [Data Models](https://github.com/katerinaelsasser/NailDeck#data-modals)
- [Technologies Used](https://github.com/katerinaelsasser/NailDeck#technologies-used)
  - [Languages](https://github.com/katerinaelsasser/NailDeck#languages)
  - [Databases](https://github.com/katerinaelsasser/NailDeck#databases)
  - [Liabries](https://github.com/katerinaelsasser/NailDeck#libaries)
- [Testing](https://github.com/katerinaelsasser/NailDeck#testing)
  - [Planning](https://github.com/katerinaelsasser/NailDeck#planning)
  - [Testing Features](https://github.com/katerinaelsasser/NailDeck#testing-features)
- [Deployment](https://github.com/katerinaelsasser/NailDeck#deployment)
  - [Running Locally](https://github.com/katerinaelsasser/NailDeck#running-locally)
  - [Deploying To Heroku]()
- [Credits]()

# UX

## Aim

The aim of this is create a website that the business can sell their nail products through. This must be easy to use and easy to navigate through on both the vistor and the business side. The visitor must be able to purchase products easily and the business must be able to upload new products on to the website.

### Target Audience

The target audience for the brand Nail Deck are:

- Anyone who love nail polishes.
- Anyone who love pirates.
- Anyone who love hand made products.

### Visitor Goals

- Browse through a list of nail products.
- Find a nail polish they would like to purchase.
- Able to navigate through the website easily.
- Able to add a review about the company.
- Can contact the company.
- Learn about the company.

### Online Shop Goals

- A clear and easy to use website that anyone can use it.
- Linking elements should link to the correct locations.
- The website should work on all size devices (sm, md, lg). This includes the navigation and the features,
- There must be a clear navigation linking all pages together.
- Admin must be able to access both the main website.

## Strategy

The main request from the company is that they want customers to purchase products from the website as well as this, the site owner wants the customer to have an account to purchase the items. Taking this into account, I have done the following:

- I want to display their products all over the website to advertise them to get them to pruchase the products. For example: images from social media of customers using the products.
- To get the customer to create an account, I have linked the product pages and the shopping cart page to a log in page, meaning the customer will have to login to access the page.

## Structure

The layout of the website has to advertise the products to customers so they would pruchase the products. Products must be presentable and easy to purchase, there must be a clear and easy to use checkout where customers can make purchases. The website is advertise for a wide range of audience who would use all devices to make purchases, which means all device displays must be readable.

## Skeleton

The main things about the website that will form the backbone are the navigation which will be featured on the header on each html page. By doing this, it will make the whole webpage look uniform. The only thing that will differ each page will be the section.

## Scope

Research was the biggest thing for this website as this is going to be in competition with other shops. I looked at what other competition had and what they haven't got. The research I do on this, will effect what I feature on the website pages.

### Research

I put together pros and cons to a select group of companies that sell the same products. These companies are Barry M, Boots, ASOS and Etsy.

#### [Barry M](https://barrym.com/)

- **Pros**

  - A lot of details of the products on display
  - Add to cart button on the product image
  - Responsive website
  - The home page sums up all of the pages.
  - Works well in different views (desktop, mobile, medium, etc.).

- **Cons**
  - A lot of features, possibly too many.
  - Navigration bar dropdown is messy.
  - Blank space on the dropdown.

#### [Boots](https://www.boots.com/)

- **Pros**
  - Elements that to connect to different pages on homepage.
  - Easy to find products.
  - Shopping cart is clear to understand.
- **Cons**
  - Too many features.
  - Elements on slideshow not responsive.
  - Too many categories.

#### [ASOS](https://www.asos.com/women/)

- **Pros**
  - Dropdown is clear to understand.
  - Pages are responsive to the different devices.
  - Products presented clearly.
- **Cons**
  - Nav Links don't take to pages when clicked on, only show the dropdown.
  - Can't buy products without having to go on to the individual display.
  - Can't select a quanity of products.

#### [Etsy](https://www.etsy.com/uk/)

- **Pros**
  - Homepage is clear for navigating as well as advertising products.
  - Easy to navigate through the website.
  - Lots of detail on individual product display.
- **Cons**
  - When clicking on a product, it opens another tab to that link.
  - Have to go on to individual product display to purchase.
  - Difficult to find a contact page.

## User stories

### Site user

As a visitor on the Nail Deck website, I want/expect:

- To view all products that is available to purchase.
- To be able to put products I want to buy in a cart.
- To be able to purchase the products I want to buy.
- To be able put in address/payment details with ease.
- To create a login easily.
- To be able to log in successfuly.
- To have a profile for my account.
- Able to see what I have bought in the past.
- The website must be clear to use.
- The infomation of the company on the website that I can view.
- To be able to contact the company if needed to.
- Able to leave a review.

### Site Owner

As the owner of the website, I want/expect:

- To sell products to customers on the website.
- Information of the business displayed so vistors can view it.
- Advertise to the customer to purchase the items.
- Products displayed clearly.
- Customers can purchase products with ease.
- To be able to have customers leave a contact.
- To be able to have customers leave a review.
- To be able to log in successfuly.
- The checkout to collect customer delivery details for sending the order and payment details.

## Surface

The surface of the website has to be fit in with the theme and with what would appeal to the target audience. I started to think about the layout, the colours, the typology and the imagery used throughout (see the [Design Choices](https://github.com/katerinaelsasser/NailDeck#design-choices) for full details of what things I decided to present for the surface). Mockups and a flowchart was created to help create all the pages, in all the mockups I noticed that the layouts were simple so customers can understand and have ease to find pages. The images that are used are images of the products the company sells and the products in use as this is advertising for the company and the customers can see what the products look like.

## Design Choices

### Overall

The overall design layout of the website has to have a simple layout with elements of pirates to show that these products have been inspired by them and have a stylish presentation for the beauty cosemetic presentation. With a lot of websites looking modern, I will need to feature things that have elements of the pirates style with modern features to them.

### Fonts

The font I have decided to use two font styles. These fonts are for the headers, with these they would bring the element of the pirate theme to the text as they are handwriting and it would give the effect of a treasure map.

- Font 1 (Meddon) - This font is chose for h1 tags for brand of the company.
- Font 2 (Tangerine) - This font is use for titles that are h2 and any sub titles.

### Icons

I wanted to style the website with icons. The icons I wanted to feature must include some pirate themed icons, such as skull and cross bones.

- The for the log in icon on the navbar has two icons. One for then the user is not logged in (the icon is `user`) and when the user is logged in (the icon is a skull and cross bone called `skull-crossbones`).

### Colours

- White - #FFFFFF
- Red - #D9230F
- Dark Grey - #212529

![ColourPallet](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/colourpallet.png)

### Images

The images that have been displayed on the website are from [Unsplash](https://unsplash.com/) & [Pixabay](https://pixabay.com/). These are royalty free image website. The images that I have used are images of hands with nail varnish on the nails or products of nail care. I have tried to find images of people who are located at beaches or somewhere tropical in the image. These images would be help create the visual of the pirate theme while advertising the products.

## Wireframes/Flowchart

### FlowChart

View the flowchart for this website [here](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/flowchart2020.jpg).

### Product Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/products-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/products-laptop.jpg)

### Cart Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/cart-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/cart-laptop.jpg)

### Checkout Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/checkout-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/checkout-laptop.jpg)

### Login Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/login-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/login-laptop.jpg)

### Register Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/register-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/register-laptop.jpg)

### User Profile Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/user-profile-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/user-profile-laptop.jpg)

### Admin Profile Layout

- [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/admin-profile-mobile.jpg)
- [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/admin-profile-laptop.jpg)

## Features

Throughout the page, there is a navigation bar on the header and the footer that takes you to the designated area. Throughout the wesbite there are responsive images as well as buttons to take the customer to the product pages.

### Existing Features

- Customers can create a account, use the login, adjust account details on profile dashboard.
- There is a contact form for users to contact the company.
- Customers can leave a review of what they thought of the company. Reviews will be displayed when they are submitted.
- List of products, including product categories display select products related to that list.
- Products can be added, adjusted and removed from the shopping basket.
- Customers can purchase products in their shopping basket. The checkout uses a Stripe API, this is where payment details will be process and a order will be placed.

### Future Features

- Product listings will have filters for specific products, including filtering by colour.
- Order confirmation will also send an email to the customer confirming the purchase.
- More categories will be created for more products.

## Information Architecture

### Database Choice

For this project, the database used is SQL. For my local machine, sqlite3 datbase was installed with Django. When deployed, Heroku provided the SQL database which is a PostgreSQL database.

### Data Models

#### Product Model

| Name        |  Key in DB  |                                         Validation |   Field Type |
| ----------- | :---------: | -------------------------------------------------: | -----------: |
| Name        |    name     |                     max_length=254, default='Name' |    CharField |
| Description | description |                            max_length=254          |    TextField |
| Price       |    price    |max_digits=6, decimal_places=2, default=Decimal(0.00) | DecimalField |
| Image       |    image    |                                 upload_to='images' |   ImageField |
| Category    |  category   | max_length=20, choices=CHOICES, default=POLISHES, |    CharField |

#### Checkout Model

| Name           |   Key in DB    |                  Validation | Field Type |
| -------------- | :------------: | --------------------------: | ---------: |
| User           |      user      | User, null=True, blank=True | ForeignKey |
| Full Name      |   full_name    |  max_length=50, blank=False |  CharField |
| Phone Number   |  phone_number  |  max_length=20, blank=False |  CharField |
| Country        |    country     |  max_length=40, blank=False |  CharField |
| Postcode       |    postcode    |   max_length=20, blank=True |  CharField |
| Town/City      |  town_or_city  |  max_length=40, blank=False |  CharField |
| Street Address | street_address |  max_length=40, blank=False |  CharField |
| Country        |     county     |  max_length=40, blank=False |  CharField |
| Date           |      date      |                             |  DateField |

#### Order Model

| Name     | Key in DB |          Validation |   Field Type |
| -------- | :-------: | ------------------: | -----------: |
| Order    |   order   |   Order, null=False |   ForeignKey |
| Product  |  product  | Product, null=False |   ForeignKey |
| Quantity | quantity  |         blank=False | IntegerField |

#### Contact Model

| Name    | Key in DB |                             Validation | Field Type |
| ------- | :-------: | -------------------------------------: | ---------: |
| Name    |   name    |  max_length=50, default='', blank=False |  CharField |
| Email   |   email   | max_length=200, default='', blank=False | EmailField |
| Message |  message  |             max_length=1024, default='' |  TextField |

#### Review Modal

| Name    | Key in DB |                                       Validation | Field Type |
| ------- | :-------: | -----------------------------------------------: | ---------: |
| Star    |   order   | max_length=11, choices=STAR_CHOICES, default='5' |  CharField |
| Message |  product  |                                  max_length=1024 |  CharField |

#### User Models

The user model is the standard one supplied by

```
django.contrib.auth.models
```

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Databases

- PostgreSQL
- SQlite3

### Libaries/Tools

- jQuery
- Git
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [Bootswatch](https://bootswatch.com/simplex/)
- Font-Awesome
- Stripe
- Django
- [AWS S3 Bucket](https://aws.amazon.com/)
- [Travis](https://travis-ci.org/katerinaelsasser/NailDeck.svg?branch=master)](https://travis-ci.org/katerinaelsasser/NailDeck)

## Testing

### Planning:

When it came to planning this website, it was very important to plan every detail which includes the APIs, technology, frameworks and other tools. The wireframes that I created were the base for the webiste, as well as this I have tried to utilise component files and I tried to reuse these across the website on multiple pages which was linked by the languages, Django.

### Testing Features

#### Contact Form Page

- **Planning:** When planning how I wanted to make the contact form, I thought about how the admin of the website would get in contact with the customer. I wanted to store the contact in the admin panel.
- **Implementation:** The dashboard was going to be where the contact form would be submitted to. This allows the admin to see what is submitted clearly and can reply when they can. I added code to the ` view.py ` file which said to save the form if the form was valid and submitted by the user. 
- **Test:** When testing, I filled in the form that was created as if I was the customer.
- **Results:** When I pressed submit, the page refreshed and the input was all gone. I checked the Admin panel to see if the data had been saved and everything that I put in the form was collected and stored.
- **Verdict:** This form has met the criteria.

#### Product List Pages (All Products/ Nail Varnishes / Nail Care)

- **Planning:** A ecommerce website needs a list of products on a page. When a user is viewing this page, they should be able to add a product to the shopping cart. As well as this, the products should be displayed professionally. As there were going to be different types of products on the listing, I have decided to also plan for categories that would hold particular products. For example: products that are nail care, will be in a category dedicated to that type.
- **Implementation:** To display the products, I had to use a model that would hold the data of the products and link to the database that connects to the correct product to the correct page.
- **Test:** When clicking on the link to the page, the products would display automatically without there being a timer. If the products were displaying, it meant that there was an error with the django code that was used. It is very important when linking products that there are no typos in the code as this became an issue for displaying them.
- **Results:** When the going on to the pages, the products displayed in a neat display all the way down the page and also products displayed in the correct categories.
- **Verdict:** This form has met the criteria. 

#### Shopping Cart

- **Planning:** A huge part of this website is so that a customer can purchase products from the company. With the admin of this website wanted customers to log into the site to use it, I wanted it so customers had to be logged in to add products to the cart. When users are thinking about purchasing their items, they must be able to edit and delete products in their cart.
- **Implementation:** I created a file called ` context.py ` which is in the cart app. This was included in the context processors section inside the template in the file, ` settings.py `. By haing this, it will tell the app how the cart should be presented in default as well as what information should be available to it. This is a requirement as the cart is not stored in the database, instead in the session. When this was added, I wrote the view function for adding products to the cart, editing the quantity of products and how the content was displayed.
- **Test:** When testing, I went over to the product pages and adding random products to the cart. Once I was happy with what I had added and made a note of what products and the quantity, I headed to the cart page and checked what was in the cart with what I had noted down.
- **Results:** All the products that I had added were in the cart displayed correctly, I tested the edit quantity/removal of the products from the cart and everything worked correctly.
- **Verdict:** This form has met the criteria.

#### Checkout

- **Planning:** When customers are putting products they want, they will need to purchase these products. As this would require the customer to fill in personal information such as card details and delivery information. This meant that the form had to be clear and easy to use when fill it out.
- **Implementation:** The checkout needed to link with a API called Stripe. Stripe is used to hold the personal infomation that would be put into the form. Connecting this to the form would be import to make sure the data would be safe.
- **Test:** When filling in the form, I used a testing cart `4242 4242 4242 4242`. There was an error with the card details, see [Bugs](https://github.com/katerinaelsasser/NailDeck#bugs) for more detail on this issue. When this was fixed, the card and delivery details went through and were submitted.
- **Results:** The details that the customer put in the form is processed and the order is taken.
- **Verdict:** This form has met the criteria.

#### Profile Dashboard

- **Planning:** When a user is logged into the website, I wanted the user to able able to access and change their details. As well as this, I wanted them to be able to see their purchase history.
- **Implementation:** To do this I will be linking to the `OrderLineItem` model in the checkout app and I will be linking to the to the login/register form. The `OrderLineItem` would collect the data for the orders and the login would help create the update form for the details. As this would be for a specific account, I would need to match the user with both the order and the details instead of collecting every single data in the database.
- **Test:** As I had tested out the checkout already, all I had to do was make sure the details matched what I had asked to be collected from it. When checking the details update, I added `test` to the empty input and pressed save, I then went into the Admin panel and looked at the specific account and looked for the `test`.
- **Results:** Both the order history and the update details displayed connected to the database and collected the right data required. I added more orders to the account and checked the page to see the order was added to the list. With the details form, I tested multiple times, checking each tine that every little detail I changed was updated on the database. 
- **Verdict:** These forms has met the criteria.

#### User Authentication (Register/ Login / Logout)

- **Planning:** As owner of the site would like users to have logins, it makes it very important that the user can create, login and logout of their accounts. This would require using django.auth setting as a feature which would be featured. The user was going to be able to access more of the website such as product pages.
- **Implementation:** The table for the user is in django. Taking this into account, all I had to do was create a form as well as the view file. I would have to create code that would create a account, a login and logout code for that account.
- **Test:** WI started by creating a account called `Admin`, once I had filled in the form and submitted it, I checked that the database had the account. When I saw the data was there, I headed over to the login page and entered the username and password into the form which would log the account in. When I was logged in, I then logged the account out.
- **Results:** When logged into the account, the detail and links on the page would adjust to the user view only. The alerts for when the account was logged in and logged out appeared with the correct text.
- **Verdict:** This form has met the criteria.

#### Review Page

- **Planning:** When a user would like to review a page, there must be a clear form that they can fill in and submit for other users of the site to see. When the review is submitted, the review must be displayed on the page for other customers to see it.
- **Implementation:** The dashboard was going to be where the review form would be submitted to. This allows the admin to see what is submitted clearly and can reply when they can. I added code to the ` view.py ` file which said to save the form if the form was valid and submitted by the user.
- **Test:** When testing, I filled in the form to create a dummy review.
- **Results:** When I pressed submit, the page refreshed and the input was all gone. AS well as this, the review that I created was displaying on the page  I checked the Admin panel to see if the data had been saved and everything that I put in the form was collected and stored.
- **Verdict:** This form has met the criteria.

### Bugs

The bug that happened during this project were with Stripe.

- **Bug/Issue:** When I was putting through a test order, an error came up with the order not going through. A message at the top of the page appeared saying that the card was incorrect.
- **Solution:** When looking at where the error was coming from, I looked at the Stripe Javascipt file. When looking at this file, I noticed a very simple mistake. This was that the card id on the HTML page was not matching the Javascript file.
- **Verdict:** When this was changed to match, the issue was fixed.

### Vailidation Services

Vailidation services were used to check HTML, CSS and Javascipt that was used throughout the website.
The following code:

- HTML - [W3C Markup Validation](https://validator.w3.org/)
- CSS - [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- JavaScript - [JSHint](https://jshint.com/)

## Deployment

### Running Locally

To run the website locally, I used the following steps.

#### Before:

Before starting, the following must be check:

- That GitPod has the following installed on the machine:
  - PIP
  - Python3
  - Git
- An account has been created for the following services:
  - Stripe

#### Instructions:

1. Clone the repository by typing in the command below into your terminal or downloading from here.

```bash
 git clone https://github.com/geomint/thecoffeeshop
```

2. Navigate to the correct location in your terminal.
3. Enter the command below into your terminal.

```bash
 python3 -m .venv venv
```

4. Use the commoand below to initialize the environment.

```bash
 .venv\bin\activate
```

- (Optional) Depending on the operating system, Upgrade pip locally with

```bash
 pip install --upgrade pip
```

5. Install the requirmenets using the below

```bash
 pip3 -r requirements.txt
```

6. In the IDE, create a file where you can store your secret information for the app. I placed these in the a file called `env.py` file.

```bash
os.environ.setdefault("STRIPE_PUBLISHABLE", "")
os.environ.setdefault("STRIPE_SECRET", "")
os.environ.setdefault("DATABASE_URL", "")
os.environ.setdefault("SECRET_KEY", "")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
```

7. Put the following command into the terminal to migrate models into database.

```bash
 python3 manage.py migrate
```

8. Add the following command to the terminal to create a 'superuser' for the project.

```bash
 python3 manage.py createsuperuser
```

9. Use the command below to run the project locally.

```bash
 python3 manage.py runserver
```

### Deploying To Heroku

The website was deployed and hosted through Heroku. I have connected this through my terminal. I have used code that has been supplied by heroku on their 'Deploy' tab.

These were the steps that I took:

1.  A `requirement.txt` file was created using the command on my terminal

```bash
pip freeze > requirement.txt
```

2. I then created a `Procfile` which as was also created on my terminal using

```bash
echo web: python app.py > Procfile
```

3. Putting `git add` followed by `git commit` and then `git push` to put my new files on GitHub

- On my Heroku account, press the **New** located on the dashboard. Give it a name and select the region to be **Europe**
- When this is created, go to the **Deploy** tab. Under the section **Deployment method**, select out of the three options **GitHub**.
- Choose the link to your GitHub repository. In this case, it would be this [link](https://github.com/katerinaelsasser/film_review_database).
- After this is connected, head over to the **Settings** tab.
- Go to the section called **Reveal Config Vars**.
- Fill in the following into the correct fields.

| Key                     |               Value               |
| ----------------------- | :-------------------------------: |
| AWS_ACCESS_KEY_ID       |     #`INSERT ACCESS KEY ID`#      |
| AWS_SECRET_ACCESS_KEY   |     #`INSERT AWS ACCESS KEY`#     |
| AWS_STORAGE_BUCKET_NAME |    #`INSERT AWS BUCKET NAME`#     |
| DATABASE_URL            |      #`INSERT DATABASE URL`#      |
| SECRET_KEY              |       #`INSERT SECRET KEY`#       |
| STRIPE_PUBLISHABLE      | #`INSERT STRIPE PUBLISHMENT KEY`# |
| STRIPE_SECRET           |   #`INSERT STRIPE SECRET KEY`#    |

- In the heroku dashboard, click **Deploy**. Under the **Manual Deployment** section, select the branch that you want to connect to.
- Once selected click on the button **Deploy Branch**

When these steps have been followed, the website will be successfully deployed.

## Credits

### Content
All content that is on this website has been written by myself. 

### Media
All images were taken from [Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/).

### Acknowledgements
Inspiration by a film called Pirates of the Carribean. I got inspired by the names as well as the storyline to create beauty products inspired by it.My mentor, Simen Daehlin, inspired my header layout as well as the social content.


## Disclaimer

The contents of this website are for educational purposes only.
