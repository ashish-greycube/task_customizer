from __future__ import unicode_literals
from frappe import _

def get_data(data):
	transactions=data['transactions']
	transactions.append(
			{
				'label': _('Purchase'),
				'items': ['Purchase Order']
			})
	data['transactions']=transactions 
	return data
