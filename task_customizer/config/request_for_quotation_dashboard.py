from __future__ import unicode_literals
from frappe import _

def get_data(data):
	data['internal_links']={
		'Task': ['items', 'task_cf'],
		'Project':['items', 'project_name']
		}
	transactions=data['transactions']
	transactions.append({'label': _('Project Reference'),
				'items': ['Project','Task']})
	data['transactions']=transactions
	return data
