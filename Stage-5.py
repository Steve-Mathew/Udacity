#Import whatever I need to import.
import os
import urllib
import webapp2
import jinja2

#This creates a Jinja Environment of some kind.
Template_Directory = os.path.join(os.path.dirname(__file__), 'Templates')
Jinja_Environment = jinja2.Environment(loader = jinja2.FileSystemLoader(Template_Directory), autoescape = True)

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
        self.render("Stage_5_Main_Template.html")

#This shows my discussion of the topic that I chose to explore.
class Exploration(Handler):
    def get(self):
        self.render("Stage_5_iOS_Development.html")

#This discusses the first link that I chose to highlight.
class Hyperlink1(Handler):
    def get(self):
        self.render("Stage_5_Apple_Developer_Resources.html")

#This discusses the second link that I chose to highlight.
class Hyperlink2(Handler):
    def get(self):
        self.render("Stage_5_iOS_Dev_Weekly.html")

#This essentially creates addresses for all pages within this website.
app = webapp2.WSGIApplication([('/', MainPage), ('/exploration', Exploration), ('/hyperlink1', Hyperlink1), ('/hyperlink2', Hyperlink2)], debug=True)
