from __future__ import unicode_literals

import json

import frappe
from frappe import _, throw
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_purchase_order_from_task(source_name, target_doc=None, ignore_permissions=False,test_arg=None):
	def set_missing_values(source, target):
		target.append("items", {
			"project": source.project,
			"task_cf": source.name
		})
	doclist = get_mapped_doc("Task", source_name, {
			"Task": {
				"doctype": "Purchase Order"
			}
		}, target_doc, postprocess=set_missing_values, ignore_permissions=ignore_permissions)

	return doclist

@frappe.whitelist()
def make_purchase_receipt_from_task(source_name, target_doc=None, ignore_permissions=False,test_arg=None):
	def set_missing_values(source, target):
		target.append("items", {
			"project": source.project,
			"task_cf": source.name
		})
	doclist = get_mapped_doc("Task", source_name, {
			"Task": {
				"doctype": 'Purchase Receipt'
			}
		}, target_doc, postprocess=set_missing_values, ignore_permissions=ignore_permissions)

	return doclist

@frappe.whitelist()
def make_purchase_invoice_from_task(source_name, target_doc=None, ignore_permissions=False,test_arg=None):
	def set_missing_values(source, target):
		target.append("items", {
			"project": source.project,
			"task_cf": source.name
		})
	doclist = get_mapped_doc("Task", source_name, {
			"Task": {
				"doctype": 'Purchase Invoice'
			}
		}, target_doc, postprocess=set_missing_values, ignore_permissions=ignore_permissions)

	return doclist

@frappe.whitelist()
def make_rfq_from_task(source_name, target_doc=None, ignore_permissions=False,test_arg=None):
	def set_missing_values(source, target):
		target.append("items", {
			"project_name": source.project,
			"task_cf": source.name
		})
	doclist = get_mapped_doc("Task", source_name, {
			"Task": {
				"doctype": 'Request for Quotation'
			}
		}, target_doc, postprocess=set_missing_values, ignore_permissions=ignore_permissions)

	return doclist            

@frappe.whitelist()
def make_rfq_from_project(source_name, target_doc=None, ignore_permissions=False,test_arg=None):
	def set_missing_values(source, target):
		target.append("items", {
			"project_name": source.name,
			# "task_cf": source.name
		})
	doclist = get_mapped_doc("Project", source_name, {
			"Project": {
				"doctype": 'Request for Quotation'
			}
		}, target_doc, postprocess=set_missing_values, ignore_permissions=ignore_permissions)

	return doclist      