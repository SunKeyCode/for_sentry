import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://f000efd81b164e909f4134a0268b77a0@o4504164192681984.ingest.sentry.io/4504174631583744",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route("/example")
def example():
    pass


@app.route("/")
def index():
    return "Main page"


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    app.run(debug=True)
