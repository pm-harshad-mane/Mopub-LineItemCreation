import json
import subprocess
import re

linItemNamePrefix = "Line Item Name " # here you need to put line item name prefix, line items will be generated as "Line Item Name ( 0.05 )" for bid value 0.05
firstLineItemBidRate = 0.05 # here you have to mention the bid rate of the last line-item created on UI
bidBucketOf = 0.05 # here you need to mention the bucket value in increment of which you want next line item to be created
maxBidRate = 0.20 # here you need to mention the max value of bid rate of which you want to create a line item; if you mention 5.00 then line item of bid rate 5.00 will be created
fileName = "line-item-creation-call.txt" # name or path of the text file in which you have copied the Curl call of the line item which we need to refer; make sure it is created recently to have a valid csrf token

# copying teh curlCall from the given file; if invalid file name is provided then code will stop after throwing errors
f = open(fileName, "r")
curlCall = f.read()
f.close()

postData = re.findall("(--data-binary '(.*?)')", curlCall)
if postData and postData[0] and postData[0][1]:
	postDataJson = json.loads(postData[0][1])
	# initializing value for new bid rate
	currentBidRate = firstLineItemBidRate
	linItemName = linItemNamePrefix
	# checking if new value is less than max bid rate allowed
	while currentBidRate < maxBidRate:
		print("")
		# updating next bid rate value
		currentBidRate = currentBidRate + bidBucketOf
		print("Executing the MoPub API to create new line item with Bid Rate: %.2f" % (currentBidRate))
		postDataJson['bid'] = currentBidRate # TODO: how to make sure that this number is always only upto 2 decimal; is it really needed to be 2 decimal?
		postDataJson['name'] = linItemName + (" ( %.2f )" % (currentBidRate)) # changing line item name
		postDataJson['keywords'][0] = ("pwbst:1 AND pwtecp:%.2f" % (currentBidRate)) # setting line item keywords
		# creating a copy of given curl call with new bid rate value
		newCurlCall = re.sub(r'--data-binary \'.*?\'', '--data-binary \'%s\'' % (json.dumps(postDataJson)), curlCall)		
		# execute curl call
		output = subprocess.Popen(newCurlCall, shell=True, stdout=subprocess.PIPE).stdout.read()
		print(output)
		outputJson = json.loads(output)
		# check response; if not success; inform and break the loop
		if outputJson['status'] == "error":
			print("Something went wrong, stopping the line-item-creation process, you may need to copy new csrf token from browser and restart process with firstLineItemBidRate set to %.2f ." % (currentBidRate - bidBucketOf))
			break
		else:
			print("Line item created successfuly.")	
else:
	print("Curl Call string is not as expected")

	
