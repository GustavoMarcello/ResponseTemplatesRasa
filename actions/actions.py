
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict


class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_oitava"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Compass.uol",
                        "subtitle": "DreamBiggerAways",
                        "image_url": "https://i.ytimg.com/vi/YuAG9joAUmw/maxresdefault.jpg",
                        "buttons": [ 
                            {
                            "title": "Início",
                            "payload": "exemplos",
                            "type": "postback"
                            },
                            {
                            "title": "Linkedin",
                            "url": "https://www.linkedin.com/company/compass-uol/mycompany/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Rasa",
                        "subtitle": "Opensource chatbot",
                        "image_url": "https://miro.medium.com/max/1200/1*Bs0JvC6bmiwrC7we49-tjw.png",
                        "buttons": [ 
                            {
                            "title": "Início",
                            "payload": "exemplos",
                            "type": "postback"
                            },
                            {
                            "title": "Linkedin",
                            "url": "https://www.linkedin.com/company/rasa/",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Carrossel")
        dispatcher.utter_message(attachment=message)
        
        return []
