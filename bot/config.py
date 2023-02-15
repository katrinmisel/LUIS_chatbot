#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "9d9fad9e-518e-4533-947d-b1eef182c3fe")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "4TZ8Q~ORsqvoc4M5D.69QfcOy9iWtaRdI4iSWb9b")
    LUIS_APP_ID = os.environ.get("LuisAppId", "9a2e59b9-686d-492b-959b-8ceff62b8494")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "31031bdf48c943c5a836b722abe99440")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://flymeresource.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "000913e9-cbba-4159-8d42-83f9e90a4efc"
    )