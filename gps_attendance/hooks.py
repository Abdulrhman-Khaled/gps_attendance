from . import __version__ as app_version

app_name = "gps_attendance"
app_title = "GPS Attendance"
app_publisher = "Peter Maged"
app_description = "GPS Attendance"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "eng.peter.maged@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gps_attendance/css/gps_attendance.css"
# app_include_js = "/assets/gps_attendance/js/gps_attendance.js"

# include js, css files in header of web template
# web_include_css = "/assets/gps_attendance/css/gps_attendance.css"
# web_include_js = "/assets/gps_attendance/js/gps_attendance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gps_attendance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Employee Checkin" : "overrides/employee_checkin/employee_checkin.js",
    "Branch" : "overrides/branch/branch.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gps_attendance.install.before_install"
# after_install = "gps_attendance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gps_attendance.uninstall.before_uninstall"
# after_uninstall = "gps_attendance.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gps_attendance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Employee Checkin": "gps_attendance.overrides.employee_checkin.employee_checkin.GPSEmployeeCheckin"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gps_attendance.tasks.all"
#	],
#	"daily": [
#		"gps_attendance.tasks.daily"
#	],
#	"hourly": [
#		"gps_attendance.tasks.hourly"
#	],
#	"weekly": [
#		"gps_attendance.tasks.weekly"
#	]
#	"monthly": [
#		"gps_attendance.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "gps_attendance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gps_attendance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gps_attendance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["gps_attendance.utils.before_request"]
# after_request = ["gps_attendance.utils.after_request"]

# Job Events
# ----------
# before_job = ["gps_attendance.utils.before_job"]
# after_job = ["gps_attendance.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gps_attendance.auth.validate"
# ]

