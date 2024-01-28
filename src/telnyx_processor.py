import os
from dotenv import load_dotenv
import requests
from pprint import pprint
from logger import logger as logging
import utils

load_dotenv()

API_KEY = os.getenv("API_KEY")
PUBLIC_KEY = os.getenv("API_KEY")


def check_telnyx_delivery_status(message_id):

    logging.info(f"{check_telnyx_delivery_status.__name__} -- CHECKING TELNYX DELIVERY STATUS FOR - {message_id}")

    response = requests.get(
        url=f"https://api.telnyx.com/v2/messages/{message_id}", 
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
            }
        )
    
    status_code = response.status_code
    delivery_status = None
    logging.info(f"{check_telnyx_delivery_status.__name__} -- TELNYX STATUS CODE -- {status_code}")

    try:
        response_data = response.json()
        logging.info(f"{check_telnyx_delivery_status.__name__} -- TELNYX RESPONSE DATA -- {response_data}")

        delivery_status = response_data["data"]["to"][-1]["status"]
    except Exception as ex:
        logging.error(f"{check_telnyx_delivery_status.__name__} -- !!! TELNYX ERROR -- {ex}")

    return True if delivery_status == "delivered" else False
    


def send_telnyx_sms(phone_number, sms_message: str, from_number):
    """
    sends single SMS message with Telnyx
    """
    phone_number_validated = utils.format_phone_number(phone_number)

    logging.info(f"{send_telnyx_sms.__name__} -- TELNYX - SENDING SMS TO - {phone_number} FROM - {from_number}")

    # numbers = ["+19172031898", "+19172031897"]
    # # numbers = ["+19172031916", "+19172031883"]
    # from_number = numbers[randint(0, len(numbers) - 1)]

    response = requests.post(
        url="https://api.telnyx.com/v2/messages",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "type": "SMS",
            "text": f"{sms_message}",
            "from": from_number,
            "to": phone_number_validated
        }
    )


    status_code = response.status_code
    logging.info(f"{send_telnyx_sms.__name__} -- TELNYX - STATUS CODE -- {status_code}")

    result = {
        "success": True if status_code == 200 else False, 
        "data": None,
        "message_id": None
        }

    try:
        response_data = response.json()
        logging.info(f"{send_telnyx_sms.__name__} -- TELNYX - RESPONSE DATA -- {response_data}")

        result["data"] = response_data["data"]
        result["message_id"] = response_data["data"]["id"]
    except Exception as ex:
        logging.error(f"{send_telnyx_sms.__name__} -- !!! TELNYX ERROR -- {ex}")

    return result
    


if __name__ == "__main__":

    telnyx_sms_sending_result = send_telnyx_sms("+38067dasdaadas", "Hello!\n\nI'm Adam Shapiro from Military & Patriots Investment Group. We have exciting Self-Storage investment opportunities for potential partners. I'd like to introduce you to an Argus development in San Antonio, Texas. The asset offers a potential 21+% IRR and 57%+ ROI. The project spans over 80,000 sq ft, features 700+ climate-controlled units, and provides a great exit opportunity in 2 years with institutional quality buyers. With our track record of 200+ ground-up projects, most being 2-year holds, it's a compelling opportunity.\n\nInterested? Reply 'Yes.'\n\nNot interested? Reply 'OUT' to opt out.\n\nBest regards,\nAdam Shapiro")
    pprint(telnyx_sms_sending_result)

    # message_delivered = check_telnyx_delivery_status(telnyx_sms_sending_result["message_id"])
    # pprint(message_delivered)