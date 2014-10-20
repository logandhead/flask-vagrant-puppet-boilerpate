from flask.ext.assets import Environment, Bundle

def asset_register(app):

   assets = Environment(app)

   assets.config['less_bin'] = '/usr/local/node/node-v0.10.32/bin/lessc'
   assets.config['less_run_in_debug'] = True

   css_bundle = Bundle('css/*.css', 'css/less/default.less',
                         filters='less', output='styles.css')

   assets.register('css_main', css_bundle)

   return assets



