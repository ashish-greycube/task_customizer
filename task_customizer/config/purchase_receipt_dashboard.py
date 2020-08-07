from __future__ import unicode_literals
from frappe import _

def get_data(data):
	internal_links=data['internal_links']
	internal_links['Task']=['items', 'task_cf']
	data['internal_links']=internal_links 

	transactions=data['transactions']
	transactions[1].update({'label': _('Reference'),
				'items': ['Purchase Order', 'Quality Inspection', 'Project','Task']})
	data['transactions']=transactions

	return data
