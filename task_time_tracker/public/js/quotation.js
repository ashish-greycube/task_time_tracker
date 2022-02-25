frappe.ui.form.on('Quotation', {
	setup: function(frm) {
        if (frm.is_new()==1) {
            frm.doc.quotation_creation_start__time_cf=frappe.datetime.now_datetime();
        }
    }
})