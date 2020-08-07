frappe.ui.form.on("Purchase Order", {
	setup: function(frm) {
		frm.set_query("task_cf", "items", function(doc,cdt,cdn) {
            const row = locals[cdt][cdn];
			return {
				filters: {
					"project": row.project,
				}
			}
        });
    }
});