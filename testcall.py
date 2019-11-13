# This is the library that makes sending requests possible. This can be installed using the command:
# pip install requests 
# pipenv install requests
# pip3 install requests
#
# Depending on what python package manager you use.
import requests

# This is all that is needed to make the actual get request to QuickBooks. It is quite simple actually.
# I kind of like it. The Authorization header is generated from the token. In a real setting, the application
# would have a login screen so only specific users can access/ different users have different access
# rights. Those accounts would be connected to a database of some sort that would have the authorization 
# token that the user needs. In this example, I generated the authorization token following the Postman 
# instructions, made the request that returned 200, wrote a little bit of python to make a request function
# with all of the header parameters that were needed, requested again to make sure it worked, and then cut
# out header parameters that I didn't recognize/thought it actually needed until I came to this short call.
#
# Passes a single parameter for the endpoint that I desired. For a real application, you would probably want
# to pass at least the endpoint and authorization but I hardcoded my authorization. Builds the complete URL
# endpoint, creates the header, assigns the returned request to a variable, and prints the body of the returned
# request.
#
# UPDATE: I added a second parameter that simply was a test value number so I wouldn't have to print out 
# an actual response, I could just check for status code and output if the test was successful or not.
def qbGET(endpoint, currentTest):
    getRequest = "https://sandbox-quickbooks.api.intuit.com" + endpoint
    header = {
        "Authorization" : "Bearer eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..GinpIY4JE6jwilPnMXGb8Q.QaMZrZ_weNjqg21svTfDVChDnynJqSsjmX4-aSc7KArzQ_W5MCxrx0x93NcQeVXjcVUgO7qXEC7SycCkm-xlRDkLPe0bZOSz0GCDaWIbFgsb03ixt0U5Nq8gNQXwgDUsaD--bRxgq5AzcFI318UwypaOA2A7N8Is1T3mfTnMqb2XJUwJoc2-zUuB4I0qYRSaGeGmNW5SlIciTl4rFlIFB3u3JSj_mYiVYKgcRjGhgOCUGKL-EeqSPVqKFAp_IVdl-_WCsLAgo2eE9bgLH1l5RWsI6wha7Guz2MxLgvgvgtg7Ix0VhVTgkAdSVVcpO4fF1xpeBQSDFTynReSnJgo-gc2cgCBf6x931fpL4mvbUSmr9Ue1UxHeVABGKzZCMxjFI-NnSs6TOUdzUvDFsDDfa8LVC9SvbVnF25dEchVB1w2A-jOAtVdZYgzTnbIqZHmZ0QrTX54I6yJl62_uWRa6UZDFl3DytpHC-bbAgsvyYdTC0C5E4FZd8XZYAlsHH0NzrkWB4kDnigTIQ7s3Y3RVweRj8pDei7qGnmRiunoszt0wybAAdSjeRRZ1rWa08NIHHSvf4WyRqPElFgsWv5mq4giR1Q5Yimx9XapZ4U_StP1V7QT3NH6nLNBKYLyWbNlbFCIXlPgKWHv6ZO2IoiiN62SNaDajpwU1IqLlgZFaMN4V91KjCFeXtfcOz6lv1TkLqQx7yyCEF-PZFRDRzDDB6O8NWMUqYP8R9Sw00GU9Z6X9335poQ3zAO4zEmhy_Q0RO1mmP7woxI7EHQJbnIz7uRqDkJIYdeMGbBk9fXlIC-EffyQw_mhfJjEKffQY9GwPYle8V9-NB1HtH-lyIgL2Hxn5zdTI0XcHobpwFlsCTWM.YVbbr-2BfEB_vEWZMPvYCg"
    }
    
    # Get takes 2 parameters: url and headers. Both must be present even if it is simply ""
    dataReceived = requests.get(url = getRequest, headers = header)

    # The content from QuickBooks is in XML. You will want to include some sort of parsing library since
    # XML is gross like a bad prostitute.
    # print(dataReceived.content)

    # Prints if the request was successful or not
    if dataReceived.status_code == 200:
        print("Get test " + currentTest + " was successful!")
    else:
        print("Get test " + currentTest + " was unsuccessful with response code: " + str(dataReceived.status_code) + "...")


# Three parameters this time. POST requests need body data otherwise this request is nearly identical
# to using a GET with the exception of using a different keyword (POST instead of GET)
def qbPOST(endpoint, currentTest, bodyData):
    postRequest = "https://sandbox-quickbooks.api.intuit.com" + endpoint
    header = {
        "Content type" : "application/json",
        "Authorization" : "Bearer eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..GinpIY4JE6jwilPnMXGb8Q.QaMZrZ_weNjqg21svTfDVChDnynJqSsjmX4-aSc7KArzQ_W5MCxrx0x93NcQeVXjcVUgO7qXEC7SycCkm-xlRDkLPe0bZOSz0GCDaWIbFgsb03ixt0U5Nq8gNQXwgDUsaD--bRxgq5AzcFI318UwypaOA2A7N8Is1T3mfTnMqb2XJUwJoc2-zUuB4I0qYRSaGeGmNW5SlIciTl4rFlIFB3u3JSj_mYiVYKgcRjGhgOCUGKL-EeqSPVqKFAp_IVdl-_WCsLAgo2eE9bgLH1l5RWsI6wha7Guz2MxLgvgvgtg7Ix0VhVTgkAdSVVcpO4fF1xpeBQSDFTynReSnJgo-gc2cgCBf6x931fpL4mvbUSmr9Ue1UxHeVABGKzZCMxjFI-NnSs6TOUdzUvDFsDDfa8LVC9SvbVnF25dEchVB1w2A-jOAtVdZYgzTnbIqZHmZ0QrTX54I6yJl62_uWRa6UZDFl3DytpHC-bbAgsvyYdTC0C5E4FZd8XZYAlsHH0NzrkWB4kDnigTIQ7s3Y3RVweRj8pDei7qGnmRiunoszt0wybAAdSjeRRZ1rWa08NIHHSvf4WyRqPElFgsWv5mq4giR1Q5Yimx9XapZ4U_StP1V7QT3NH6nLNBKYLyWbNlbFCIXlPgKWHv6ZO2IoiiN62SNaDajpwU1IqLlgZFaMN4V91KjCFeXtfcOz6lv1TkLqQx7yyCEF-PZFRDRzDDB6O8NWMUqYP8R9Sw00GU9Z6X9335poQ3zAO4zEmhy_Q0RO1mmP7woxI7EHQJbnIz7uRqDkJIYdeMGbBk9fXlIC-EffyQw_mhfJjEKffQY9GwPYle8V9-NB1HtH-lyIgL2Hxn5zdTI0XcHobpwFlsCTWM.YVbbr-2BfEB_vEWZMPvYCg"
    }

    # Unlike a GET request, POST requests require 3 parameters: url endpoint, headers, and body data.
    # Body data is needed because POST requests are typically used for creating data and the endpoint
    # needs to know what to create in the DB.
    dataReceived = requests.post(url = postRequest, headers = header, data = bodyData)

    # The content from QuickBooks is in XML. You will want to include some sort of parsing library since
    # XML is gross like a bad prostitute.
    # print(dataReceived.content)

    # Prints if the request was successful or not
    if dataReceived.status_code == 200:
        print("Post test " + currentTest + " was successful!")
    else:
        print("Post test " + currentTest + " was unsuccessful with response code: " + str(dataReceived.status_code) + "...")
        print("Returned body: " + str(dataReceived.content))

