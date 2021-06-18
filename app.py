import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
sentry_sdk.init(dsn="https://examplePublicKey@o0.ingest.sentry.io/0", integrations=[FlaskIntegration()])
# ... rest