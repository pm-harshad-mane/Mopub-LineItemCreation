# Problem: How to create multiple line items in MoPub UI quickly?

1. Login to MoPub UI
2. Create a new application
3. Create new ad-units associated to the new application
4. Create new order
5. Now under this new order we have to create multiple line items, say 100 line items each with Rate of increments of $0.05. First with rate $0.05 , second with rate $0.10, third with $0.15 and so on.

# Assumption
Here we are assuming that we have to create multiple line items with same configuration and only chnage is the Rate value

# Solution
1. Now we have to create the first line item in the sequence
2. Open the developer toolbar of the Chrome browser
3. Fill up the three step form of line item creation, enter priority, budget, **enter the Rate as 0.05**, daypart targeting, frequency caps, select ad-units, setup geo targetings, connectivity, device and OS targetings, user targetings, keyword targetings.
4. Now before clicking the Save button, clear the Network pannel of developer toolbar.
5. Now click the Save button.
6. If your action was successful then you will see many calls executing in the network panel.
7. Find the call in network panel "https://app.mopub.com/web-client/api/line-items/create"
8. Right-click on this call in Network panel, select option *Copy* *->* *Copy as cURL*.
9. Paste the copied content in a new text file on your computer, say *line-item-creation-call.txt*.
10. The "line-item-creation-call.txt" will look as following. This is the API call made to create your first Line Item. If you execute this curl command with all given parameters then it will crteate a new Line Item in MoPub UI with exactly same properties. Now we just have to execute the following CURL command on Terminal by changing the Rate field as required.

```
curl 'https://app.mopub.com/web-client/api/line-items/create' -H 'origin: https://app.mopub.com' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' -H 'x-csrftoken: qSpAW9s6MP9bn4kb2cF0sr1ic6EFM81jj7AXobAIjJ1vmKN8au5flLbmqV1hJasy' -H 'content-type: application/json' -H 'accept: */*' -H 'referer: https://app.mopub.com/new-line-item?orderKey=28f5037d7ed74c8b85f1aea55a3900b7' -H 'authority: app.mopub.com' -H 'cookie: mp__mixpanel=%7B%22distinct_id%22%3A%20%221695a1d38e7360-0225d094509571-36667905-1aeaa0-1695a1d38e8412%22%2C%22%24device_id%22%3A%20%221695a1d38e7360-0225d094509571-36667905-1aeaa0-1695a1d38e8412%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Freports%2Fcustom%2F%22%2C%22%24initial_referring_domain%22%3A%20%22app.mopub.com%22%7D; csrftoken=qSpAW9s6MP9bn4kb2cF0sr1ic6EFM81jj7AXobAIjJ1vmKN8au5flLbmqV1hJasy; sessionid=ewjhuret4eruw2vqp4wb6jn952ese33y; mp_c99579c4804fba6b8aeed7a911581652_mixpanel=%7B%22distinct_id%22%3A%20%22b4a2ccec80294e9983b350b9f7913578%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Fnew-line-item%3ForderKey%3D28f5037d7ed74c8b85f1aea55a3900b7%22%2C%22%24initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22member%22%2C%22accountKey%22%3A%20%221e8bbcf1b05649c98b773a742a7791cd%22%7D; mp_mixpanel__c=0' --data-binary '{"adUnitKeys":["9656e24ec144478ba22f8251fa7326fe"],"allocationPercentage":100,"bid":0.05,"budgetStrategy":"allatonce","budget":null,"budgetType":"unlimited","bidStrategy":"cpm","deviceTargeting":false,"dayPartTargeting":"alltime","end":null,"frequencyCapsEnabled":false,"includeConnectivityTargeting":"all","includeGeoTargeting":"all","keywords":["a = 1 AND b=1"],"name":"test 12","orderKey":"28f5037d7ed74c8b85f1aea55a3900b7","priority":12,"refreshInterval":0,"start":"2019-03-08T08:00:00.000Z","type":"network","targetAndroid":false,"minAndroidVersion":"1.5","maxAndroidVersion":"999","minIosVersion":"2.0","maxIosVersion":"999","targetIOS":"unchecked","targetIphone":false,"targetIpad":false,"targetIpod":false,"userAppsTargeting":"include","userAppsTargetingList":[],"enablePrivateKeywords":true,"networkType":"custom_native","disallowAutoCpm":false,"enableOverrides":true,"overrideFields":{"custom_event_class_name":"a.c.c","custom_event_class_data":"a.c.b.c"}}' --compressed
```

# python script
So here is a simple python script that will read the given *line-item-creation-call.txt* file and executes it multiple times till it has created line items of given Max Rate (mentioned in python code).
You will need to update following variables as needed
```
firstLineItemBidRate = 0.05 # here you have to mention the bid rate of the last line-item created on UI
bidBucketOf = 0.05 # here you need to mention the bucket value in increment of which you want next line item to be created
maxBidRate = 0.10 # here you need to mention the max value of bid rate of which you want to create a line item; if you mention 5.00 then line item of bid rate 5.00 will be created
fileName = "a.txt" # name or path of the text file in which you have copied the Curl call of the line item which we need to refer; make sure it is created recently to have a valid csrf token

````

