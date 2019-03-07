# Problem: How to create multiple line items in MoPub UI quickly?

1. Login to MoPub UI
2. Create a new application
3. Create new ad-units associated to the new application
4. Create new order
5. Now under this new order we have to create multiple line items, say 100 line items each with Rate of increments of $0.05. First with rate $0.05 , second with rate $0.10, third with $0.15 and so on.

# Assumption
Here we are assuming that we have to create 100 line items with same configuration and only chnage is the Rate value

# Solution
1. Now we have to create the first line item in the sequence
2. Open the developer toolbar of the Chrome browser
3. Fill up the three step form of line item creation, enter priority, budget, **enter the Rate as 0.05**, daypart targeting, frequency caps, select ad-units, setup geo targetings, connectivity, device and OS targetings, user targetings, keyword targetings.
4. Now before clicking the Save button, clear the Network pannel of developer toolbar.
5. Now click the Save button.
6. If your action was successful then you will see many calls executing in the network panel.
7. Find the call in network panel "https://app.mopub.com/web-client/api/line-items/create"
8. Right-click on this call in Network panel, select option "Copy" -> "Copy as cURL".
9. Paste the copied content in a new text file on your computer, say "line-item-creation-call.txt".
10. The "line-item-creation-call.txt" will look as following. This is the API call made to create your first Line Item. If you execute this curl command with all given parameters then it will crteate a new Line Item in MoPub UI with exactly same properties. Now we just have to execute the following CURL command on Terminal by changing the Rate field as required.

```
code
```

# python script
So here is a simple python script that will read the given "line-item-creation-call.txt" file and executes it multiple times till it has created line items of given Max Rate (mentioned in python code).


