import requests
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill


class HistoryDeathSkill(OVOSSkill):

    @intent_handler("deaths_in_history.intent")
    def handle_random_event_intent(self, message):
        req = requests.get('http://history.muffinlabs.com/date')
        person = req.json()['data']['Deaths'][0]['text']
        self.speak_dialog("died_this_date", {"person": person})

    @intent_handler("births_in_history.intent")
    def handle_random_event_intent(self, message):
        req = requests.get('http://history.muffinlabs.com/date')
        person = req.json()['data']['Births'][0]['text']
        self.speak_dialog("born_this_date", {"person": person})

    @intent_handler("events_in_history.intent")
    def handle_random_event_intent(self, message):
        req = requests.get('http://history.muffinlabs.com/date')
        person = req.json()['data']['Events'][0]['text']
        self.speak_dialog("today_in_history", {"event": person})
