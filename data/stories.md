## happy path 1
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit   
* affirm
    - action_set_visit
    - slot{"confirm_visit": true}
    - utter_ask_confirm_notification
* affirm
    - action_enable_notification
    - action_farewell

## happy path 2
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit   
* deny
    - utter_ask_reschedule
* affirm
    - form_schedule
    - form{"name": "form_schedule"}
    - form{"name": null}
    - utter_inform_new_date
* affirm OR thanks
    - action_set_visit
    - slot{"confirm_visit": true}
    - utter_ask_confirm_notification
* affirm
    - action_enable_notification
    - action_farewell

## happy path 3
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* deny
    - utter_ask_reschedule
* affirm
    - form_schedule
    - form{"name": "form_schedule"}
    - form{"name": null}
    - utter_inform_new_date
* affirm OR thanks
    - action_set_visit
    - slot{"confirm_visit": true}
    - utter_ask_confirm_notification
* deny
    - utter_acknowledge_thanks
    - action_farewell

## happy path 4
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* deny
    - utter_ask_reschedule
* deny
    - utter_apologise
    - action_farewell

## happy path 5
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* affirm
    - action_set_visit
    - slot{"confirm_visit": true}
    - utter_ask_confirm_notification
* deny
    - utter_acknowledge_thanks
    - action_farewell

## happy path 6
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* deny
    - utter_ask_reschedule
* affirm
    - form_schedule
    - form{"name": "form_schedule"}
    - form{"name": null}
    - utter_inform_new_date
* deny
    - utter_ask_reschedule
* affirm
    - form_schedule
    - form{"name": "form_schedule"}
    - form{"name": null}
    - utter_inform_new_date
* affirm OR thanks
    - action_set_visit
    - slot{"confirm_visit": true}
    - utter_ask_confirm_notification
* affirm
    - action_enable_notification
    - action_farewell

## happy path 7
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* deny
    - utter_ask_reschedule
* affirm
    - form_schedule
    - form{"name": "form_schedule"}
    - form{"name": null}
    - utter_inform_new_date
* deny
    - utter_ask_reschedule
* affirm
    - form_schedule
    - form{"name": "form_schedule"}
    - form{"name": null}
    - utter_inform_new_date
* affirm OR thanks
    - action_set_visit
    - slot{"confirm_visit": true}
    - utter_ask_confirm_notification
* deny
    - utter_acknowledge_thanks
    - action_farewell

## sad path 1
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* deny
    - utter_confirm_wrong
* affirm
    - utter_apologise
    - utter_acknowledge_thanks
    - action_farewell

## sad path 2
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"failed": true}
    - utter_failure
    - utter_apologise
    - action_farewell 
