<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

### 3.8 API Call
Overview

Screenshot 199: API Call node view

The API Call node integrates external systems via APIs, enabling Processes to retrieve or send data to various platforms, including social media (e.g., LinkedIn, Facebook), banking services (e.g., Visa, Mastercard), and general web services. The node supports both dynamic and static parameter configurations.


Diagram 12: API Call node flow.

All API calls are made from the following IP addresses (effective 11th November 2025, 00:00 UTC):

54.171.15.37/32

108.128.68.222/32

63.33.226.230/32

If you encounter access errors when calling external systems or databases, please make sure these addresses are whitelisted in your firewall or network settings.

Note:

The old IP addresses (54.154.124.100 and 54.154.124.224) will be deactivated after the transition date but should remain on your allowlist until further notice, as they may be temporarily reused in case of a rollback. You will be informed separately once they are permanently decommissioned.

You can use the API Call for weather data retrieval, payment verification, customer feedback analysis and other cases. Utilizing Header Parameters (see Node Settings) allows you to use the node in the following cases:

Authentication

Sending API keys or tokens (e.g., Authorization: Bearer <token>).

Basic authentication credentials.

Custom authentication headers required by specific APIs.

Content Negotiation

Specifying accepted response formats (Accept: application/json).

Defining the request content type (Content-Type: application/json).

Character set specifications (charset=utf-8).

API Versioning

Specifying API versions (e.g., api-version: 2.0).

Indicating which version of the API you want to use.

Request Metadata

Tracking IDs for request tracing.

Client identification information.

Session tokens

Caching Controls

Cache-control directives.

ETag headers for resource versioning.

Last-modified information.

Security Headers

Cross-Origin Resource Sharing (CORS) headers.

Security tokens.

Custom security-related headers.

Language and Localization

Preferred language (Accept-Language).

Timezone information.

Regional preferences.

Custom Headers

API-specific custom parameters.

Platform-specific identifiers.

Application-specific metadata.

Node Settings

The API Call node has the following parameters:

Screenshot 200: API Call node basic settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

URL [Required] [Field] [String]: The endpoint for the API Call specified in one of the formats:

URL: for example, https://account.corezoid.com/api/1

Variable: for example, {{url}}.

Construction: for example {{conv[state diagram id].ref[ref].url}}

Request format [Required] [Action]: Selects the request format:

Default: Sets standard HTTP/HTTPS request format with a Key-Value editor for query parameters and a request method dropdown menu.

Corezoid: Same as the Default format, but with no request method selection.

Raw: A free-form request format that allows you to write custom request bodies. Use this format when an API follows a non-standard request format.


## 11. Request method [Required] [Action]: HTTP methods supported:
POST: Send data.

GET: Retrieve data.

PUT: Create or update existing data.

DELETE: Delete data.

HEAD: Similar to POST, but with no response body.

PATCH: Update only a part of the data.

Note: Some APIs have the same endpoint for different request methods.

12. Data format [Required] [Action]: Select the format for sending payload data:

JSON

XML

Form

13. Content-Type [Required] [Field] [String]: Indicates the format of the data sent in the request body. The field is filled out automatically based on the data format that you have selected. Default types based on the data format:

JSON: application/json; charset=utf-8.

XML: application/xml; charset=utf-8.

Form: application/x-www-form-urlencoded; charset=utf-8.

14. Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets.

15. Value [Required] [Field] [Any]: Specify the value you want to assign to the Key-named parameter. See data types descrition for more details.

16. Code editor [Optional] [Action]: Click Code editor to open the code editor tab, where:

Screenshot 201: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 202: Code editor full-screen view.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

17. Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.


## 18. Delete key-value [Optional] [Action]: Delete the key-value pair.

## 19. Add key-value [Optional] [Action]: Add a new key-value pair.
To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon on the right side of the key-value line.

Screenshot 203: Adding a key-value pair.

Other settings

Screenshot 204: API Call other parameters.

20. Header parameters  [Optional] [Action]: Select to specify header parameters for API requests providing additional information (authentication parameters, metadata, etc.). Use the same Key-Value format as in the Request Parameters.


## 21. Code editor [Optional] [Action]: Open the Code editor.
22. Add key-value [Optional] [Action]: Add a new key-value pair to the header parameters.

23. Customize response parameters  [Optional] [Action]: Select to modify the response header and body parameters and specify the response format before the task is released from the node. Use standard icons to add parameters' keys and values.

You can use this feature to work with APIs that provide an incorrect response format or do not specify a format. By customizing the response parameters, you can ensure that the response is parsed correctly.

Also, it can be used to minimize the amount of data added to a task. When an API request returns a lot of data, use Customize response parameters to extract only the needed data.

24. Response format  [Required] [Action]: Select the format for the response:
	* Default
	* Application/Json
	* Application/X-Www-Form-Urlencoded
	* Application/Xml
	* Text/Xml

25. Code editor [Optional] [Action]: Open the Code editor.

26. Header key [Required] [Field] [String]: The key preset to “header” to enable the processing of response header data from an external API and its inclusion in the task.
27. Header value [Required] [Field] [Any]: The key preset to “{{header}}” to enable the processing of response header data from an external API and its inclusion in the task.
28. Type of data [Required] [Action]: Selects the data type for the response header value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O) selected by default.

29. Delete key-value [Optional] [Action]: Delete the key-value pair.
30. Body key [Required] [Field] [String]: The key preset to “body” to enable the processing of response body data from an external API and its inclusion in the task.

31. Body value [Required] [Field] [Any]: The key preset to “{{body}}” to enable the processing of response body data from an external API and its inclusion in the task. 
32. Type of data [Required] [Action]: Selects the data type for the response body value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O) selected by default.
33. Delete key-value [Optional] [Action]: Delete the key-value pair.

34. Add key-value [Optional] [Action]: Add a new key-value pair to the header parameters.
35. Limit the number of simultaneous requests to the API [Required] [Action]: Limit the number of concurrent requests made to the API.
36. Number of simultaneous requests to the API [Required] [Field] [Number]: Specify the maximum number of concurrent requests made to the API. Set to 5 by default.

37. Add system parameters to the request [Optional] [Action]: Add Corezoid system parameters to an API request required to make the request to the Corezoid API. Parameters can be the following: conv_signature, conv_time, and conv_id. For more information, go to Corezoid API.
Warning (color): Some APIs have strict requirements for the parameters that can be included in a request. If this is the case for the API you are using, you may need to clear the checkbox to exclude Corezoid system parameters from your request.

38. Sign the request with the secret key [Optional] [Action]: Select to sign requests from the node with the secret key you can specify in the field that appears. You can use it to send requests to Corezoid API, which requires secret key authentication.
Note (color): To include the necessary system parameters along with the request, you have to select the Add system parameters to the request option.

39.  Secret key [Optional/Required if Sign the request with the secret key is selected] [Field] [String]: Specify the secret key.

40. Refresh the secret key [Optional] [Action]: Refresh the secret key.
41. RFC standard response [Optional] [Action]: Select to Process the response from an external API according to the RFC standard.
Note (color): When this option is selected, the response body is mandatory for response codes 200 and 201 and is optional for the 202 response code.

42. Include debug info [Optional] [Action]: Adds the API request extra information to the conveyor_api_debug task parameter that includes execution time, request body size, response code, and response body size.

"__conveyor_api_debug__": {

"http_exec_time": 328.552,

"http_req_body_size": 0,

"http_res_code": 200,

"http_res_body_size": 1132

}

Table 16: Conveyor debug parameters.

43. Sign the request by certificate  [Optional] [Action]: Select to add a certificate in the PEM format. Use this option for APIs that require a client certificate to be included in your request.
-----BEGIN RSA PRIVATE KEY-----

....your private key goes here....

-----END RSA PRIVATE KEY-----

-----BEGIN CERTIFICATE-----

....your certificate goes here....

-----END CERTIFICATE-----

44. Certificate input field [Optional/Required if Sign the request by certificate is selected] [Field] [String]: Input the certificate to sign the request with.

45. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

46. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

47. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

48. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded is selected] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

49. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Example Usage

There are innumerable ways in which companies choose to implement their APIs:

Using different data formats, including JSON and XML as the most popular ones

Applying certificates

Getting an API key or token

Generating an authentication code and periodically renewing their access token

Note: There are no commonly used examples that can cover all the possible features.

API call to OpenWeatherMap
OpenWeatherMap is a popular free API that you can use to check the weather at any location.
To check the weather in San Francisco:

Create a Process and add the API Call node.
Note: For more information, go to Create Process and Add node.

Go to OpenWeatherMap and get the needed API where:

https://api.openweathermap.org/data/2.5/weather is the endpoint URL.

lat, lon, and appid are parameters.

The appid parameter is a unique API key that you get by creating an account with the service.
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

In API request URL of the API Call node details panel:

In the URL field, enter the endpoint URL.

In the Request method dropdown list, select GET.

In Request parameters of the API Call node details panel, enter the lat, lon, and appid parameter values.

Screenshot 205: Enter parameter for the GET request method.

Switch to the View mode by clicking View on the upper panel.

In the New Task dialog that opens, click Add task.

Screenshot 206: Add the task.

On the task details form, you can see that it’s cloudy in San Francisco now.

Screenshot 207: Check the weather in San Francisco.

Best Practices

Secure API Keys: Use environment variables or secure storage for sensitive data like API keys or tokens.

Optimize Timeouts: Set appropriate timeout values to prevent blocking workflows unnecessarily.

Error Management: Implement robust error handling strategies, such as retries and failover mechanisms, for critical operations.

Logging and Monitoring: Ensure logs capture sufficient detail for diagnosing integration issues.

By effectively leveraging the API Call node, you can extend Corezoid Processes to interact seamlessly with external systems, enhancing automation and connectivity.

Error Handling and Troubleshooting

(current table under spoiler)

Table 17: Error parameter names.

*The error tag __conveyor_api_return_type_tag_ may have the following values.

Table 18: API Call errors.


### 3.9 Database Call
Overview

Screenshot 208: Database Call node view

The Database Call node lets you write and execute SQL queries directly within Corezoid, removing the need for writing custom APIs to access databases. With the Database Call node, managing and accessing data in your databases becomes straightforward and streamlined.
Supported database management systems (DBMS):

MySQL

Microsoft SQL Server

PostgreSQL

Oracle

MongoDB

To use the Database Call node, first, you need to connect your database to Corezoid.

Diagram 13: Database Call node flow.

All Database calls are made from the following IP addresses:

54.171.15.37/32

108.128.68.222/32

63.33.226.230/32

If you encounter access errors when calling databases, you might need to white-list these addresses.

Preparing to Work with the Database Call

Create a database you want to use with the Database Call.

Save your DB parameters to use when creating a connection in Corezoid:

Screenshot 209: DB parameters example for Add database call window.

In Corezoid, create a database connection by clicking Create-Database.

Screenshot 210: Create a database.

Fill in all required fields: specify all the required parameters, such as database name, users, passwords, etc. and select the database type in the drop-down list:

Screenshot 211: Add connection for the Database Call.

1. Connection Name [Required] [Field] [String]: Connection name.


## 2. Database type [Required] [Action]: Select database type:
Postgres

Oracle

MongoDB

MySQL

MSSQL


## 3. Host [Required] [Field] [String]: Database server address.
4. Port [Required] [Field] [String]: Connection port. Set to 5432 by default when PostgreSQL in the Database type field.


## 5. Database username [Required] [Field] [String]: database user name.

## 6. Database password [Required] [Field] [String]: connection password.

## 7. Database Name [Required] [Field] [String]: database name.
8. Timeout, ms [Required] [Field] [String]: connection timeout in milliseconds (required).


## 9. Enable SSL [Optional] [Action]: SSL encryption option.

## 10. Test connection [Required] [Action]: button to verify connection.

## 11. Cancel [Optional] [Action]: cancel the connection configuration saving.
12. OK [Required] [Action]: save the connection configuration.

After you've successfully tested the connection to your database, click OK to save the connection configuration to the folder you select.

Create a process: create a new Process in your system and add the DB Call node to it.

Screenshot 212: Add the Database Call node.

Connect the node to the database: link the DB Call node to your database by navigating to the connection parameters in the Connection field.

Screenshot 213: Link the Database Call node to your database.

Execute a query: configure a query in the node. For example, select the SQL in the Language field and enter a query to retrieve information from your database.

Screenshot 214: Enter an SQL query.

Save changes and switch to the View mode: Click Deploy to apply all changes and switch to the View mode.

Send an empty task to your Process to check its operation: In the View mode, click +New task, select Create, and click Add task to send a new empty task to your Process.

Screenshot 215: Sending an empty task.

Check whether your task in the final node contains information retrieved from the database.

Screenshot 216: Viewing the task in the Final node.

After checking your Process operation, you can configure and use your Database Call node.

Node Settings

The Database Call node has the following parameters:

Screenshot 217: Database Call settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Connection [Required] [Action]: Selects the connection to your database. Click the directory icon  and navigate to the saved connection configuration that you’ve created in Preparting to Work with the Database Call. 
Note: For more information about how to connect your database to Corezoid, go to Examples.

DB type [Required][Field][String]: Shows the selected DB type.

Host  [Required][Field][String]: Shows the selected DB host.

Port  [Required][Field][String]: Shows the DB port.

DB name  [Required][Field][String]: Shows the selected DB name.

SSL  [Required][Field][String]: Shows whether the SSL encryption is on.

Language [Required] [Action]: Selects the language of queries to the selected database. For now, only SQL is available.

SQL Query [Required] [Field]: Input your SQL query.
Note: To access task parameters, use curly braces: {{some_parameter}}. Ensure that the query result does not surpass the maximum task size limit.

Code editor [Optional] [Action]: Click Code editor to open the code editor with your SQL request, where:
Screenshot 218: Code editor full-screen mode.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

18. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

19. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

20. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

21. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

22. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Create a table
CREATE TABLE alc (

user_id integer,

conveyor_id integer,

name text,

description text

);

Insert a new row into a table
INSERT INTO alc (user_id, conveyor_id, name, description)

VALUES (13, 777000, 'Send Message', 'Use to send text messages to phone number')

Call stored function with one parameter (PostgreSQL)
SELECT function_name(arg)

Select data from two tables using JOIN
SELECT alb.conveyor_id, CONCAT('https:://api.corezoid.com/api/2/json/', alb.hash) as URL, alc.*

FROM "public"."alb" alb

LEFT JOIN "public"."alc" alc ON alc.conveyor_id = alb.conveyor_id

WHERE alc.conveyor_id is not null

Update data based on task parameters
Change the value of the hash field with the value of {{URL}} parameter for a row with conveyor_id equals to {{conv_id}}.
UPDATE alb

SET hash = '{{URL}}'

WHERE conveyor_id = '{{conv_id}}'

Error handling & troubleshooting

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 19: Error parameter names.

*The error tag __conveyor_db_call_return_type_tag__ may have the following values.

Table 20: Database Call node errors.

When working with your Process, you may encounter the following issues.

Table 21: Database Call node issues.


