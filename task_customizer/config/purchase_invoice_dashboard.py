from __future__ import unicode_literals
from frappe import _

def get_data(data):
	internal_links=data['internal_links']
	internal_links['Task']=['items', 'task_cf']
	internal_links['Project']=['items', 'project']
	data['internal_links']=internal_links 

	transactions=data['transactions']
	transactions.append({'label': _('Project Reference'),
				'items': ['Project','Task']})
	data['transactions']=transactions

	return data
