import webbrowser

def open_whatsapp_chat(contact_name):
    base_url = "https://web.whatsapp.com/https://web.whatsapp.com/
    phone_number = "9588204685"  # Replace with the phone number of the contact

    # Remove any non-digit characters from the phone number
    phone_number = "".join(filter(str.isdigit, phone_number))

    # Construct the URL with the phone number and contact name
    url = f"{base_url}+{phone_number}&text=Hi%20{contact_name},%20"

    # Open the URL in the default web browser
    webbrowser.open(url)

# Example usage
contact_name = "John Doe"
open_whatsapp_chat(contact_name)