from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.utils import get_link_to_form

def create_todo_based_on_repair_stage(self,method):
	msg=''
	if method=='on_submit':
		if self.repair_status:
			repair_status_doc=frappe.get_doc('Repair Status Offerte', self.repair_status)
			for task in repair_status_doc.repair_order_stage_task:
				todo = frappe.new_doc('ToDo')
				todo.owner=frappe.session.user
				todo.description=_('Task {0} is created for {1}  repair order in {2} stage '.format(task.task,self.name,self.repair_status))
				todo.reference_type='Quotation'
				todo.reference_name=self.name
				todo.repair_status_offerte_cf=self.repair_status
				todo.save(ignore_permissions=True)
				msg += _('To Do {} is created'.format(get_link_to_form('ToDo',todo.name)))
			if msg:
				frappe.msgprint(msg, alert=1)				

	elif method=='before_update_after_submit':
		old_repair_status = frappe.db.get_value('Quotation', self.name, 'repair_status')
		if self.repair_status!=old_repair_status:
			repair_status_doc=frappe.get_doc('Repair Status Offerte', self.repair_status)
			for task in repair_status_doc.repair_order_stage_task:
				todo = frappe.new_doc('ToDo')
				todo.owner=frappe.session.user
				todo.description=_('Task {0} is created for {1}  repair order in {2} stage '.format(task.task,self.name,self.repair_status))
				todo.reference_type='Quotation'
				todo.reference_name=self.name
				todo.repair_status_offerte_cf=self.repair_status
				todo.save(ignore_permissions=True)			
				msg += _('To Do {} is created'.format(get_link_to_form('ToDo',todo.name)))
			if msg:
				frappe.msgprint(msg, alert=1)