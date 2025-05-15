from getmac import get_mac_address
import frappe

@frappe.whitelist()
def get_mac(self, ip_address):
    mac = get_mac_address(ip=ip_address)
    if mac:
        return mac
    else:
        return None

        