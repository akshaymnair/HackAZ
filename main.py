import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Sixth Sense- AI CCTV and Audio Monitoring System!')
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
