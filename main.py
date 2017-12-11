
import webapp2

form="""
<form action="/testform" >
    <input type="text" name="query"/>
    <button type="submit">Submit</button>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)


class TestFormHandler(webapp2.RequestHandler):
    def get(self):
        query=self.request.get('query')
        self.response.out.write(query)
        # self.response.headers["Content-Type"]="text/plain"
        # self.response.out.write(self.request)


app = webapp2.WSGIApplication([
    ('/', MainHandler),('/testform',TestFormHandler)
], debug=True)
