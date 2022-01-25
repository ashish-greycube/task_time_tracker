frappe.ui.form.on("ToDo", {
	refresh: function(frm) {
		if(frm.doc.reference_type=='Quotation' && frm.doc.reference_name && frm.doc.repair_status_offerte_cf) {
			frm.add_custom_button(__('Start'), function() {
				frm.set_value('task_start__date_time_cf', frappe.datetime.now_datetime())
			},__('Time'));
			frm.add_custom_button(__('Stop'), function() {
				frm.set_value('task_end__date_time_cf', frappe.datetime.now_datetime())
			},__('Time'));			
		}
	}
});