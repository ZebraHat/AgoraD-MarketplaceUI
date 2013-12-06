AgoraD-MarketplaceUI
====================
Another django project which will have closed signups. An organization that wishes to create a data sharing marketplace (like us) will host the project on their servers and fascilitate the transfer of data. In order to join the exchange, you would contact the marketplace manager and be let in. You would then be able to browse the data sellers and contact information. Once an agreement is reached, the seller clicks a button to initiate transfer to another user, that user then accepts and the transfer starts. Marketplace tracks these deals.

Instructions for setup:

    1) Clone repository recursively to ensure all the submodules are pulled in ("$ git clone --recursive git@github.com:ZebraHat/AgoraD-MarketplaceUI.git")
    2) Pull in necessary requirements ("$ sudo pip install -r requirements.txt"), or install in a virtualenv (recommended)
    3) Sync and install the database (you'll need sqlite3 if you don't already have it) -- "$ python manage.py syncdb"
    4) Test using "$ python manage.py runserver 0.0.0.0 " (Or leave off the ports if you're just testing locally)
    5) Leave server running using your favorite Django-interfaceable webservers (like uWSGI + NGINX)

Instructions for new user setup:

    1) Enter the admin page at /admin, using the credentials you established when installing the database
    2) Go through the normal django procedure of adding a user
    3) Provide the username and password created to the new user

Current State
-------------
The repository has
 * base templates adopted from https://github.com/IronSummitMedia/startbootstrap/tree/master/templates/sb-admin
 * landing page adopted from https://github.com/IronSummitMedia/startbootstrap/blob/master/templates/stylish-portfolio.html
 * bootstrap submodule https://github.com/twbs/bootstrap
