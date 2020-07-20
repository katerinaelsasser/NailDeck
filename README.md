# Nail Deck [![Build Status](https://travis-ci.org/katerinaelsasser/NailDeck.svg?branch=master)](https://travis-ci.org/katerinaelsasser/NailDeck)

Nail Deck is an online website for selling hand made nail polishes to customers. Their polishes are inspired by pirates which includes the names of the products.

Content
* [UX](https://github.com/katerinaelsasser/NailDeck#ux)
    * [Aim](https://github.com/katerinaelsasser/NailDeck#aim)
        * [Target Audience](https://github.com/katerinaelsasser/NailDeck#target-audience)
        * [Visitor Goals](https://github.com/katerinaelsasser/NailDeck#visitor-goals)
        * [Online Shop Goals](https://github.com/katerinaelsasser/NailDeck#online-shop-goals)
    * [Strategy]()
    * [Structure]()
    * [Skeleton]()
    * [Scope](https://github.com/katerinaelsasser/NailDeck#scope)
    * [Research](https://github.com/katerinaelsasser/NailDeck#research)
    * [User Stories](https://github.com/katerinaelsasser/NailDeck#user-stories)
        * [Site User](https://github.com/katerinaelsasser/NailDeck#site-user)
        * [Site Owner](https://github.com/katerinaelsasser/NailDeck#site-owner)
    * [Surface](https://github.com/katerinaelsasser/NailDeck#surface)
    * [Design Choices](https://github.com/katerinaelsasser/NailDeck#design-choices)
        * [Overall](https://github.com/katerinaelsasser/NailDeck#overall)
        * [Fonts](https://github.com/katerinaelsasser/NailDeck#fonts)
        * [Icons](https://github.com/katerinaelsasser/NailDeck#icons)
        * [Colours](https://github.com/katerinaelsasser/NailDeck#colours)
        * [Images](https://github.com/katerinaelsasser/NailDeck#images)
    * [Wireframes/Flowchart](https://github.com/katerinaelsasser/NailDeck#wireframesflowchart)
* [Features](https://github.com/katerinaelsasser/NailDeck#features)
    * [Existing Features](https://github.com/katerinaelsasser/NailDeck#existing-features)
    * [Future Features](https://github.com/katerinaelsasser/NailDeck#future-features)
* [Information Architecture]()
    * [Database choice]()
    * [Data Models]()
* [Technologies Used](https://github.com/katerinaelsasser/NailDeck#technologies-used)
    * [Languages](https://github.com/katerinaelsasser/NailDeck#languages)
    * [Databases](https://github.com/katerinaelsasser/NailDeck#databases)
    * [Liabries](https://github.com/katerinaelsasser/NailDeck#libaries)
* [Testing]()
* [Deployment]()
    * [Running Locally]()
    * [Deploying To Heroku]()
* [Credits]()


# UX
## Aim
The aim of this is create a website that the business can sell their nail products through. This must be easy to use and easy to navigate through on both the vistor and the business side. The visitor must be able to purchase products easily and the business must be able to upload new products on to the website.
### Target Audience
The target audience for the brand Nail Deck are:
* Anyone who love nail polishes.
* Anyone who love pirates.
* Anyone who love hand made products.

### Visitor Goals
* Browse through a list of nail products.
* Find a nail polish they would like to purchase.
* Able to navigate through the website easily.

### Online Shop Goals
* A clear and easy to use website that anyone can use it.
* Linking elements should link to the correct locations.
* The website should work on all size devices (sm, md, lg). This includes the navigation and the features,
* There must be a clear navigation linking all pages together.
* Admin must be able to access both the main website and the admin page.

## Strategy
The main request from the company is that they want customers to purchase products from the website as well as this, the site owner wants the customer to have an account to purchase the items. Taking this into account, I have done the following:
* I want to display their products all over the website to advertise them to get them to pruchase the products. For example: images from social media of customers using the products.
* To get the customer to create an account, I have linked the product pages and the shopping cart page to a log in page, meaning the customer will have to login to access the page.

## Structure
The layout of the website has to advertise the products to customers so they would pruchase the products. Products must be presentable and easy to purchase, there must be a clear and easy to use checkout where customers can make purchases. The website is advertise for a wide range of audience who would use all devices to make purchases, which means all device displays must be readable.

## Skeleton
The main things about the website that will form the backbone are the navigation which will be featured on the header on each html page. By doing this, it will make the whole webpage look uniform. The only thing that will differ each page will be the section.

## Scope
Research was the biggest thing for this website as this is going to be in competition with other shops. I looked at what other competition had and what they haven't got. The research I do on this, will effect what I feature on the website pages.

### Research
I put together pros and cons to a select group of companies that sell the same products. These companies are Barry M, Boots, ASOS and Etsy.

#### [Barry M](https://barrym.com/)
* Pros 
    * A lot of details of the products on display
    * Add to cart button on the product image
    * Responsive website
    * The home page sums up all of the pages.
    * Works well in different views (desktop, mobile, medium, etc.).

* Cons 
    * A lot of features, possibly too many.
    * Navigration bar dropdown is messy.
    * Blank space on the dropdown.
    
#### [Boots](https://www.boots.com/)
* Pros
    * Elements that to connect to different pages on homepage.
    * Easy to find products.
    * Shopping cart is clear to understand.
* Cons
    * Too many features.
    * Elements on slideshow not responsive.
    * Too many categories.

#### [ASOS](https://www.asos.com/women/)
* Pros 
    * Dropdown is clear to understand.
    * Pages are responsive to the different devices.
    * Products presented clearly.
* Cons
    * Nav Links don't take to pages when clicked on, only show the dropdown.
    * Can't buy products without having to go on to the individual display.
    * Can't select a quanity of products.

#### [Etsy](https://www.etsy.com/uk/)
* Pros
    * Homepage is clear for navigating as well as advertising products.
    * Easy to navigate through the website.
    * Lots of detail on individual product display.
* Cons
    * When clicking on a product, it opens another tab to that link.
    * Have to go on to individual product display to purchase.
    * Difficult to find a contact page.

## User stories 
### Site user
As a visitor on the Nail Deck website, I want/expect:
* To view all products that is available to purchase.
* To be able to put products I want to buy in a cart.
* To be able to check out producst I want to buy.
* To be able put in address/payment details with ease.
* To create a login easily.
* To be able to log in successfuly. 
* To reset password if I forget it.
* To have a profile for my account.
* The website must be clear to use.
* The infomation of the company on the website that I can view.
* To find infomation of how to contact the business if needed.

### Site Owner 
As the owner of the website, I want/expect:
* To sell products to customers on the website.
* To be able to put new products on with ease.
* Information of the business displayed so vistors can view it.
* Contact details must be displayed so the vistors can find it if needed.

## Surface
The surface of the website has to be fit in with the theme and with what would appeal to the target audience. I started to think about the layout, the colours, the typology and the imagery used throughout (see the [Design Choices](https://github.com/katerinaelsasser/NailDeck#design-choices) for full details of what things I decided to present for the surface). Mockups and a flowchart was created to help create all the pages, in all the mockups I noticed that the layouts were simple so customers can understand and have ease to find pages. The images that are used are images of the products the company sells and the products in use as this is advertising for the company and the customers can see what the products look like.

## Design Choices 
### Overall
The overall design layout of the website has to have a simple layout with elements of pirates to show that these products have been inspired by them and have a stylish presentation for the beauty cosemetic presentation. With a lot of websites looking modern, I will need to feature things that have elements of the pirates style with modern features to them.

### Fonts
The font I have decided to use two font styles. These fonts are for the headers, with these they would bring the element of the pirate theme to the text as they are handwriting and it would give the effect of a treasure map. 
* Font 1 (Meddon) - This font is chose for h1 tags for the title of the website and also the titles of the products. 
* Font 2 (Tangerine) - This font is use for titles that are h2 and any sub titles.
### Icons
I wanted to style the website with icons. The icons I wanted to feature must include some pirate themed icons, such as skull and cross bones.
* The for the log in icon on the navbar has two icons. One for then the user is not logged in (which is the skull) and the other for when they are logged in (which is the skull and cross bones).
### Colours

* White - #FFFFFF
* Orange - #FF7D45
* Red - #C63232
* Purple - #772953
* Black - #000000

### Images
The images that have been displayed on the website are from [Unsplash](https://unsplash.com/) & [Pixabay](https://pixabay.com/). These are royalty free image website. The images that I have used are images of hands with nail varnish on the nails. I have tried to find images of people who are located at beaches or somewhere tropical in the image. These images would be help create the visual of the pirate theme while advertising the products.

## Wireframes/Flowchart

### FlowChart 

### Product Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/products-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/products-laptop.jpg)

### Cart Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/cart-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/cart-laptop.jpg)

### Checkout Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/checkout-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/checkout-laptop.jpg)

### Login Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/login-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/login-laptop.jpg)

### Register Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/register-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/register-laptop.jpg)

### User Profile Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/user-profile-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/user-profile-laptop.jpg)

### Admin Profile Layout
* [Mobile Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/admin-profile-mobile.jpg)
* [Laptop Version](https://github.com/katerinaelsasser/NailDeck/blob/master/wireframes/admin-profile-laptop.jpg)

## Features
Throughout the page, there is a navigation bar on the header and the footer that takes you to the designated area. Throughout the wesbite there are responsive images as well as buttons to take the customer to the product pages.
### Existing Features
* Customers can create a account, use the login, adjust account details on profile dashboard.
* If users forget thier password, they can reset the password.
* There is a contact form for users to contact the company.
* List of products, including product categories display select products related to that list.
* Products can be added, adjusted and removed from the shopping basket.
* Customers can purchase products in their shopping basket. The checkout uses a Stripe API, this is where payment details will be process and a order will be placed.
### Future Features
* Product listings will have filters for specific products, including filtering by colour.
* Order confirmation will also send an email to the customer confirming the purchase.
* More categories will be created for more products.

## Information Architecture
### Database Choice
For this project, the database used is SQL. For my local machine, sqlite3 datbase was installed with Django. When deployed, Heroku provided the SQL database which is a PostgreSQL database.

### Data Modals
#### Product Modal
The products have the following model:

| Name          | Key in DB     | Validation  | Field Type |
| ------------- |:-------------:| -----:      | -----:     |
| Name      | name | max_length=254, default='' |CharField |
| Description     | description |  | TextField|
| Price     | price  | max_digits=6, decimal_places=2 | DecimalField|
| Image     | image | upload_to='images' | ImageField|
| Category     | category | max_length=11, choices=CHOICES, default='polishes' |CharField |

#### Checkout Modal
| Name        | Key in DB           | Validation  | Field Type |
| ------------- |:-------------:| -----:| -----:|
| User      | user | User, on_delete=models.PROTECT, default=None | ForeignKey|
| Full Name     | full_name | max_length=50, blank=False | CharField|
| Phone Number     | phone_number | max_length=20, blank=False |CharField |
| Country     | country | max_length=40, blank=False |CharField |
| Postcode     | postcode | max_length=20, blank=True |CharField |
| Town/City     | town_or_city | max_length=40, blank=False | CharField|
| Street Address     | street_address | max_length=40, blank=False | CharField|
| Country     | county | max_length=40, blank=False | CharField|
| Date     | date |  |DateField |

#### Order Modal
| Name        | Key in DB           | Validation  | Field Type |
| ------------- |:-------------:| -----:| -----:|
| Order      | order | Order, null=False |ForeignKey |
| Product     | product | Product, null=False | ForeignKey|
| Quantity     | quantity | blank=False |IntegerField |

#### User Modals
The user model is the standard one supplied by `django.contrib.auth.models`.
## Technologies Used
### Languages
* HTML
* CSS
* JavaScript
* Python
### Databases
* PostgreSQL
* SQlite3
### Libaries
* jQuery
* Git
* Bootstrap
* Font-Awesome
* Sweetalert2
* Stripe
* Django
## Testing]()
## Deployment]()
### Running Locally]()
To run the website locally, I used the following steps.

#### Before:
Before starting, the following must be check:
* That GitPod has the following installed on the machine:
    * PIP
    * Python3
    * Git
* An account has been created for the following services:
    * Sendgrid
    * Stripe

#### Instructions:
1. Clone the repository by typing in the command below into your terminal or downloading from here.
` git clone https://github.com/geomint/thecoffeeshop `
2. Navigate to the correct location in your terminal.
3. Enter the command below into your terminal.
` python3 -m .venv venv `
4. Use the commoand below to initialize the environment.
` .venv\bin\activate `
* (Optional) Depending on the operating system, Upgrade pip locally with
` pip install --upgrade pip `
5. Install the requirmenets using the below
` pip3 -r requirements.txt `
6. In the IDE, create a file where you can store your secret information for the app. I placed these in the a file called `env.py` file.
` os.environ.setdefault("STRIPE_PUBLISHABLE", "") `
` os.environ.setdefault("STRIPE_SECRET", "") `
` os.environ.setdefault("DATABASE_URL", "") `
` os.environ.setdefault("SECRET_KEY", "") `
` os.environ.setdefault("AWS_ACCESS_KEY_ID", "") `
` os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "") `
7. Put the following command into the terminal to migrate models into database.
` python3 manage.py migrate `
8. Add the following command to the terminal to create a 'superuser' for the project. 
` python3 manage.py createsuperuser `
9. Use the command below to run the project locally.
` python3 manage.py runserver `

### Deploying To Heroku]()
## Credits
