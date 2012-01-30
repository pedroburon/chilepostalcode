from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import urllib2

try:
    import simplejson as json
except ImportError:
    import json

from BeautifulSoup import BeautifulSoup


DATA_STRING = 'origen=p&szEstConsulta=OK&calle=%(street)s&numero=%(number)s&comuna=%(commune)s'
URL_STRING = 'http://codigopostal.correos.cl/correos_cp/soporte_web/consulta_web/versionphp2006/' \
             'pagina_interior/codigo_postal/Correos_codigoPostal_NEW/pgn_modulo_codigopostal.asp'


class MainPage(webapp.RequestHandler):
    def get(self):
        street = self.request.get('street', '')
        number = self.request.get('number', '')
        commune = self.request.get('commune', '')
        callback = self.request.get('callback', False)

        params = {'number': number, 'commune': commune, 'street': street}
        data = (DATA_STRING % params).replace(' ', '+')
        page = urllib2.urlopen(URL_STRING, data)

        soup = BeautifulSoup(page)
        
        span = soup.find('span', {'class': 'rojo'})
        if span:
            params.update({'postalcode': span.text})
        else:
            params.update({'postalcode': None, 'error': 'Error'})
         
        response = json.dumps(params)

        self.response.headers['Content-Type'] = 'application/json'
        if callback:
            self.response.headers['Content-Type'] = 'text/javascript'
            response = '%(callback)s(%(response)s)' % {'callback': callback, 'response': response}

        self.response.out.write(response)


application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
