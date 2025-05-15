from getmac import get_mac_address
import frappe

@frappe.whitelist()
def get_mac():
    mac = get_mac_address()
    if mac:
        return mac
    else:
        return None

        