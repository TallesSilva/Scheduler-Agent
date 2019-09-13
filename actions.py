from typing import Dict, Text, Any, List, Union, Optional

from datetime import datetime
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Action, Tracker
from rasa_sdk.events import SlotSet, Restarted

import scheduler_agent.gcalendar as gc

import logging

DUCKLING_FORMAT = "%Y-%m-%dT%H:%M:%S.%f-07:00"


def _get_customer_data():
    # date = datetime.datetime.now()
    # fetch data from mongo
    # catches and raises anything wrong
    
    return {
        "name": "Rui Conti",
        "cpf": "06426711683",
        "address": "Rua Mario Pinto Sobrinho, 380. Apto 301"
    }

class ActionStartup(Action):
    def name(self):
        return "action_startup"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Olá, tudo bem?")
        #dispatcher.utter_template("utter_greet")

        return []
        # user_cpf = tracker.get_slot("user_id")
        # if user_cpf:
        #     try:
        #         user_data = _get_customer_data(user_cpf)
        #         selected_slots = ["schedule_date"]
        #         #  get more if we want
        #         try:
        #             return [
        #                 SlotSet(slot, user_data.get(slot))
        #                 for slot in selected_slots
        #             ]
        #         except KeyError as ex:
        #             return [SlotSet("failed", True)]  # or pass     
        # return [SlotSet("failed", True)]

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
        # schedule_date = _from_string_to_date(tracker.get_slot("schedule_date"))
        # date_str, hour_str = _split_date_hour(schedule_date)
        # dispatcher.utter_message(
        #     f"Está agendado para {date_str} às {hour_str}"
        # )
        dispatcher.utter_template("utter_ask_confirm_visit",tracker)
        #dispatcher.utter_message("Eu posso confirmar a visita?")
        return []

class ActionSetVisit(Action):
    def name(self):
        return "action_set_visit"
    
    def run(self, dispatcher, tracker, domain):
        # schedule_date = _from_string_to_date(tracker.get_slot("schedule_date"))
        # date_str, hour_str = _split_date_hour(schedule_date)
        # dispatcher.utter_message(
        #     f"Está agendado para {date_str} às {hour_str}"
        # )
        # dispatcher.utter_template("utter_ask_confirm_visit",tracker)
        #dispatcher.utter_message("Eu posso confirmar a visita?")
        return [SlotSet("confirm_visit", True)]

class ActionEnableNotification(Action):
    def name(self):
        return "action_enable_notification"
    
    def run(self, dispatcher, tracker, domain):
        # do something:
        # enable_notifications(tracker.sender_id)
        # OR
        dispatcher.utter_message("Você será informado.")
        return [SlotSet("notification_confirm", True)]
    
class ActionFarewell(Action):
    def name(self):
        return "action_farewell"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_farewell", tracker)
        # do some clean-up:
        # remove_from_redis(tracker.sender_id)
        if tracker.get_slot("confirm_visit"):
            user_data = _get_customer_data()
            start_date = tracker.get_slot("schedule_new_date")
            if not start_date:
                start_date = datetime(2019, 9, 18, 9, 30, 0)
            else:
                start_date = datetime.strptime(start_date, DUCKLING_FORMAT)

            gc.create_event(user_data, start_date)
            dispatcher.utter_message(
                "Beleza! A visita está marcada para o dia {}, às {}. O técnico leva em torno de 30 minutos para concluir a instalação"
                "".format(start_date.strftime("%d/%m"),
                          start_date.strftime("%Hh%M")))
            
        
        return [Restarted()]
 
 
class FormSchedule(FormAction):
    # Get user suggested date using duckling time entity
    
    def name(self):
        return "form_schedule" 
    
    def required_slots(self, tracker: Tracker) -> List[Text]:
    # A list of required slots that the form has to fill
        return ["schedule_new_date"]
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        #Define what the form has to do after all required slots are filled
        dispatcher.utter_message("Nova data registrada com sucesso.")
        #dispatcher.utter_template("utter_inform_new_date", tracker)
        return []
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    # A dictionary to map required slots to
    #    - an extracted entity
    #    - intent: value pairs
    #    - a whole message
    #    or a list of them, where a first match will be picke:
        return {
            "schedule_new_date": [self.from_entity(entity="time"),
                                  self.from_text()],
            #"schedule_new_time": self.from_entity(entity="time")
            }

              
    def validate_schedule_new_date(self,
                                   value,
                                   dispatcher,
                                   tracker:Tracker, domain):
        # value_validated, something = None, None
        # # do logic
        # # value_validated = ..
        # if something:
        #     return {"schedule_day": value}
        # return {"schedule_date": value_validated}
        entities = tracker.latest_message.get("entities", [])
        for entity in entities:
            try:
                date_str = datetime.strptime(entity.get("value", None),
                                             DUCKLING_FORMAT)
                text = entity.get("text", None)
                
                return {
                    "schedule_new_date": date_str.strftime(DUCKLING_FORMAT)
                }
            except ValueError as ex:
                pass
        # nothing passed
        dispatcher.utter_message("Não entendi essa data. Tente me dizer algo do tipo: 'dia 23/08 às 15h', 'quarta as 13h'")
        dispatcher.utter_message("Vou te perguntar de novo")
        return {
            "schedule_new_date": None
        }
        
        # if any(tracker.get_latest_entity_values("time")):
        #     if (int(value[11] + value[12]) <= 8 or int(value[11] + value[12]) >=18):
        #         dispatcher.utter_message("Horário indisponível. Favor informar outro horário")
        #         return{"schedule_new_date": None,
        #             "schedule_new_time": None}
        #     else:
        #         return{"schedule_new_date": value[0:10],
        #                "schedule_new_time": value[11:19]}
        # else:
        #     dispatcher.utter_message("Desculpa, não entendi a data. Você poderia me dizê-la em outro formato")
        #     return{"schedule_new_date": None,
        #            "schedule_new_time": None}
        
    
    # def validate_schedule_new_time(self, value, dispatcher, tracker: Tracker, domain):
    #     # value_validated = None
    #     # validate hour
    #     return {"schedule_new_time": value[11:19]}