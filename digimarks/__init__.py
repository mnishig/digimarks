import os

from flask import Flask


def create_app(test_config=None):
    # create our flask app and a database wrapper
    app = Flask(__name__)
    app.config.from_object(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('settings.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Strip unnecessary whitespace due to jinja2 codeblocks
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # set custom url for the app, for example '/bookmarks'
    try:
        # TODO: get settings from ENV vars
        app.config['APPLICATION_ROOT'] = os.environ['APPLICATION_ROOT']
    except AttributeError:
        pass

    return app
