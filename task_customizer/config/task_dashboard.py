from __future__ import unicode_literals
from frappe import _

def get_data(data):
	data['non_standard_fieldnames']={'Purchase Order': 'task_cf','Purchase Receipt': 'task_cf','Purchase Invoice': 'task_cf'}

	transactions=data['transactions']
	transactions.append(
			{
				'label': _('Purchase'),
				'items': ['Purchase Order','Purchase Receipt','Purchase Invoice']
			}
            )
	data['transactions']=transactions 
	return data
