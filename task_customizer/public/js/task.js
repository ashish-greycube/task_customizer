frappe.ui.form.on("Task", {
	setup: function (frm) {
		frm.make_methods = {
			'Timesheet': () => frappe.model.open_mapped_doc({
				method: 'erpnext.projects.doctype.task.task.make_timesheet',
				frm: frm
			}),            
			'Purchase Order': () => frappe.model.open_mapped_doc({
                method: 'task_customizer.make_dashboard.make_purchase_order_from_task',
                frm: frm
            }),
			'Purchase Receipt': () => frappe.model.open_mapped_doc({
                method: 'task_customizer.make_dashboard.make_purchase_receipt_from_task',
                frm: frm
            }),
			'Purchase Invoice': () => frappe.model.open_mapped_doc({
                method: 'task_customizer.make_dashboard.make_purchase_invoice_from_task',
                frm: frm
            }),
			'Request for Quotation': () => frappe.model.open_mapped_doc({
                method: 'task_customizer.make_dashboard.make_rfq_from_task',
                frm: frm
            })                                                
		}
    }
});
