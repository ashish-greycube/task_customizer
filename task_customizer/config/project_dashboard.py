from __future__ import unicode_literals
from frappe import _

def get_data(data):
	data['non_standard_fieldnames']={'Request for Quotation': 'project_name'}
	transactions=data['transactions']
	transactions[3].update({'label': _('Reference'),
				'items': ['Request for Quotation','Purchase Order', 'Purchase Receipt', 'Purchase Invoice']})
	data['transactions']=transactions

	return data
