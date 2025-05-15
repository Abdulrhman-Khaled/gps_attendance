from gps_attendance.utils import valid_distance_to_gps
import frappe
from erpnext.hr.doctype.employee_checkin.employee_checkin import EmployeeCheckin
from frappe import _



class GPSEmployeeCheckin(EmployeeCheckin):
    def validate(self):
        super(GPSEmployeeCheckin , self) .validate()
        self.validate_employee_location()
    
    def validate_employee_location(self):
        if not ( self.latitude or self.longitude) :
            frappe.throw(_("Invalid Employee Checkin Location"))
        
        
        self.branch = self.branch or frappe.db.get_value("Employee" , self.employee , "branch")
        if not self.branch :
            frappe.throw(_("Please Set Branch for Employee {}").format(self.employee))
        
        branch = frappe.get_doc("Branch" , self.branch)
        if not ( branch.latitude or branch.longitude) :
            frappe.throw(_("Invalid Branch Location"))
        
        branch_origin = ( branch.latitude , branch.longitude)
        user_origin = ( self.latitude , self.longitude)
        allowed_distance = branch.allowed_distance
        
        self.distance = valid_distance_to_gps(branch_origin,user_origin , allowed_distance)

        if self.distance < 0 :
            frappe.throw(_("alloed distance only from origin is {} not {}").format(allowed_distance , self.distance))

        