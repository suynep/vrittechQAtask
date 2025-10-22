import dotenv
import json
import re
import mailslurp_client
import os

dotenv.load_dotenv()

#####################################################################

configuration = mailslurp_client.Configuration()
configuration.api_key["x-api-key"] = (
    os.environ.get("MAILSLURP_API")
)


def create_random_email():
    with mailslurp_client.ApiClient(configuration) as api_client:
        # create an inbox
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox = inbox_controller.create_inbox()

        print(inbox.email_address)

        return inbox


def get_email(inboxID):
    with mailslurp_client.ApiClient(configuration) as api_client:
        wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
        email = wait_for_controller.wait_for_latest_email(
            inbox_id=inboxID, timeout=60_000, unread_only=True
        )

        res_text = email.text_excerpt
        print(res_text)
        m = re.search("[0-9]+", res_text)
        print("otp " + res_text[m.start() : m.end()])

        return res_text[m.start() : m.end()]


def delete_inbox(inboxID):
    with mailslurp_client.ApiClient(configuration) as api_client:
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox_controller.delete_inbox(inbox_id=inboxID)
        print(f"** Inbox {inboxID} deleted!")


# random_inbox = create_random_email()
# get_email(random_inbox.id)