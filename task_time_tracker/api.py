from __future__ import unicode_literals
from pickle import FALSE, TRUE
import frappe
from frappe import throw, _
from frappe.utils import get_link_to_form,time_diff_in_seconds,get_url_to_form


def calculate_creation_time_spent_on_quotation(self,method):
	if self.quotation_creation_start__time_cf:
		time_spent_on_quotation_creation_cf=time_diff_in_seconds(self.creation,self.quotation_creation_start__time_cf)
		print('time_spent_on_quotation_creation_cf'*10,time_spent_on_quotation_creation_cf)
		frappe.db.set_value('Quotation', self.name, 'time_spent_on_quotation_creation_cf',time_spent_on_quotation_creation_cf)

def create_todo_based_on_repair_stage(self,method):
	msg=''
	if method=='on_update':
		if self.repair_status:
			repair_status_doc=frappe.get_doc('Repair Status Offerte', self.repair_status)
			first_todo=False
			for task in repair_status_doc.repair_order_stage_task:
				description=_('Task {0} is created for {1}  repair order in {2} stage '.format(task.task,self.name,self.repair_status))
				if not frappe.db.exists({'doctype': 'ToDo','description': description}):
					todo = frappe.new_doc('ToDo')
					todo.owner=frappe.session.user
					todo.description=description
					todo.reference_type='Quotation'
					todo.reference_name=self.name
					todo.repair_status_offerte_cf=self.repair_status
					todo.save(ignore_permissions=True)
					msg += _('To Do {} is created <br>'.format(get_link_to_form('ToDo',todo.name)))
					if first_todo==False:
						first_todo_name=todo.name
						first_do_desc=description
						first_todo=True
			if first_todo==True:
				frappe.msgprint(get_link_to_form("ToDO",first_todo_name,label=first_do_desc))
			if msg:
				frappe.msgprint(msg, alert=1)				
				# frappe.local.response["type"] = "redirect"
				# frappe.local.response["location"] = get_url_to_form("ToDO",first_todo_name)				

	# elif method=='before_update_after_submit':
	# 	old_repair_status = frappe.db.get_value('Quotation', self.name, 'repair_status')
	# 	if self.repair_status!=old_repair_status:
	# 		repair_status_doc=frappe.get_doc('Repair Status Offerte', self.repair_status)
	# 		for task in repair_status_doc.repair_order_stage_task:
	# 			todo = frappe.new_doc('ToDo')
	# 			todo.owner=frappe.session.user
	# 			todo.description=_('Task {0} is created for {1}  repair order in {2} stage '.format(task.task,self.name,self.repair_status))
	# 			todo.reference_type='Quotation'
	# 			todo.reference_name=self.name
	# 			todo.repair_status_offerte_cf=self.repair_status
	# 			todo.save(ignore_permissions=True)			
	# 			msg += _('To Do {} is created <br>'.format(get_link_to_form('ToDo',todo.name)))
	# 		if msg:
	# 			frappe.msgprint(msg, alert=1)