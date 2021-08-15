from flask import Flask
from flask import render_template


def create_app(test_config=None):
    # create and configure the App
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

#    @app.route("/")
#    def hello_world():
#        return "<p>Hello, World!</p>"

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)

    import eyezoochi
    app.register_blueprint(eyezoochi.bp)
    app.add_url_rule('/', endpoint='index')


    return app

app = create_app()
if __name__ == '__main__':
    app.run()
