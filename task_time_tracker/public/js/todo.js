frappe.ui.form.on("ToDo", {
	validate: function(frm) {
		if (frm.doc.task_start__date_time_cf && frm.doc.task_end__date_time_cf) {
			if (frm.doc.task_end__date_time_cf <= frm.doc.task_start__date_time_cf) {
				frappe.throw(__('End Time should be greater than Start time'))
				
			}
			
		}
	},
	refresh: function(frm) {
		if(frm.is_new()==undefined) {
			frm.add_custom_button(__('Start'), function() {
				frm.set_value('task_start__date_time_cf', frappe.datetime.now_datetime())
				frm.set_value('status', 'Started')
				frm.save()

			},__('Timer'));
			frm.add_custom_button(__('Stop'), function() {
				frm.set_value('task_end__date_time_cf', frappe.datetime.now_datetime())
				frm.set_value('status', 'Closed')
				frm.save()
			},__('Timer'));		
			$('[data-label="Timer"] > button').removeClass(' btn-default')
			$('[data-label="Timer"] > button').addClass('btn-warning')
		}
	}
});