# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from enum import Enum
from typing import Dict, Tuple
from botbuilder.ai.luis import LuisRecognizer
from botbuilder.core import IntentScore, TopIntent, TurnContext
from booking_details import BookingDetails


class Intent(Enum):
    BOOK_FLIGHT = "BookFlight"
    CANCEL = "Cancel"
    NONE_INTENT = "NoneIntent"


def top_intent(intents: Dict[Intent, dict]) -> TopIntent:
    max_intent = Intent.NONE_INTENT
    max_value = 0.0

    for intent, value in intents:
        intent_score = IntentScore(value)
        if intent_score.score > max_value:
            max_intent, max_value = intent, intent_score.score

    return TopIntent(max_intent, max_value)


class LuisHelper:
    @staticmethod
    async def execute_luis_query(
        luis_recognizer: LuisRecognizer, turn_context: TurnContext
    ) -> Tuple[Intent, object]:
        """
        Returns an object with preformatted LUIS results for the bot's dialogs to consume.
        """
        result = None
        intent = None

        try:
            recognizer_result = await luis_recognizer.recognize(turn_context)
            intent = recognizer_result.get_top_scoring_intent().intent

            if intent == Intent.BOOK_FLIGHT.value:
                result = BookingDetails()

                # We need to get the result from the LUIS JSON which at every level returns an array.
                
                #to_entities = recognizer_result['entities']['$instance']['dst_city'][0]
                #if to_entities:
                #    result.dst_city = to_entities[0]["text"].capitalize()
                #else: result.dst_city = None

                result.dst_city = recognizer_result.entities.get("$instance", {}).get("dst_city", [])[0].get("text").capitalize()
                result.or_city = recognizer_result.entities.get("$instance", {}).get("or_city", [])[0].get("text").capitalize()

                # This value will be a TIMEX. And we are only interested in a Date so grab the first result and drop
                # the Time part. TIMEX is a format that represents DateTime expressions that include some ambiguity.
                # e.g. missing a Year.
                result.str_date = "2020-01-01"
                result.end_date = "2020-01-02"
                #result.budget = str(recognizer_result.entities.get("$instance", {}).get("str_date", [])[0])
                result.budget = recognizer_result.entities.get("$instance", {}).get("budget", [])[0].get("text")


        except Exception as exception:
            print(exception)

        return intent, result