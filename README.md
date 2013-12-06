AgoraD-MarketplaceUI
====================
The AgoraD MarketplaceUI is an easy to install and configure django project to manage multiple AgoraD Loading Dock nodes. The Marketplaces are designed to have closed signups, but anyone may run a Marketplace.

A typical use case is that two companies would like to buy or sell their data, but the only way to do so would be to have engineers spend days or weeks tranfering this database out of the seller's and into the buyer's (made especially difficult if the buyer and seller have different datastore types and environments).

The AgoraD project looks to simplify this process by supporting several drivers for multiple datastores and datastore versions. Sharing your data (or even migrating internally) should be as easy as installing and configuring a Loading Dock, and registering it with a Marketplace.

Once the Marketplace is up and running, it has a simple and intuitive web GUI that let's you browse other's data offerings and contact those sellers about a potential purchase agreement. Monetary transfer and contractual agreements are outside the scope and domain of the project, so all of those negotiations should still happen offline.

--------------------------------

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
