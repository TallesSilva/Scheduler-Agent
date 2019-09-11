## happy path 1
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit   
* affirm
    - utter_ask_confirm_notification
* affirm
    - action_enable_notification
    - utter_thanks
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
    - slot{"schedule_new_data": "Thu 25 May 2020"}
    - utter_thanks
* affirm OR bye OR thanks
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
    - slot{"schedule_date": "Thu 25 May 2020"}
    - utter_thanks
* affirm OR bye OR thanks
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

## happy path 4
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* affirm
    - utter_ask_confirm_notification
* affirm
    - action_enable_notification
    - utter_thanks
    - action_farewell

## happy path 4
* greet{"user_id": "20255684978"}
    - slot{"user_id": "20255684978"}
    - action_startup
    - slot{"schedule_date": "Thu 24 May 2019"}
    - utter_ask_confirm_installation
* affirm
    - action_confirm_visit
* affirm
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
