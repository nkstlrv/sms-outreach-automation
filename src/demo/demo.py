from pprint import pprint

demo = {'status_code': 200, 'phone_number': '(844) 900-0770', 'phone_number_validated': '+18449000770', 'ghl_contact_id': 0, 'result': {'data': {'record_type': 'message', 'direction': 'outbound', 'id': '40318d32-18de-46ad-8e92-3e2da6c9a3f1', 'type': 'SMS', 'organization_id': '279c618d-f76a-441b-861e-376ea14716e2', 'messaging_profile_id': '4001873e-ed66-4208-a51a-1fab1f3f491b', 'from': {'phone_number': '+19172031916', 'carrier': 'Telnyx', 'line_type': 'Wireless'}, 'to': [
    {'phone_number': '+18449000770', 'status': 'queued', 'carrier': '', 'line_type': ''}], 'cc': [], 'text': 'Hello, Test', 'media': [], 'webhook_url': 'https://hook.us1.make.com/cb7l4499l40gdpgfpighl13m8v3dlp9t', 'webhook_failover_url': '', 'encoding': 'GSM-7', 'parts': 1, 'tags': [], 'cost': {'amount': '0.0040', 'currency': 'USD'}, 'received_at': '2024-01-22T16:55:07.127+00:00', 'sent_at': None, 'completed_at': None, 'valid_until': '2024-01-22T17:55:07.127+00:00', 'errors': []}}}


pprint(demo["result"]["data"]["errors"])