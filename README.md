# Auction Site

A Django-based auction platform implementing listings, bidding, comments, watchlists and categories.  
The application follows the CS50W auction specification and includes full admin management for listings, bids and comments.

## Features

### Models
- **Listing** — represents an auction listing with fields such as title, description, starting bid, current active flag, optional image URL and optional category.
- **Bid** — stores bids tied to a listing and a user, with the bid amount and timestamp.
- **Comment** — stores user comments on listings with text and timestamp.
- **User** — authentication uses Django’s built-in User model.
- Listings, bids and comments are manageable through the Django admin interface.

### Create Listing
- Authenticated users can create new listings with:
  - Title
  - Description
  - Starting bid (numeric)
  - Optional image URL
  - Optional category
- New listings are active by default until closed by their creator.

### Active Listings Page (Home)
- Default route displays all **active** listings.
- Each listing preview shows: title, short description, current price, and image (if available).
- Listings link to their dedicated listing pages.

### Listing Page
- Displays full details: title, description, image, starting bid, current price, bid history, comments, and active/closed status.
- Signed-in users can:
  - **Add/remove** the listing from their watchlist.
  - **Place bids**: bids must be >= starting bid and greater than any existing bids; invalid bids yield clear error feedback.
  - **Post comments** which are shown on the listing page.
- The listing creator can **close the auction**, making the highest bidder the winner and deactivating the listing.
- Closed listings indicate the winner; if the signed-in user is the winner, the page states this.

### Watchlist
- Users can add listings to a personal watchlist.
- A dedicated Watchlist page shows all saved listings and links to each listing page.

### Categories
- A Categories page lists all categories used by listings.
- Clicking a category shows all active listings in that category.

### Admin Interface
- The Django admin allows administrators to view, add, edit, and delete listings, bids and comments.

## Running Locally

To run the project on your machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/matheusesilva/commerce.git
   cd commerce

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install Django:
   ```bash
   pip install django

4. Apply database migrations:
   ```bash
   python manage.py makemigrations auctions
   python manage.py migrate

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser

6. Start the development server:
   ```bash
   python manage.py runserver
   
7. Visit the app in your browser:
   ```bash
   http://127.0.0.1:8000/
