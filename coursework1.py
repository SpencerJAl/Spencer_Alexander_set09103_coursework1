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
  return render_template('artist.php')

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

@app.route('/country/france')
def france():
  return render_template('france.html')

@app.route('/country/italy')
def italy():
  return render_template('italy.html')

@app.route('/country/netherlands')
def netherlands():
  return render_template('netherlands.html')

@app.route('/century/19th')
def ninth():
  return render_template('19th.html')

@app.route('/century/18th')
def eighth():
  return render_template('18th.html')

@app.route('/century/15th')
def fifth():
  return render_template('15th.html')

@app.route('/artist/vincent')
def redv():
  return redirect(url_for('gogh'))

@app.route('/artist/vincentvan')
def redvv():
  return redirect(url_for('gogh'))

@app.route('/artist/vincentvangogh')
def redvvg():
  return redirect(url_for('gogh'))

@app.route('/artist/vangogh')
def redvg():
  return redirect(url_for('gogh'))

@app.route('/artist/GOGH')
def redg():
  return redirect(url_for('gogh'))

@app.route('/artist/VINCENT')
def redV():
  return redirect(url_for('gogh'))

@app.route('/artist/VINCENTVAN')
def redVV():
  return redirect(url_for('gogh'))

@app.route('/artist/VINCENTVANGOGH')
def redVVG():
  return redirect(url_for('gogh'))

@app.route('/artist/vincent van')
def redv_v():
  return redirect(url_for('gogh'))

@app.route('/artist/vincent van gogh')
def redv_v_g():
  return redirect(url_for('gogh'))

@app.route('/artist/VINCENT VAN')
def redV_V():
  return redirect(url_for('gogh'))

@app.route('/artist/VINCENT VAN GOGH')
def redV_V_G():
  return redirect(url_for('gogh'))

@app.route('/artist/pablo')
def redpa():
  return redirect(url_for('picasso'))

@app.route('/artist/PABLO')
def redPA():
  return redirect(url_for('picasso'))

@app.route('/artist/Pablo')
def redPa():
  return redirect(url_for('picasso'))

@app.route('/artist/pablo picasso')
def redpp():
  return redirect(url_for('picasso'))

@app.route('/artist/PABLO PICASSP')
def redPP():
  return redirect(url_for('picasso'))

@app.route('/artist/Pablo Picasso')
def redPaPi():
  return redirect(url_for('gogh'))

@app.route('/artist/piccaso')
def redp():
  return redirect(url_for('picasso'))

@app.route('/artist/da vinci')
def redda():
  return redirect(url_for('DaVinci'))

@app.route('/artist/DA VINCI')
def redDA():
  return redirect(url_for('DaVinci'))

@app.route('/artist/leonardo')
def redleo():
  return redirect(url_for('DaVinci'))

@app.route('/artist/Leonardo')
def redLeo():
  return redirect(url_for('DaVinci'))

@app.route('/artist/LEONARDO')
def redLEO():
  return redirect(url_for('DaVinci'))

@app.route('/artist/leonardo da vinci')
def redleod():
  return redirect(url_for('DaVinci'))

@app.route('/artist/Leonardo Da Vinci')
def redLeoD():
  return redirect(url_for('DaVinvi'))

@app.route('/artist/LEONARDO DA VINCI')
def redLEOD():
  return redirect(url_for('DaVinci'))


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
