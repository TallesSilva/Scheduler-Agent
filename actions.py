import datetime
from rasa_sdk.interfaces import Action, FormAction
from rasa_sdk.events import SlotSet, Restarted

def _get_customer_data(user_cpf: str):
    date = datetime.datetime.now()
    # fetch data from mongo
    # catches and raises anything wrong
    
    return {
        "user_cpf": user_cpf,
        "user_address": "Av. Floriano Peixoto, 345. Apto 302",
        "schedule_date": str(date)
    }

class ActionStartup(Action):
    def name(self):
        return "action_startup"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("utter_greet", tracker)
        user_cpf = tracker.get_slot("user_id")
        if user_cpf:
            try:
                user_data = _get_customer_data(user_cpf)
                selected_slots = ["schedule_date"]
                #  get more if we want
                try:
                    return [
                        SlotSet(slot, user_data.get(slot))
                        for slot in selected_slots
                    ]
                except KeyError as ex:
                    return [SlotSet("failed", True)]  # or pass     
        return [SlotSet("failed", True)]

# class ActionConfirmInstallation(Action):
#     def name(self):
#         return "action_confirm_installation"
    
#     def run(self, dispatcher, tracker, domain):
#         return []

def _from_string_to_date(string: str):
    # TODO: do
    # return string
    raise NotImplementedError

def _split_date_hour(date: datetime):
    raise NotImplementedError

class ActionConfirmVisit(Action):
    def name(self):
        return "action_confirm_visit"
    
    def run(self, dispatcher, tracker, domain):
        schedule_date = _from_string_to_date(tracker.get_slot("schedule_date"))
        date_str, hour_str = _split_date_hour(schedule_date)
        dispatcher.utter_message(
            f"Está agendado para {date_str} às {hour_str}"
        )
        dispatcher.utter_template("utter_ask_confirm_visit")
        return []

class ActionEnableNotification(Action):
    def name(self):
        return "action_confirm_notification"
    
    def run(self, dispatcher, tracker, domain):
        # do something:
        # enable_notifications(tracker.sender_id)
        # OR
        return [SlotSet("notification_confirm", True)]

class ActionFarewell(Action):
    def name(self):
        return "action_farewell"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_farewell", tracker)
        # do some clean-up:
        # remove_from_redis(tracker.sender_id)
        
        return [Restarted()]
    
class FormSchedule(FormAction):
    def name(self):
        return "form_schedule"
    
    def required_slots(self, tracker):
        if tracker.get_slot("schedule_day", None):
            return [
                "schedule_hour"
            ]
        return [
            "schedule_date"
        ]
        
    def slot_mappings(self):
        return {
            "schedule_date": [self.from_entity(entity="time")]
        }
        
    def validate_schedule_hour(self, value, dispatcher, tracker, domain):
        value_validated = None
        # validate hour
        return {"schedule_hour": value_validated}
    
    def validate_schedule_date(self, value, dispatcher, tracker, domain):
        value_validated, something = None, None
        # do logic
        # value_validated = ..
        if something:
            return {"schedule_day": value}
        return {"schedule_date": value_validated}
    
    def submit(self, dispatcher, tracker, domain):
        return []