# Example package with a console entry point
import json
import urllib
import urllib2

class PBS:

    def getrequest(self, url):
        opener = urllib2.build_opener()
        f = opener.open(url)
        return json.load(f)
    
    def bookshelf(self, memberid="", limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'Bookshelf',
             'MemberID' : memberid,
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)


    def booksread(self, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'BooksRead',
             'MemberID' : memberid,
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params
 
        return self.getrequest(request)


    def clubwishlist(self, isbns, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'ClubWishList',
             'Limit' : limit,
             'Offset' : offset,
             'ISBN' : ','.join(isbns)
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)


    def isbnlist(self, isbns, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'ISBNList',
             'Limit' : limit,
             'Offset' : offset,
             'ISBN' : ','.join(isbns)
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)
        


    def memberreviews(self, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'MemberReviews',
             'MemberID' : memberid,
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)



    def memberwishlist(self, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'MemberWishList',
             'MemberID' : memberid,
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)



    def recentlyposted(self, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'RecentlyPosted',
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)



    def recentlyswapped(self, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'RecentlySwapped',
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)



    def tbrpile(self, limit=10, offset=0):
        params = urllib.urlencode(
            {'RequestType' : 'TBRPile',
             'MemberID' : memberid,
             'Limit' : limit,
             'Offset' : offset
            })
        request = "http://www.paperbackswap.com/api/v2/index.php?" + params

        return self.getrequest(request)
