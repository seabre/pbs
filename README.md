#PBS

A Python (2.7) interface to [PaperBackSwap](http://www.paperbackswap.com/).

##Installation

Clone this repo.

Run `python setup.py install`, possibly with superuser permissions.

If everything went well, you should be good to go.

##Example script

`import pbs`

`p = pbs.PBS()`

`print p.recentlyswapped()`

##API Documentation

As far as using the library is concerned, the code right now is your best reference.

For API documentation, see [PaperBackSwap's API documentation](http://www.paperbackswap.com/developers/v1-xml.php). This documentation is actually for the XML API, but it's the same for their JSON API.

All method calls in this library are lowercase, so where you might see `RecentlySwapped` in their documentation, in this library it would be referred to as `recentlyswapped`.

##TODO

Lots of things.

* I don't have exception handling. That needs to be done.
* The calls to the API could be generalized.
* Tests.

This was written in roughly an hour. I met the PaperBackSwap guys at a bar for dinner and decided to play with their API when I got home, so yes Virgina, there are bugs.
