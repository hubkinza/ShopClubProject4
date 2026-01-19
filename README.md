
# ShopClub - E-Commerce Django Application

<img width="2940" height="1588" alt="image" src="https://github.com/user-attachments/assets/41047133-5fe0-4a53-ba40-2a3c64c79538" />




## Project Overview

**ShopClub** is a full-stack e-commerce web application built with Django 4.2, featuring a complete shopping experience with product browsing, cart management, secure Stripe payment integration, and user authentication. The application demonstrates modern web development practices, clean code principles, and comprehensive CRUD functionality.

**Live Site:** `http://13.60.188.35/`  
**Admin Panel:** `http://13.60.188.35//admin`

---

## Purpose & Value

ShopClub provides users with:
- 🛍️ **Easy Shopping Experience**: Browse products by category, search, and filter by price
- 💳 **Secure Payments**: Industry-standard Stripe integration for safe transactions
- 👤 **User Accounts**: Save shipping addresses and track order history
- 📦 **Order Management**: Real-time order status and payment tracking
- 🔒 **Data Security**: Protected user information and secure authentication

**Why Users Need Accounts:**
- Save shipping addresses for faster checkout
- Track order history and payment status
- Access order details and receipts
- Manage personal profile information
- Admin users can create, edit, and delete products

---

## Features

### User Features
- ✅ User registration with shipping address collection
- ✅ Login/logout functionality with styled pages
- ✅ Product browsing with category filters
- ✅ Shopping cart with quantity management
- ✅ Secure Stripe checkout integration
- ✅ Order history and tracking
- ✅ User profile management
- ✅ Payment success/failure feedback

### Admin Features
- ✅ Product CRUD (Create, Read, Update, Delete) via web interface
- ✅ Django admin panel for advanced management
- ✅ Order management and payment status tracking
- ✅ Category management

### Security Features
- ✅ Authentication required for cart/checkout
- ✅ Staff-only access to product management
- ✅ Environment variables for sensitive data
- ✅ DEBUG mode disabled in production
- ✅ CSRF protection on all forms
- ✅ Password validation and hashing

---

## Technology Stack

### Backend
- **Python 3.11.14**
- **Django 4.2.11** - Full-stack MVC framework
- **PostgreSQL** - Relational database (AlwaysData hosting)
- **Gunicorn 21.2.0** - WSGI HTTP server
- **Stripe 7.0.0** - Payment processing
- **Cloudinary** - Storage

### Frontend
- **Bootstrap 5.3.2** - Responsive UI framework
- **Bootstrap Icons 1.11.1** - Icon library
- **HTML5 & CSS3** - Semantic markup and styling
- **JavaScript (Vanilla)** - Client-side interactivity

### Deployment & Infrastructure
- **AWS EC2** - Cloud hosting (Ubuntu 22.04)
- **Nginx** - Reverse proxy and static file serving
- **WhiteNoise 6.6.0** - Static file serving
- **Git & GitHub** - Version control

### Additional Packages
- **Django Allauth 0.61.1** - Authentication
- **Django Crispy Forms 2.1** - Form styling
- **Pillow 10.2.0** - Image processing
- **Python-decouple 3.8** - Environment variable management

---
## Screenshots

### Homepage
<img width="2940" height="1580" alt="image" src="https://github.com/user-attachments/assets/1554af41-cd9d-4fc8-b6ae-deb51cf37445" />


### Product Catalog
<img width="2934" height="1478" alt="image" src="https://github.com/user-attachments/assets/f40feb51-9b59-44fb-9de9-783220663998" />


### Shopping Cart
<img width="2940" height="1590" alt="image" src="https://github.com/user-attachments/assets/709c4a4c-d06d-4030-b005-a361d6c38bb1" />


### Checkout Process
<img width="2940" height="1588" alt="image" src="https://github.com/user-attachments/assets/fb4ef617-0a8d-4ccf-8380-17ef4cef2fd3" />


### Order Confirmation
<img width="2940" height="1750" alt="image" src="https://github.com/user-attachments/assets/f0ee7f4a-78ae-4ea7-be24-47e000045fbd" />


### Admin Product Management

<img width="2930" height="1548" alt="image" src="https://github.com/user-attachments/assets/bec4e07c-b4d3-42e8-a1cf-9a4bbff19a86" />

<img width="2940" height="1584" alt="image" src="https://github.com/user-attachments/assets/69d2c3ee-839d-4177-b99a-af99dae6521d" />


---
## Full Stack Web Application Design & Development

####  ✅ Django Framework with Multiple Apps
 
- **3 Django Apps**: `products`, `orders`, `accounts`
- Each app is a reusable component with specific responsibility
- MVC architecture properly implemented

**Code Location:**
```
shopclub/
├── products/     # Product catalog, cart, categories
├── orders/       # Order processing, checkout
└── accounts/     # User profiles, authentication
```

####  ✅ Front-End Design (UX/Accessibility)
 
- Responsive Bootstrap 5 design (mobile-first)
- Semantic HTML5 markup
- ARIA labels for accessibility
- Consistent color scheme with high contrast
- Intuitive navigation and user flows
- Form validation with clear error messages
- Loading states and user feedback

**Code Location:** `templates/` directory with base template and app-specific templates

#### ✅ Full Stack Implementation
 
- PostgreSQL relational database (AlwaysData)
- Interactive frontend with dynamic content
- 3 distinct Django apps with specific purposes
- Complete user flow from browsing to checkout

**Models:** 10 custom models across 3 apps  
**Views:** 20+ view functions  
**Templates:** 12 HTML templates with Bootstrap 5

#### ✅ Forms with Validation
 
- **ProductForm**: Create/edit products with validation (slug uniqueness, price format)
- **CheckoutForm**: Shipping information with email/phone validation
- **CustomSignupForm**: User registration with password matching and address validation

**Code Location:**
- `products/forms.py` - Product management form
- `orders/forms.py` - Checkout form with Stripe integration
- `accounts/forms.py` - Custom signup form

#### ✅ Django File Structure
 
```
shopclub/
├── config/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/            # Products app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
├── orders/              # Orders app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
├── accounts/            # Accounts app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/           # Templates
│   ├── base.html
│   ├── products/
│   ├── orders/
│   └── accounts/
├── static/              # Static files
├── media/               # User uploads
└── manage.py
```

####  ✅ Consistent URL Patterns
 
- RESTful URL naming conventions
- Namespaced URLs (`products:cart`, `orders:checkout`)
- Descriptive path names
- Consistent parameter patterns (slug for products, order_number for orders)

**Code Location:** All `urls.py` files use consistent patterns

####  ✅ Navigation & Structured Layout
 
- Global navigation bar in `base.html`
- Breadcrumb navigation on product pages
- Consistent header and footer across all pages
- Mobile-responsive navigation with hamburger menu
- Cart count badge in navbar

**Code Location:** `templates/base.html`


####  ✅ Testing Procedures
**Manual Testing Performed:**
- ✅ User registration and login
- ✅ Product browsing and filtering
- ✅ Add to cart functionality
- ✅ Checkout process with Stripe test cards
- ✅ Order creation and tracking
- ✅ Admin product CRUD operations
- ✅ Form validation (all forms tested with invalid data)
- ✅ Responsive design (tested on mobile, tablet, desktop)
- ✅ Browser compatibility (Chrome, Firefox, Safari)

**Test Card:** 4242 4242 4242 4242 (Stripe test mode)

---

###    2: Relational Data Model & Business Logic

#### 2.1 ✅ Relational Database Schema
 
**Database Diagram:**
```
User (Django Auth)
  ├── UserProfile (1:1)
  ├── Orders (1:Many)
  ├── Cart (1:Many)
  └── ShippingAddress (1:Many)

Category
  └── Products (1:Many)

Order
  └── OrderItems (1:Many) → Product

Product
  ├── Cart (1:Many)
  └── OrderItems (1:Many)
```

**Code Location:** All `models.py` files

####  ✅ Custom Django Models
  **10 custom models created**

1. **Product** (`products/models.py`) - Main product catalog
2. **Category** (`products/models.py`) - Product categorization
3. **Cart** (`products/models.py`) - Shopping cart items
4. **Order** (`orders/models.py`) - Customer orders
5. **OrderItem** (`orders/models.py`) - Items in orders
6. **ShippingAddress** (`orders/models.py`) - Saved addresses
7. **UserProfile** (`accounts/models.py`) - Extended user data

**All models include:**
- Custom fields
- Relationships (ForeignKey, OneToOne)
- Properties and methods
- Meta classes for ordering

#### ✅ Form with Validation for Record Creation
 

**CustomSignupForm** (`accounts/forms.py`):
- Creates User records in database
- Validates: username, email, password matching
- Creates UserProfile automatically
- Creates default ShippingAddress
- **Beyond authentication:** Collects shipping address during signup

**CheckoutForm** (`orders/forms.py`):
- Creates Order records
- Validates: email format, phone number, postal code
- Pre-fills from saved addresses

**ProductForm** (`products/forms.py`):
- Creates Product records
- Validates: price format, slug uniqueness, stock quantity

#### ✅ Full CRUD Implementation
 

| Model | Create | Read | Update | Delete |
|-------|--------|------|--------|--------|
| **Product** | ✅ Admin form | ✅ List/Detail views | ✅ Edit form | ✅ Delete confirmation |
| **Category** | ✅ Admin panel | ✅ Category pages | ✅ Admin panel | ✅ Admin panel |
| **Cart** | ✅ Add to cart | ✅ Cart view | ✅ Update quantity | ✅ Remove from cart |
| **Order** | ✅ Checkout | ✅ Order list/detail | ✅ Admin panel | ✅ Admin panel |
| **UserProfile** | ✅ Auto on signup | ✅ Profile page | ✅ Profile form | ✅ Admin panel |

**Code Evidence:**
- **Create**: `product_create()`, `add_to_cart()`, `checkout()`
- **Read**: `product_list()`, `product_detail()`, `order_list()`
- **Update**: `product_edit()`, `update_cart()`, `profile()`
- **Delete**: `product_delete()`, `remove_from_cart()`

---

### Authentication, Authorization & Permissions

####  ✅ Authentication Mechanism
 
- Django Allauth integration for registration/login
- Custom signup form with extended fields
- Password validation and hashing

**Why Users Need Accounts:**
- **Cart Functionality**: Only logged-in users can add items to cart
- **Checkout**: Authentication required to place orders
- **Order Tracking**: View order history and payment status
- **Address Management**: Save shipping addresses for future use
- **Profile Management**: Update personal information

**Code Location:**
- `config/settings.py` - Allauth configuration
- `accounts/forms.py` - Custom signup form
- `templates/account/` - Styled login/signup pages

####  ✅ Login/Registration Pages for Anonymous Users Only
 
- Login/Signup links hidden when user is logged in
- Redirect to home if authenticated user visits login page
- Navbar dynamically shows Login/Signup OR Profile/Logout
  

---

### E-Commerce Payment System

#### ✅ Stripe Integration
 
- Complete Stripe Checkout implementation
- Shopping cart checkout flow
- Payment Intent creation via API
- Secure card element integration
- Webhook handler for payment confirmation

**Features:**
- Test mode with Stripe test keys
- Client-side card validation
- Server-side payment processing
- Payment status tracking (Pending/Paid/Failed)

**Code Location:**
- `orders/views.py` - `checkout()`, `create_payment_intent()`
- `templates/orders/checkout.html` - Stripe.js integration
- `.env` - Stripe API keys (hidden from git)

#### ✅ Payment Feedback System
 

**Success Flow:**
1. Payment processes successfully
2. Order created with "Paid" status
3. Redirect to success page with order number
4. Cart cleared automatically
5. Success message displayed

**Failure Flow:**
1. Payment fails (invalid card, insufficient funds)
2. Error message displays below card field
3. User can retry immediately
4. Order not created
5. Cart remains intact

**Code Location:**
- `templates/orders/order_success.html` - Success page
- `templates/orders/checkout.html` - Error handling in JavaScript
- Toast messages for all actions (Django messages framework)

---

### Version Control & Deployment

#### ✅ Deployed & Tested
 
- Deployed on AWS EC2 (Ubuntu 22.04)
- Gunicorn + Nginx production setup
- AlwaysData PostgreSQL database
- Static files served via WhiteNoise
- Media files accessible
- All features tested on production

**Production URL:** `http://YOUR-EC2-IP`

**Testing Checklist:**
- ✅ Homepage loads
- ✅ Product browsing works
- ✅ User registration/login
- ✅ Add to cart functionality
- ✅ Checkout with Stripe
- ✅ Order creation
- ✅ Admin panel accessible
- ✅ Static/media files serve correctly
- ✅ Database connection stable


This README includes:
- ✅ Full deployment procedure (see below)
- ✅ Database configuration steps
- ✅ Testing procedures
- ✅ Application purpose explained
- ✅ User value proposition
- ✅ Feature documentation

---

## Database Schema

### Entity Relationship Diagram

```
┌─────────────┐         ┌──────────────┐
│   Category  │────────<│   Product    │
│             │ 1     * │              │
└─────────────┘         └──────────────┘
                               │
                               │ *
                               │
┌─────────────┐         ┌──────────────┐         ┌──────────────┐
│    User     │────────<│     Cart     │>────────│   Product    │
│  (Django)   │ 1     * │              │ *     1 │              │
└─────────────┘         └──────────────┘         └──────────────┘
      │ 1
      │
      │ 1
      ▼
┌─────────────┐
│ UserProfile │
│    (1:1)    │
└─────────────┘
      │
      │ 1
      │
      │ *
      ▼
┌─────────────┐         ┌──────────────┐         ┌──────────────┐
│    Order    │────────<│  OrderItem   │>────────│   Product    │
│             │ 1     * │              │ *     1 │              │
└─────────────┘         └──────────────┘         └──────────────┘
```

### Models Detail

**Product**
- Fields: name, slug, category (FK), description, price, image, stock, available
- Relationships: ForeignKey to Category
- Methods: `in_stock` property

**Category**
- Fields: name, slug, description
- Relationships: One-to-Many with Products

**Cart**
- Fields: user (FK), product (FK), quantity
- Relationships: ForeignKey to User and Product
- Methods: `total_price` property

**Order**
- Fields: user (FK), order_number, shipping info, total_amount, payment_status
- Relationships: ForeignKey to User, One-to-Many with OrderItems
- Methods: Auto-generate order_number on save

**OrderItem**
- Fields: order (FK), product (FK), quantity, price
- Relationships: ForeignKey to Order and Product
- Methods: `total_price` property

**UserProfile**
- Fields: user (OneToOne), phone, bio, avatar
- Relationships: OneToOneField with User
- Signals: Auto-created on user registration

---


## Testing

### Manual Testing Procedures

#### Authentication Testing
| Test | Steps | Expected Result | Status |
|------|-------|----------------|--------|
| User Registration | Visit /accounts/signup, fill form | Account created, redirected to home | ✅ Pass |
| Login | Visit /accounts/login, enter credentials | Logged in, cart available | ✅ Pass |
| Logout | Click logout | Logged out, cart hidden | ✅ Pass |
| Anonymous Cart Access | Visit /cart without login | Redirected to login | ✅ Pass |

#### Product Management Testing (Admin)
| Test | Steps | Expected Result | Status |
|------|-------|----------------|--------|
| Create Product | Click "Add Product", fill form | Product created | ✅ Pass |
| Edit Product | Click edit on product page | Changes saved | ✅ Pass |
| Delete Product | Click delete, confirm | Product removed | ✅ Pass |
| Non-admin Access | Login as regular user | No admin buttons visible | ✅ Pass |

#### Shopping Cart Testing
| Test | Steps | Expected Result | Status |
|------|-------|----------------|--------|
| Add to Cart | Click "Add to Cart" on product | Item added, quantity correct | ✅ Pass |
| Update Quantity | Change quantity in cart | Total updates | ✅ Pass |
| Remove Item | Click remove button | Item deleted from cart | ✅ Pass |
| Stock Validation | Try to add more than stock | Error message shown | ✅ Pass |

#### Checkout & Payment Testing
| Test | Steps | Expected Result | Status |
|------|-------|----------------|--------|
| Stripe Card Element | Visit checkout | Card form displays | ✅ Pass |
| Valid Payment | Use test card 4242... | Payment succeeds | ✅ Pass |
| Invalid Card | Use declined card | Error message shown | ✅ Pass |
| Order Creation | Successful payment | Order created, cart cleared | ✅ Pass |
| Payment Status | Check order detail | Shows "Paid" status | ✅ Pass |

#### Responsive Design Testing
| Device | Resolution | Test Result |
|--------|-----------|-------------|
| Mobile | 375x667 | ✅ Navbar collapses, all features work |
| Tablet | 768x1024 | ✅ Layout adjusts, readable text |
| Desktop | 1920x1080 | ✅ Full layout, all features visible |

#### Browser Compatibility
| Browser | Version | Status |
|---------|---------|--------|
| Chrome | Latest | ✅ Pass |
| Firefox | Latest | ✅ Pass |
| Safari | Latest | ✅ Pass |
| Edge | Latest | ✅ Pass |

### Test Cards (Stripe Test Mode)
- **Success:** 4242 4242 4242 4242
- **Decline:** 4000 0000 0000 0002
- **Insufficient Funds:** 4000 0000 0000 9995

**Any future date for expiry, any 3 digits for CVC**

---
## Installation & Setup

### Prerequisites
- Python 3.11.14
- pip
- PostgreSQL database access
- Stripe account (for payments)

### Local Development Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/shopclub.git
cd shopclub
```

2. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env File**
```bash
touch .env
```

Add the following to `.env`:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=kinzaqureshi_shopclub
DB_USER=kinzaqureshi
DB_PASSWORD=Shopclub123
DB_HOST=postgresql-kinzaqureshi.alwaysdata.net
DB_PORT=5432

STRIPE_PUBLISHABLE_KEY=pk_test_your_key
STRIPE_SECRET_KEY=sk_test_your_key
STRIPE_WEBHOOK_SECRET=
```

5. **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create Superuser**
```bash
python manage.py createsuperuser
```

7. **Collect Static Files**
```bash
python manage.py collectstatic
```

8. **Run Development Server**
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

## Prerequisites
- Ubuntu server (AWS EC2 or similar)

---

## Deployment

### AWS EC2 Deployment Procedure

#### 1. Create EC2 Instance
- **AMI:** Ubuntu Server 22.04 LTS
- **Instance Type:** t2.micro (Free tier)
- **Security Groups:** 
  - SSH (22) - Your IP
  - HTTP (80) - 0.0.0.0/0
  - Custom TCP (8000) - 0.0.0.0/0

#### 2. Connect to EC2
```bash
chmod 400 shopclub-key.pem
ssh -i shopclub-key.pem ubuntu@YOUR-EC2-IP
```

#### 3. Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-dev python3-venv libpq-dev nginx -y
```

#### 4. Setup Project
```bash
sudo mkdir -p /var/www/shopclub
sudo chown ubuntu:ubuntu /var/www/shopclub
cd /var/www/shopclub

# Upload files or git clone
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```



### Clone your repository
```bash
cd ~
git clone <your-repo-url>
cd ShopClubProject4
```

### Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configure Django settings
```bash
nano config/settings.py
```

Update the following:
- `DEBUG = False`
- `ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address']`
- Configure your database settings
- Set a strong `SECRET_KEY`

### Run migrations
```bash
python manage.py migrate
python manage.py collectstatic
```

## 3. Gunicorn Setup

### Create systemd service file
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

### Add the following content:
```ini
[Unit]
Description=gunicorn daemon for ShopClub
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/ShopClubProject4
Environment="PATH=/home/ubuntu/ShopClubProject4/venv/bin"
ExecStart=/home/ubuntu/ShopClubProject4/venv/bin/gunicorn \
          --workers 3 \
          --umask 0007 \
          --bind unix:/home/ubuntu/ShopClubProject4/shopclub.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Enable and start Gunicorn
```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

## 4. Nginx Setup

### Create Nginx configuration
```bash
sudo nano /etc/nginx/sites-available/shopclub
```

### Add the following content:
```nginx
server {
    listen 80;
    server_name your-domain.com your-ip-address;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/ubuntu/ShopClubProject4;
    }

    location /media/ {
        root /home/ubuntu/ShopClubProject4;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/ShopClubProject4/shopclub.sock;
    }
}
```

### Enable the site
```bash
sudo ln -s /etc/nginx/sites-available/shopclub /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 5. File Permissions

### Set correct permissions
```bash
sudo chmod 755 /home/ubuntu
sudo chmod 755 /home/ubuntu/ShopClubProject4
sudo usermod -aG ubuntu www-data
```


## 8. Verify Deployment

Check that all services are running:
```bash
sudo systemctl status gunicorn
sudo systemctl status nginx
```

Visit  site at `http://13.60.188.35/`

## Managing the Application

### Restart Gunicorn after code changes
```bash
sudo systemctl restart gunicorn
```

### View Gunicorn logs
```bash
sudo journalctl -u gunicorn -n 50 --no-pager
```

### View Nginx logs
```bash
sudo tail -n 50 /var/log/nginx/error.log
sudo tail -n 50 /var/log/nginx/access.log
```

### Restart Nginx
```bash
sudo systemctl restart nginx
```





