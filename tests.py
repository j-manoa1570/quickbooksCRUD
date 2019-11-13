import testcall
import testData

# This string is to query a customer. Quickbooks uses a SQL database to store everything so at some point you
# will need to add some functions in for building SQL statements 
testcall.qbGET("/v3/company/4620816365019203260/query?query=select * from Customer Where Metadata.LastUpdatedTime > '2015-03-01'&minorversion=41", "1")

# This will find a customer according to their ID. You might have to use The previous request and this request 
# together depending on what you are trying to do. You could also implement a local database that gets updated
# with data from QuickBooks
testcall.qbGET("/v3/company/4620816365019203260/customer/1?minorversion=41", "2")

# More SQL but this one is for Employees
testcall.qbGET("/v3/company/4620816365019203260/query?query=select * from Employee where DisplayName = 'Emily Platt'&minorversion=41", "3")

# Checks for bundle
testcall.qbGET("/v3/company/4620816365019203260/query?query=select * from Item where Type='Group'&minorversion=4", "4")

# Checks for a Category
testcall.qbGET("/v3/company/4620816365019203260/query?query=select * from Item where Type='Category'&minorversion=4", "5")

# Checks for items
testcall.qbGET("/v3/company/4620816365019203260/query?query=select * from Item maxresults 2&minorversion=41", "6")

# Creates a new customer
testcall.qbPOST("/v3/company/4620816365019203260/customer?minorversion=41", "1", testData.body1)

# Creates a new employee
testcall.qbPOST("/v3/company/4620816365019203260/employee?minorversion=41", "2", testData.body2)

# Create a new item
testcall.qbPOST("/v3/company/4620816365019203260/item?minorversion=41", "3", testData.body3)