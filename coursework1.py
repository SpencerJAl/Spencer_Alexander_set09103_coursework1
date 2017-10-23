import ConfigParser
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html')

@app.route('/century')
def century():
  return render_template('century.html')

@app.route('/artist')
def artist():
  return render_template('artist.html')

@app.route('/country')
def country():
  return render_template('country.html')

@app.route('/artist/gogh')
def gogh():
  return render_template('gogh.html')

@app.route('/artist/DaVinci')
def vinci():
   return render_template('vinci.html')
@app.route('/artist/picasso')
def picasso():
  return render_template('picasso.html')

@app.route('/config/')
def config():
  str = []
  str.append('Debug:'+app.config['DEBUG'])
  str.append('port:'+app.config['port'])
  str.append('url:'+app.config['url'])
  str.append('ip_address:'+app.config['ip_address'])
  return '/t'.join(str)

def init(app):
   config = ConfigParser.ConfigParser()
   try:
     config.location = "etc/defaults.cfg"
     config.read(config.location)

     app.config['DEBUG'] = config.get("config", "debug")
     app.config['ip_address'] = config.get("config", "ip_address")
     app.config['port'] = config.get("config", "port")
     app.config['url'] = config.get("config", "url")
   except:
     print "Could not get config details: ", config.location

@app.errorhandler(404)
def page_not_found(error):
 return render_template('404.html'), 404


if __name__ == "__main__":
 init(app)
 app.run(
    host=app.config['ip_address'],
    port=init(app.config['port']))
