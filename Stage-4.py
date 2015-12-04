#Import whatever I need to import.
#At this point, just throw everything in there!
#I'll figure out what I don't need later!
import os
import urllib
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import cgi

#This creates a Jinja Environment of some kind.
Template_Directory = os.path.join(os.path.dirname(__file__), 'Templates')
Jinja_Environment = jinja2.Environment(loader = jinja2.FileSystemLoader(Template_Directory), autoescape = True)

#This is for circumventing user input of HTML.
def escape_html(s):
    return cgi.escape(s, quote=True)

#This handles the display of web pages.
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_string(self, template, **params):
        t = Jinja_Environment.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_string(template, **kw))

#This is the header, which also works as a homepage.
class MainPage(Handler):
    def get(self):
        self.render("Stage_4_Main_Template.html")

#This shows the Networks section of Stage 4.
class Networks(Handler):
    def get(self):
        self.render("Stage_4_Networks.html")

#This discusses terms used to describe how HTML sends and receives data.
class Networks_and_HTML(Handler):
    def get(self):
        self.render("Stage_4_Networks_and_HTML.html")

#This discusses the use of templates for rendering web pages.
class HTMLTemplates(Handler):
    def get(self):
        self.render("Stage_4_HTML_Templates.html")

#This discusses databases.
class Databases(Handler):
    def get(self):
        self.render("Stage_4_Databases.html")

#This is supposed to establish the database for user comments.
class Comment(ndb.Model):
    username = ndb.StringProperty(indexed=True)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
    key = ndb.key("Thoughts")

user_comment = Comment()

#This is where users are supposed to be able to post comments, as well as view other people's comments...except I can't get this to work properly.
class Commentary(Handler):
    def get(self):
        comments_query = Comment.query(key="Thoughts")#.order(-date)
        self.render("Stage_4_Commentary.html", user_comment = user_comment, comments_query = comments_query)
        
class Commentary2(Handler):
    def post(self):
        user_comment.username = self.request.get('username')
        user_comment.content = self.request.get('content')
        user_comment.put()
        #Is anything actually getting "put"?!
        
        comments_query = Comment.query(key="Thoughts")#.order(-date)
        self.render("Stage_4_Commentary.html", user_comment = user_comment, comments_query = comments_query)
        #Using the statement "sample_user = sample_user" is accepted, rather than just "sample_user"; the log will say "render() accepts exactly 2 arguments (5 given)" otherwise (for this scenario).  Is that how it's supposed to work?

#This essentially creates addresses for all pages within this website.
app = webapp2.WSGIApplication([('/', MainPage), ('/networks', Networks), ('/networks_and_html', Networks_and_HTML), ('/html_templates', HTMLTemplates), ('/databases', Databases), ('/commentary', Commentary), ('/sign', Commentary2)], debug=True)
