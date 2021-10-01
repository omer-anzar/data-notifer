#############################
Data-notifer By Omer Anzar
#############################

Links format
always start from single quotation and end with it too.
If links has date syntax inside it that changes daily then u have to uses these

#############################
Date
30.09.2021 	: {:%d.%m.%Y}	.format(getDate())	
30092021 	: {:%d%m%Y}	.format(getDate())
30-Sep-2021	: {:%d-%b-%Y}	.format(getDate())
2021 		: {:%Y}		.format(getDate())

three letter name month
Sep		: {:%b}		.format(getDate())

Full name month
September	: {:%B}		.format(getDate())

4 letter name month
Sept 		: {}		.format(month)
Decem 		: {}		.format(month)
#############################

IF link is like this for e.g.

https://mufap.com.pk/pdf/PKFRVs/2021/Sept/PKFRV30092021.csv

so you have to wirte like this
..................................................................................................
'https://mufap.com.pk/pdf/PKFRVs/{:%Y}/month/PKFRV{:%d%m%Y}.csv'.format(getDate(),month,getDate())
..................................................................................................
Explanation:
	1st value of format which is getDate goes to the first curly bracket
	2nd value of pass in format which is month goes to the 2nd curly bracket in the link
	similary third value pass to the third curly bracket respectively.

Note:-link should always be in single quotation and inside links.txt
and the name of the file in names.txt should be w.r.t to its link's row
#############################