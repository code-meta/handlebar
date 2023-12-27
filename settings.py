class Site:
    YOUTUBE = "youtube"
    IMDB = "imdb"
    GOOGLE = "google"
    YAHOO = "yahoo"
    HEALTHLINE = "healthline"
    MDN = "mdn"


SITE = Site()


DEFAULT_SITES = [
    SITE.YOUTUBE,
    SITE.IMDB,
    SITE.GOOGLE,
    SITE.YAHOO,
    SITE.HEALTHLINE,
    SITE.MDN,
]

HELP_TEXT = """
Learn to use the followings in order use hanlebar better

open sites with:
    site_name 
        Example: youtube
        default supported sites are:
            - youtube      ==   youtube.com 
            - imdb         ==   imdb.com 
            - google       ==   google.com   
            - yahoo        ==   yahoo.com   
            - healthline   ==   healthline.com    
            - mdn          ==   developer.mozilla.org 

        for other sites you can use the following:
            site_domain or site_url
            Example: nytimes.com/international
        
        to open sites in a private tab use the following:
            site_name -p 
                Example: youtube -p
            site_domain -p or site_url -p 
                Example: nytimes.com/international -p
"""
