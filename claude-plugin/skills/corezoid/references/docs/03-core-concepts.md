<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

### 2.3 Core Concepts
Corezoid enables users to build dynamic workflows using a Process-oriented model. A Process represents a sequence of tasks or events, while states act as the checkpoints or stages within the Process. Events transition the workflow between states, enabling logic-based automation.

Node: A building element for Processes, a unit of work in the Process.

Process: A structured sequence of states defining the logic and actions to accomplish a specific task.

State: Represents a condition within the Process. Examples include "Data Received," "API Called," or "Task Completed."

State Diagram: A diagram that tracks and stores an object state.

Event: A trigger that causes transitions between states. Events may depend on conditions, time, or external inputs.

Task: A discrete unit of work within a Process. Tasks are sets of data in JSON format saved as key-value pairs (e.g., { "key": "value" }). They serve as inputs for nodes to execute actions such as sending notifications, making API calls, or updating databases. Tasks can be added manually, imported from CSV files, loaded via direct URL, or submitted using the Corezoid API.


### 2.3.1 Nodes
Nodes in Corezoid are building blocks that determine how tasks are processed, routed, or manipulated at each step within your Processes and State Diagrams. By adding and connecting nodes, you design the structure of your workflow. Based on their functions, nodes are organized into the following categories:


Diagram 3: Node palette showcasing available node types with descriptions.

Flow Control: These are the fundamental building blocks that control the basic flow and timing of tasks through a Process.

Code: Focused on manipulating and transforming task parameters and data.

External Resources: Designed for integrating with external systems and data sources.

Queue (accumulating and retrieving tasks): Manage task accumulation and retrieval for asynchronous processing.

Process Interactions: Facilitate communication and data flow between different Processes.

Dashboard (gathering statistics on tasks): Tracks and accumulates values from task parameters and provides statistical insights and monitoring capabilities for Process metrics.

Each node has specific parameters and configurations that allow users to define its behavior.

Flow Control (basic building nodes):

Start: The entry point into a Process or State Diagram for tasks, initializing logic execution. Mandatory for every Process and State Diagram.

End: The final node in a Process or State Diagram where tasks are collected after going through all the nodes in the workflow. Mandatory for every Process and State Diagram.

Condition: Routes tasks within the workflow based on specified parameter values. You can use it to trigger alerts and verify payments.

Delay: Pauses task processing for a specified time. Use it for scheduled mailing, SMS sending.

Parallel Processing (coming soon).

Screenshot 34: Configuration panel for the Condition node.

Screenshot showing the configuration panel for a Condition node with an example condition (e.g., if order_status == 'complete').

Operations on Task Parameters:

Set Parameters: Adds new or updates existing parameters for a task. Use it for data modification stored in a State Diagram.

Code: Executes your custom JavaScript or Erlang code for advanced data manipulation.

Git Call: Runs code stored in a Git repository written in JavaScript, Golang, Python, Java, PHP, Closure, Lisp, and Prolog out of the box. Use the custom Dockerfiles feature to run code in any language.

Screenshot 35: Configuration panel for the Git Call node.

External Resources (accessing external resources)

API Call: Interacts with external APIs by sending requests and processing responses. You can use it with social media, payment gateways, or weather services.

Database Call: Executes SQL queries on an external database for interaction with stored data on the task level. Use this node to update an external database or select and retrieve data from it.

Screenshot 36: Configuration panel for the API Call node.

Example of an API Call node with input fields for the URL, headers, and payload.

Queue (accumulating and retrieving tasks):

Queue: Stores tasks for later processing. Use it for load balancing or implementing asynchronous workflows, like batch notification sending.

Get from Queue: Retrieves tasks from a specified queue. Use it together with Queue nodes to resume task processing in your workflow.


### 2.3.2 Tasks
Overview

A task is a set of data in JSON format saved in key-value pairs ("key": "value"). Tasks can:

Execute specific actions, such as API calls or data manipulation.

Be dynamically assigned based on Process logic.

Report real-time status and results.

Screenshot 37: Task execution log showing task details, status, and timestamps.

Task details

The node that the task reached has a counter showing the number of received tasks.

Screenshot 38: Task distribution.

The received task has the following data:

ID: A unique value in the entire system.

REF: A unique value in the current Process.

Created: Date and time when the task was created.

Changed: Date and time when the task was changed.

Task parameters in the JSON or Table format.


#### REF parameter
REF parameter must have a unique value within a Process for all the tasks that are not located in the Process final nodes.
You can specify the REF (reference) parameter for new tasks in Corezoid UI and via the Corezoid API. When adding a new task in the UI, the `getRandomRef` function is used to generate and suggest a REF value. You have the option to change the suggested REF manually.

For tasks added through the UI, the `getRandomRef` function creates a unique reference by combining two parts:

1. `Date.now().toString()` - This retrieves the current timestamp in milliseconds since January 1, 1970, and converts it to a string, providing a unique number that increases over time.

2. `Math.floor((Math.random() * 100) + 1)` - This generates a random number between 1 and 100 (inclusive) and rounds it to the nearest whole number.

The function combines these two components to create a unique reference. For example, it might look like this: 167890123456789 (timestamp) + 42 (random number) = 16789012345678942.

Screenshot 39: Task view in the archive.


#### 2.3.2.1 Task Adding
In Corezoid, you can add a task to a Process differently. Use one of the following ways.

Send a task manually.

Import a task from the CSV file.

Load a task via direct URL.

Use the Corezoid API.

For one Process, the recommended number of tasks is ⩽100 000.


#### Send Task Manually
After you have set all the parameters in your Process, you can send the task to it manually. To do so:

Switch to the View mode by clicking View on the upper panel.

In the upper-left corner of the page, click + New task.

In the New task dialog that opens, enter the key and value in the Key and Value fields correspondingly, and then select the needed type of data in the dropdown list (S (String), N (Number), B (Boolean), A (Array), O (Object)).

Click Add task.

Screenshot 40: Task view in the archive.

The task goes to:

The Success End node if it meets the requirements specified in the node.

The Error End node if it doesn’t meet the requirements specified in the node.

Below you can see a short video about sending a task manually to a Process.

Screenshot 41: Sending a task manually

Import Task from CSV File

After you set all the parameters in your Process, you can import a task from a file. To do so:

Switch to the View mode by clicking View on the upper panel.

In the upper-left corner of the page, click Import from CSV.

Screenshot 42: Task view in the archive.

In the Import from CSV dialog that opens, click Select a file to select the needed file, select Divider and Encoding, and then click Next.

Screenshot 43: Task view in the archive.

In the next Import from CSV dialog that opens, select the Parameters names are in first row checkbox, select the needed column name for each column, and then click Import.

Screenshot 44: Task view in the archive.

After the file has been imported, click Done.

Screenshot 45: Task view in the archive.

The task goes to:

The Success End node if it meets the requirements specified in the node.

The Error End node if it doesn’t meet the requirements specified in the node.

Below, you can see a short video about importing a task from the CSV file to a Process.

Screenshot 46: Task import from a CSV file.

Load Task via Direct URL

By using the Direct URL option, you can load a task via JSON, XML, or NVP to a Process and enable the authorization for task loading (see Start for details on authorization use). To do so:

Open the needed Process in the Edit mode, and then click the Start node.

On the Start node details panel that opens, leave the Direct URL for tasks upload checkbox selected by default, and then click the needed way to load a task:

Copy webhook via JSON

Copy webhook via XML

Copy webhook via NVP

Send your payload to the URL by using the POST method.

Screenshot 47: Task view in the archive.

Below, you can see a short video about loading task data via direct URL.

Screenshot 48: Task view in the archive.

To test how it works, use Postman:

Type: POST

URL: Direct URL from the clipboard

Body: Request body, for example {"text":"Hello!"}

Type of Body: raw

Content/type: JSON (application/json)

The response contains the task ID (the obj_id parameter of the ops object). See the video below.

Screenshot 49: Task view in the archive.


#### 2.3.2.2 Task Parameters
Task parameter name

The task parameter name must be unique for all tabs and can contain:

Big and small Latin letters

Numbers

Special characters: _, #, @, $, , [, ], .

If the parameter name contains special characters like ".", "[" or "]", they have to be separated with a backslash:

phone[0]: Element of the "phone" array

phone\[0\]: Parameter "phone[0]"

Screenshot 50: Task view in the archive.

Task parameter type

The task parameter can be of the following types:

String (text and numbers together)
{

"name": "John"

}

Number (integer, float):
Note: The maximum value for the Number type is 2ˆ53 = 9 007 199 254 740 992. For larger values, use the String type.
{

"card_number": 123456789,

"bonus": 10.50

}

Boolean (true, false)
{

"send_notifications": false,

"subscribed": true

}

Array:
{

"phones": [

"+380991234567",

"+380661234567"

]

}

Object (set of Key-value pairs)
{

"address": {

"city": "Odessa",

"zip_code": 65000

}

}

Set task parameters

Setting task parameters helps you save time when configuring data in the node or entering parameters in the task before sending it. To set task parameters:

In the upper-right corner of the page of your Process, click the parameters icon .

Screenshot 51: Task view in the archive.

In the Task parameters dialog that opens, click the needed tab (Input, Local, or Output), and then click + Add parameter.
The Task parameters dialog has the following tab with parameters:

Input: Parameters which go to the Start node of a Process.

Local: Internal frequently used parameters for fast and convenient use in logic.

Output: Parameters, which are the result of a Process.

Screenshot 52: Task view in the archive.

In the table that opens:

Enter the parameter name in the Name column.

(Optional) Enter the parameter description in the Description column.

Specify the parameter type (S (String), N (Number), B (Boolean), A (Array),
O (Object)) in the Type column.

Select the checkbox in the Auto-clear column to hide the parameter value (display as “***") in the Archive tab.

Select the checkbox in the Required column to set the parameter as required.
Note: The Required column is only available for the Input and Output tabs.

Click .* in the RegExp column to use Regular Expression: enter the needed values (RegExp for validation of value and Text of the response in case of error regexp), and then click Save.
Note: The RegExp column is available for the Output tab only
Screenshot 53: Task view in the archive.

Screenshot 54: Task view in the archive.

In the Task parameters dialog, you can perform additional actions:

Copy and paste the needed parameter by selecting the checkbox and clicking Copy and Paste consecutively

Move the needed parameter to another tab (Local or Output) by hovering over the needed parameter row and clicking the arrows icon

Copy the needed parameter by hovering over the needed parameter row and clicking the copy icon

Delete the needed parameter by hovering over the needed parameter row and clicking the trash icon

To turn off task reference masking (for 3-digit and 16-digit numbers that fall within the range of possible CVV and PAN pay card numbers), select the Mask REF checkbox.

Screenshot 55: Task view in the archive.

In the lower-right corner of the Task parameters dialog, click Save.

The added parameters are saved, and you can use them when configuring data in the node or sending tasks to a Process.

Below, you can see a short video about adding a task parameter on the node details panel. By default, the parameter is added to the Local tab.

Screenshot 56: Task view in the archive.

Why set task parameters

Input tab: The task parameters of the Input tab are automatically copied to a new task.

Screenshot 57: Task view in the archive.

When adding the Call a Process, Copy Task, and Modify Task nodes to a Process, the Input parameters of the selected Process are automatically filled in.

Screenshot 58: Task view in the archive.

Output tab: The task parameters of the Output tab are used to configure the Reply to Process node.

Screenshot 59: Output tab.

Local tab: The task parameters of the Local tab are shown in the dropdown list when creating a task.


#### 2.3.2.3 Task Management
In the task dialog of the End node, you can:

View task data in the JSON or Table formats by clicking the expand icon  next to View

Screenshot 60: View task data.

Renew task data by clicking the refresh icon

Screenshot 61: Renew task data.

Export a task to a CSV file by clicking the CSV icon 

Screenshot 62: Export to CSV icon.

Below, you can see a short video about exporting a task to a CSV file.

Screenshot 62: Export to CSV.

View the node info by clicking the info icon

Screenshot 63: Info menu.

By clicking the options icon :

Set scroll (vertical or horizontal)

View system parameters

Delete all tasks (except Success and Error End nodes)

Reset counter

Screenshot 64: Three-dot menu.

View tasks statistics by clicking Statistics and selecting the needed time range

Screenshot 65: Statistics tab.

Below you can see a short video about viewing task statistics.

Screenshot 66: Statistics display in real time.

Note: The tasks are stored in a Process until the end of the month, and on the first day of each month they are deleted. But, the final node counters always show the total number of tasks received.


### 2.3.3 Processes
A Process represents a sequence of steps or tasks designed to achieve a specific goal. Processes are the backbone of Corezoid workflows. They include:

Start and End Points: Define where the Process begins and concludes.

Transitions: Logical connections between tasks or nodes.

Triggers: Events that initiate or modify Process execution.

Diagram 4: Example of a simple Process flow with start, action, and end nodes.

For more details, see Processes in the Glossary.


### 2.3.4 State Diagrams
A State Diagram is a graphical representation of a Process, showing how data flows between different states and nodes. Benefits include:

Visual clarity for complex workflows.

Simplified debugging by tracing transitions.

Enhanced collaboration with a shared visual model.

Screenshot 67: State diagram example.

More about this can be found in the Glossary under State Diagrams.


### 2.3.5 Parameters
Parameters can be of the following types:

Task parameters (Global and Local)

Node parameters (Callback URL, Count, and Sum)

For more information about how to get task parameters from a State Diagram, go to Getting task parameters from State Diagram.


#### Task parameters
Task parameters can be Global and Local.

Global parameters

System-defined, read-only parameters available in Condition, Set Parameters, API Call, Queue, Copy Task, Call a Process, Reply to Process, Modify Task, and Sum nodes.

The Global parameters are the parameters defined by the system. You can use them, but you can’t customize them. In the table below, you can see the list of Global parameters, their types, and description.

Table 1: Global parameters.

In the video below, you can see how to access the Global parameters from the node details panel.

Screenshot 68: Global parameters access.


#### Local parameters
User-defined parameters added manually to Process or State Diagram.

For more information on how to add Local parameters, go to Set task parameters.

In the video below, you can see how to access the Local parameters from the node details panel.

Screenshot 69: Access the Local parameters from the node details panel.


#### Getting task parameters from State Diagram
Precondition:

Existing State Diagram.

Stored tasks.

Access to the State Diagram.

Corezoid tasks are stored in the JSON format, meaning that they are represented as objects.

You can use a State Diagram as a data storage from where you can get a single or multiple parameters by using the following template for your request:

Screenshot 70: State Diagram parameters scheme

Where:

conv: Is a constant keyword used to get data from a State Diagram.

Methods to define the State Diagram:

variable: Is data that varies depending on the entity that you refer to. For example, {{Process_ID}} that stores a different ID number for each Process.

static ID: Is an exact data, for example, a Process ID.

@alias-name: Is the name of the alias you are calling.

.ref: Is a constant keyword used to get data from a task with a corresponding reference number.

Data type:

variable: Is data that varies depending on the entity that you refer to. For example, {{Reference_ID}} that stores a different ID number for each reference.

static ID: Is an exact data, for example, a reference ID.

(Optional) .parameter: Is a specific parameter name that you are retrieving.

When working with a State Diagram, you can get:

The whole task by using the following parameter request:
{{conv[{{Process_ID}}].ref[{{REF}}]}}

Where:

Process_ID is the Process ID of the State Diagram (can be found by clicking the Start node in the Edit mode).

REF is the reference of the task.

For example: The following statement will return all the task parameters of the 12345 task from the Customers State Diagram:
{{conv[customers].ref[12345]}}

A single task parameter by using the following static parameter request:
{{conv[{{Process_ID}}].ref[{{REF}}].parameter}}

Where:

Process_ID is the Process ID of the State Diagram (can be found by clicking the Start node in the Edit mode).

REF is the reference of the task.

parameter is the parameter you want to retrieve.

For example: The following statement will return the amount_owed task parameter of the 12345 task stored in the Customers State Diagram:
{{conv[customers].ref[12345].amount_owed}}

Corezoid will try to automatically match the type if the accessed value type doesn't match the one specified. To avoid potential errors, specify the correct parameter type of the value you are trying to get.

A single task parameter by using a dynamic parameter request, for example:
{{conv[{{my_proccess_name}}].ref[{{my_task_reference}}].amount_owed}}

Where:

Process_ID and REF are names of variables that store their values in double curly braces and not the exact values.

parameter is a static value.

A single task parameter by using their alias, for example:
{{conv[@alias-name].ref[{{REF}}]}}


#### Node parameter examples
Callback URL

With the Callback URL function, you can get a Callback URL in the Waiting for Callback node dynamically.

Screenshot 71: Getting a Callback URL in the Waiting for Callback node dynamically.

For example:

// Returns Corezoid or Mandrill CallbackURL by {{node_id}}

{{node[{{node_id}}].public_callback_corezoid}}

{{node[{{node_id}}].public_callback_mandrill}}

// Returns Corezoid or Mandrill CallbackURL by {{node_id}} from {{conv_id}} process

{{conv[{{conv_id}}].node[{{node_id}}].public_callback_corezoid}}

{{conv[{{conv_id}}].node[{{node_id}}].public_callback_mandrill}}

Count

The Count function returns the amount of tasks in a node with the specified ID. For example:

// Node ID = 561a272782ba961374d44178

{{node[561a272782ba961374d44178].count}}

// Returns amount of tasks in the node specified by the parameter {{node_id}}

{{node[{{node_id}}].count}}

// Returns amount of tasks in the node specified by the parameter {{node_id}} from {{conv_id}} process

{{conv[{{conv_id}}].node[{{node_id}}].count}}

Sum

The Sum function returns the sum value for the selected task parameter. For example:

// Node ID = 561a272782ba961374d44178

{{node[561a272782ba961374d44178].SumID}}

// Returns amount by SumID parameter from node {{node_id}}

{{node[{{node_id}}].SumID}}

// Retuns amount by SumID parameter from {{node_id}} from {{conv_id}} process

{{conv[{{conv_id}}].node[{{node_id}}].SumID}}

SumID value

Where the SumID is the Sum node ID value. See the article.


### 2.3.6 Functions
The functions listed below can be used in the Condition and Set Parameters nodes. Please refer to the Erlang documentation for more details on the functions supported in Code nodes.

Using functions, you can perform various operations on data to get desired values in your Processes and State Diagrams.

Basic functions in use

Below are the basic functions for configuring nodes in your Processes and State Diagrams.

$.math()

With the $.math() function, you can perform mathematical operations (addition, subtraction, multiplication, and division).
For example:

To calculate the 1+1 result, use:
$.math(1+1)

To calculate the sum of the specified parameter’s value + 10, use:
$.math({{parameter_name}}+10)

To calculate the difference between two parameters, use:
$.math({{parameter_name1}}-{{parameter_name2}})

$.random(N)

The $.random(N) function returns a random number depending on the specified N, where:

.random(0): always returns 0.

.random(N), N>1: returns a positive random number.

$.random(N), N<0: returns a negative random number.

If the N value is bigger than int64, int64 will be used instead.

$.sha1_hex

The $.sha1_hex(content) function returns sha1 in hex from a constant or task parameter if it is specified in the {{parameter_name}} format. For example, to get the sha1 in hex for the constant 100, use:

$.sha1_hex(100)

$.md5_hex

The $.md5_hex(content) function returns md5 hash in hex generated from a constant or task parameter if it is specified in the {{parameter_name}} format. For example, to get the md5 in hex for the constant 100, use:

$.md5_hex(100)

$.base64_encode

The $.base64_encode(content) function converts a constant or a task parameter in the base64 format if it is specified in the {{parameter_name}} format, where content means a constant or {{parameter_name}}.

$.unixtime()

The $.unixtime() function returns the current time in Unix Time in GMT 0. You can use arithmetic arguments to adjust the current time value.
For example:

To return the current time in Unix Time, use:
$.unixtime()

To return Unix Time for current time + 60 min, use:
$.unixtime(%y-%m-%d %h:%i+60:%s)

To return Unix Time for the current date with the set time 02:00:00, use:
$.unixtime(%y-%m-%d 02:00:00)

$.date(%y-%m-%d %h:%i:%s)

The $.date(%y-%m-%d %h:%i:%s) function converts a date in the day and time format. You can use arithmetic arguments. For example:

To return the current date and time in the YYYY-MM-DD HH:MM:SS format, use:
$.date(%y-%m-%d %h:%i:%s)

To add +1 day to the returned date in the YYYY-MM-DD HH:MM:SS format, use:
$.date(%y-%m-%d+1 %h:%i:%s)

$.unixtime().tz

With the $.unixtime().tz function, you can get the current time of a specific timezone. For example, to return the current time in Kyiv (Eastern European time zone) in the Unix Time format, use:

$.unixtime().tz('Europe/Kiev')

$.map() and $.filter()

You can use the $.map() and $.filter() Erlang functions in the Set Parameters node in a similar way to how you use the .math() and .unixtime() functions. The use of the $.map() and $.filter() functions aims at making responses from external APIs more lightweight and tasks smaller after passing through the API Call nodes.

The $.map() and $.filter() functions are used in the following constructions:

$.map(fun(Item) -> end, arr)

$.filter(fun(Item) -> end, value)
where:

fun is the supported function.

Item is an arbitrary value and the Item value must be capitalized.

arr is a parameter of an input task, which contains an array.

value is a single value.

A function body follows the arrow ->, in which you can write allowed expressions using simple operations from ALLOWED_INF_EXPRS (expressions allowed in $.map() and $.filter() functions), and some functions from ALLOWED_EXT_FUNS (allowed in $.map() and $.filter() functions).

Using the the fun() function with the {{...}} construction

You can't use the {{...}} construction in the fun() function.

ALLOWED_EXT_FUNS

{proplists,'_','_'},

{base64,'_','_'},

{binary, split, '_'},

{binary, replace, '_'},

{eutils, get_value, 2},

{eutils, from_json, '_'},

{eutils, to_json, 1},

{erlang,binary_to_float,1},

{erlang,binary_to_integer,1},

{erlang,integer_to_binary,1},

{erlang,integer_to_binary,2},

{erlang,round,1},

{erlang, is_integer, 1},

{erlang, is_binary, 1},

{erlang, is_list, 1},

{erlang, is_float, 1},

{erlang, is_boolean, 1},

{erlang, is_number, 1},

{erlang, hd, 1},

{erlang, tl, 1}

ALLOWED_EXT_FUNS performance

The use of the functions from the ALLOWED_EXT_FUNS modules list and adhering to the specified syntax enable maximum execution performance. In this case, the performance will be kept at a high level and gradually improve when support for newer Erlang versions in Corezoid is implemented.

proplists - let's take a closer look at the get_value and delete functions. For example, we need to get a value from the test and increase it by 1. To do this, we'll use the following code:

Test = proplists:get_value(<<"test">>, Item),

[{<<"test">>, Test + 1} | proplists:delete(<<"test">>, Item)]

In this example, we've written the "test" value to the Test variable. As the Item is a list, we added a new test variable with the "Test +1" value to the head of the list and removed the old test variable from the Item. Note that we'll have both test variables processed in the code without removing the old variable.

base64 - note the use of encode and decode functions; they are used the same way as in other languages:

Test = proplists:get_value(<<"test">>, Item),

[{<<"base64">>, base64:encode(Test)} | Item]

Analogous to the previous example, we've got a value from the test and written it to the Test variable. Then, we updated the base64 value with the new base64 value and added it to the Item.

binary - split and replace functions are available. They allow splitting a string and replacing it with another string.

eutils - internal Corezoid library. It offers the following functions:

get_value - similar to proplists and serves the same purpose;

from_json - converts JSON to list;

to_json - converts list to JSON.

For example, if your task contains the following data:

[{"test":"{\"a\":1}"}, {"test":"{\"a\":2}"}, {"test":"{\"a\":4}"}].

you can use the following code:

Test0 = eutils:get_value(<<"test">>, Item),

Test1 = eutils:from_json(Test0),

[{<<"a">>, eutils:get_value(<<"a">>, Test1)} | Item]

The code takes the test value, converts the string to a list, and assigns the Test1 the following value

[

{<<"a">>, 1}

]

We take the "a" value and remove it from the test, then we add it to the Item.

erlang - only the functions for converting binary to number and vice versa are available.

ALLOWED_INF_EXPRS

'+',

'-',

'*',

'/',

'bnot',

'div',

'rem',

'band',

'bor',

'bxor',

'bsl',

'bsr',

'not',

'and',

'or',

'xor',

'andalso',

'orelse',

'==',

'/=',

'=<',

'<',

'>=',

'>',

'=:=',

'=/=',

'++',

'--'

Examples

Multiplying all array elements by a specified value ($.map() function)

In the Set Parameters node input, take a task containing the a array:
"a": [1,2,3]

In the Set Parameters node, enter the $.map() function :
"b": "$.map(fun(Item) -> Item*2 end, {{a}})"

Each a array element is multiplied by 2, and the results are written to the b array:

"b": "[2,4,6]"

Filtering out uneven numbers and writing even numbers ($.filter() function)

Set the b task:
[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

In the Set Parameters node, write the $.filter() function:
"b1": "$.filter(fun(Item) when Item rem 2 < 1 -> true; (_) -> false end, {{b}})"

The response is:

"b1":[2,4,6,8,10,12,14]

Conversion of an array with objects containing the "fieldName" key into an array that includes only values of this key:

Generic method:
$.map(fun(E) -> FieldName = eutils:get_value(<<"fieldName">>, E), FieldName end, {{arr}})

Simplified method:
$.map(fun(E) -> eutils:get_value(<<"fieldName">>, E) end, {{arr}})

Conversion reverse to the one in the previous example - an array of simple primitives is conversed to an object array:

By declaring a key-value pairs collection:
$.map(fun(Value) -> #{<<"fieldName1">> => Value, <<"fieldName2">> => Value} end, {{arr}})

By declaring a tuples collection:
$.map(fun(Value) -> [{<<"fieldName1">>, Value}, {<<"fieldName2">>, Value}] end, {{arr}})


### 2.3.7 Dashboards
Overview

A dashboard is a tool in Corezoid designed for collecting and visualizing statistics and reports related to Processes and State Diagrams. Dashboards present data in the form of charts, allowing users to gain insights from the data visually. The charts, in turn, use data from nodes of built Processes and State Diagrams. The tasks in these nodes (counters) serve as the source of data (metrics) of the charts.

Create Dashboard

To create a Dashboard:

On the Workspace tab, click Create, and then in the dropdown list, select Dashboard.
Note: You can import a dashboard from a JSON file that contains a folder with a dashboard and related Processes and charts.To do so, in the dropdown list, select From file and then choose the file from your device.

Screenshot 72: Dashboard creation on the Workspace tab.

In the Create dashboard dialog that opens, enter a dashboard name and description (optional), and then click Ok.

Screenshot 73: Create Dashboard window.

On the Chart details panel of the created dashboard page, click the plus icon + next to Metrics.

Screenshot 74: Adding metrics to a Dashboard.

In the Metrics table, select the needed data source for the chart:

Folders: A list of folders with Processes

Processes: Processes located in the selected folder

Process nodes: Nodes of the selected Process.
Note: Click the plus icon + to add a node to the chart.

Added metrics: Lists the nodes added to the dashboard

Note: After you have selected the needed data, in the upper-right corner of the table, click the close icon .

Screenshot 75: Metrics menu.

(Optional) On the Chart details panel:

Click Table chart, and then select the needed chart type (Bar chart, Pie chart, Funnel chart).

Click the copy icon to make a copy of the chart.

Click the delete icon to delete the chart.

Screenshot 76: Chart menu.

(Optional) In the upper-left corner of the created dashboard page, click + Add chart and customize a new chart by following steps 3-6.
Note: You can add multiple charts to your dashboard.

Screenshot 77: Adding a chart to a Dashboard.

In the upper-left corner, click Save.

Screenshot 78: Saving a Dashboard.

You’ve created the dashboard, and now can easily customize it.

Additional actions

Select time range

You can select the needed time range for your dashboard by clicking Real-Time in the upper-right corner of the page.

Screenshot 79: Viewing Dashboard real-time metrics.

The Real-Time mode works only for the End node where the tasks are accumulated and for the Waiting for Callback, Delay and Set State nodes (in a State Diagram) where the tasks are delayed for the time specified in the Process. Nodes of other types do not accumulate tasks, resulting in empty chart data when the Real-Time mode is selected.

Resize chart

Adjust the size of a chart by moving the cursor to its left or right side and setting the desired size.

Screenshot 80: Viewing Dashboard

Add link to chart

If your data has a hierarchical structure with nested elements, you can display detailed information by linking the chart to another dashboard that provides in-depth metric details.
To add a link to a chart:

In Metrics of the Chart details panel, click the link icon .

Screenshot 81: Adding a link to a chart.

In the Linked chart table, select the needed dashboard and a chart in it.


Screenshot 82: Linked chart table.

After you’ve added the link, you can open it by clicking the corresponding metric link icon.


### 2.3.8 Projects
Overview

A project is a workspace where you can store and manage Processes, State Diagrams, Dashboards, API keys, aliases and folders.

Core Components

Stages

Development environments for Processes

Default: Production and Develop

Group Processes by environment type

Aliases

Replace Process IDs with readable names

Enable flexible Process interaction

Variables

Stage-level settings

Allow Process reuse with different values

Environment-specific configuration

Versions

Stage snapshots

Track and restore previous states

Support rollback capabilities

Best Practices

Development

Use distinct stages for development phases

Implement continuous integration flow

Maintain organized Process groups

Testing

Create dedicated testing environments

Validate Process interactions

Verify variable configurations

Deployment

Use merge functionality for updates

Follow stage-to-stage promotion

Maintain version control

Create project

To create a project:

In the upper-left corner of the Workspace tab, click the expand icon, and in the dropdown list, select the needed company.
Note: Don’t select My Corezoid as selecting it means no user company is selected.

Screenshot 83: Selecting a workspace.

In the upper-left corner, click Create, and in the dropdown list, select Project.
Note: To import a project file from your device, select From file.

Screenshot 84: Create-Project.

In the Create project dialog, enter your project name and description (optional), and then click Ok.


Screenshot 85: Create project window.

The new project is created and automatically added to the Projects folder.

Screenshot 86: New project in the list.

Manage project

To manage a project, click the desired project in the Projects folder.

Screenshot 87: Select a project in the list to manage.

In the Projects, you can:

Share the project with other users and groups:
a. In the upper-right corner, click the share icon .
b. In the Invite user or group field of the Sharing settings dialog that opens, enter the name or email of the needed user or group, press Enter on your keyboard, and then click Send invitation.
Note: Users and user groups that you want to provide access to the project, must be registered in your company.

Screenshot 88: Project sharing-invite users.

c. After the selected user has confirmed the invitation by email, set the needed sharing permissions checkboxes (View, Task management, and Modify), and then click Save.
Note: You can select the permissions for the user you want to share with before clicking Send invitation. Setting the permissions for a user after the user has clicked the link in the email sets the new permissions. Every time permissions change, the user receives the corresponding notification by email.

Screenshot 89: Project sharing-setting permissions.

Check the project information:
a. In the upper-right corner, click the info icon .
b. View project details by clicking the Info and History tabs.

Screenshot 90: Project sharing-project info check.

Perform more actions by using the options icon  and clicking:

Download to download the project

Edit to change the project name

Delete to delete the project

Note: To perform an action on multiple objects, press Shift or Command on your keyboard, click the needed objects, and then click the options icon  .

Screenshot 91: Project sharing-project info check.


#### 2.3.8.1 Stages
Overview

Stage is an environment where you can store your Processes, State Diagrams, and so on to test and work on. After you’ve created a project, it has two stages by default: Production and Develop.

Screenshot 92: Stages subsection.

By default, each stage includes the Aliases and Variables sections where you create and manage these objects. For more information, go to Alias and Variable.

Screenshot 93: Aliases and variables.

Create stage

To create a stage:

On the Workspace tab of your company, select the needed project, and then double-click Stages.

Screenshot 94: Stages folder.

In the upper-left corner, click Create, and in the dropdown list, select Stage.
Note: You can import a stage file from your device by selecting From ….

Screenshot 95: Create menu for stages folder.

In the Create stage dialog, enter your stage name and description (optional), and then click Ok.
Note: To make the stage protected of any changes, select the Immutable stage checkbox. For more information on immutable stages, go to Immutable stage.

Screenshot 96: Create stage window.

The new stage has been created and automatically added to Stages.

Screenshot 97: Created stage in the list.

Manage stage

To see what additional actions you can perform on your stage, click the needed stage in the selected project.

Screenshot 98: Stage selected in the list.

Now, you can:

Share the stage with other users and groups:

In the upper-right corner, click the share icon .

In the Invite user or group field of the Sharing settings dialog that opens, enter the name or email of the needed user or group, press Enter on your keyboard, and then click Send invitation.
Note: Users and user groups that you want to provide access to the stage, must be registered in your company.

Screenshot 99: Invitation sending.

After the selected user has confirmed the invitation by email, set the needed sharing permissions checkboxes (View, Task management, and Modify), and then click Save.
Note: You can select the permissions for the user you want to share the stage with before clicking Send invitation. Setting the permissions for a user after the user has clicked the link in the email sets the new permissions. Every time, the user receives the corresponding notification by email.

Screenshot 100: Permissions configuration in sharing settings.

Check the stage information:

In the upper-right corner, click the info icon .

View alias details by clicking the Info and History tabs.

Screenshot 101: Info and History tabs.

Perform more actions by using the options icon  and clicking:

Create version to create a new version of a stage
Note: You can create versions only from the stages that contain at least one object (Process, State Diagram, and so on). If the selected stage does not have any objects, then the Create version option will be unavailable for selection and will be grayed out. For more information, go to Create version.

Merge to merge a stage or a version with another stage
Note: For more information, go to Merge.

Download to download the stage

Edit to change the stage name

Delete to delete the stage

Note: To perform an action on multiple stages, press Shift or Command on your keyboard, click the needed stages, and then click the options icon  .

Screenshot 102: Version three-dot menu options.

Immutable stage

When you create a project, it has two stages by default: Production and Develop. By default, the Production stage is immutable, that is protected from any changes so that no user can add any object to the immutable stage.

Note: The Immutable parameter for Stages can be toggled by a Project owner, Stage owner, or Superadmin user.

To make a stage immutable:

In the Stages section, click the needed stage, click the options icon, and in the dropdown list, select Edit.

Screenshot 103: Stage edit item.

In the Edit stage dialog, select the Immutable stage checkbox, and then click Ok.

Screenshot 104: Edit stage window.

The stage becomes immutable and gets the lock icon next to its name.

Screenshot 105: Immutable stage icon.

Note: You can make your stage accessible for other users by deselecting the Immutable stage checkbox when editing it. So, the stage will be editable, and you can add needed objects to it.


#### 2.3.8.2 Aliases
Overview

Alias is a type of Corezoid object that is used to replace numeric object identifiers with symbolic ones specified by a user. Aliases can be used to interact with Processes and State Diagrams both in the nodes and via the Corezoid API.

Create alias

You can create an alias:

At the company level

At the stage level

To create an alias:

On the Workspace tab of your company:

(At the company level) Click the Folders folder, click Aliases, and then click Create.

Screenshot 106: Aliases in folder.

(At the stage level) In the Projects folder, select the needed project and stage, double-click Aliases, and then click Create.
Screenshot 107: Create alias.

In the Create alias dialog:

In the Name and Description fields, enter your alias name and description (optional).
Note: The Short name field repeats the alias name in the Name field and must be unique within the stage; you can edit it at any time.

In the Linked object field, click the directory icon  and select the needed Process to link the alias to.
Note: You can link a Process later when editing the alias.

Click Ok.

Screenshot 108: Create alias window.

The alias has been created, and you can see its linked Process in the field. By default, the aliases provide the following access rules:

All users of a company can view the list of all aliases created in the company.

Only the alias owner can manage the alias linking to a Process or a State Diagram.

The alias owner can link the alias only to those Processes and State Diagrams to which he/she has task management and editing access.

The alias owner cannot link Processes or State Diagrams to the alias to which he/she has access only for viewing.

If the alias owner is denied access rights to a Process or a State Diagram linked to the alias, he/she cannot view the linked object name (the linked object identifier is always displayed regardless of access settings).

A user can open a linked Process or a State Diagram in the View mode if he/she has the View or Edit access to the object.

Screenshot 109: Created alias in the list.

Manage alias

To see what additional actions you can perform on your alias, click the needed alias.

Screenshot 110: An alias selected in the list.

Check the alias information:

In the upper-right corner, click the info icon .

View alias details by clicking the Info and History tabs.

Copy the webhook via JSON, XML, or NVP in the Webhook tab.
Warning: The Webhook tab is available to the alias owner only. After clearing and selecting the Direct URL for tasks upload checkbox again, the link changes and you cannot send data via the initial link.

Screenshot 111: Selected alias tabs.

Perform more actions by using the options icon  and clicking:

Edit to change the alias name

Delete to delete the alias
Note: To perform an action on multiple aliases, press Shift or Command on your keyboard, click the needed ones, and then click the options icon  .

Screenshot 112: Alias three-dot menu.

Import alias

You can import aliases together with your project in a folder. As a result, the project folder will be created with linked aliases in the Aliases tab. There may be a conflict between already existing and aliases you want to import with the message “Aliases already exist” displayed. There are two ways to solve this problem:

When uploading a file, click Upload only processes. Only folders, Processes, State Diagrams, and dashboards will be imported, while the aliases linked to them will be completely ignored.

Screenshot 113: Upload only processes.

When a file has been uploaded, click Show conflicts, and then Force upload. You can view all conflicting aliases in the file and import them by replacing the existing linked objects with imported ones.

Screenshot 114: Show conflicts.

Examples

You can specify an alias in the Call Process, Copy Task, and Modify Task nodes of a Process. You have several ways to do this in the Basic settings of the node details panel:

Select an alias by using the directory icon

Search for an alias by its name by entering the @ symbol at the beginning of the line

Enter an alias name as a task parameter (for example, @{{alias_name}}) which contains a value equal to the alias short name

Screenshot 115: Alias selection.


### 2.3.8.3 Variables
Overview

Variables are stage objects which store data for various purposes (secret, public keys and so on), which you can edit and reuse in Corezoid nodes. Variables store data in the RAW and JSON formats.

Create variable

To create a variable:

On the Workspace tab of your company, in the Projects folder, select the needed project and stage, double-click Variables, and then click Create.

Screenshot 116: Create-variable.

In the Create variable dialog:

Screenshot 117: Create variable window.

In the Title field, enter your variable title.

In the Short name field, your variable short name will be generated automatically based on the title. You can edit the short name manually.

In the Value type list, select RAW or JSON format.

In the Value field, enter the needed value or click the code editor icon  and enter the value in the Code editor dialog that opens.
Note: You can link a Process later when editing the alias.

Click to open the Code editor window in the full-screen mode.

Select the Secret variable checkbox to make your variable secret.
Note: Making a variable secret is irreversible and automatically restricts its use to the API Call nodes only.

In the Change scope restrictions block, click the title to open the Use only in window. In the window, select the nodes, in which the variable will be available for the use by selecting the corresponding checkboxes (1) and clicking Confirm (3). 
You can discard the scope restriction changes by clicking Back (2) or window close icon (4):
 
Screenshot 118: Use only in: window.

Click to hide the list of nodes where the variable will be available.
Note: You must specify at least one node for the variable.

Click OK to create a variable, or Cancel to cancel.

The variable has been created, and you can use it in your Processes.

Screenshot 119: Created variable in the list.

Variable edit

To edit a variable:

Select the variable in the list.

Click the variable three-dot menu icon or right-click the selected variable to open the context menu.

Select Edit in the menu list:


Screenshot 120: Variable edit.

In the Edit variable window, edit the variable parameters and scope restrictions.
The value is not shown for secret variables, and the Secret variable box can't be cleared when editing:

Screenshot 121: Edit variable window for secret and non-secret variables.

Click OK to save the changes.

Manage variable

To see what additional actions you can perform on your variable, click the needed variable.

Screenshot 122: Select a variable.

Now you can:

Check the variable information, by clicking the info icon .

Screenshot 123: Variable info view.

When viewing a secret variable info, the value is obfuscated in the Value column of the variables list and not shown in the variable info panel:


Screenshot 124: Variable value view for non-secret variables.


Screenshot 125: Variable value view for secret variables.

Delete the variable, by clicking the options icon  , and then clicking Delete.

Screenshot 126: Delete a variable.

Note: To perform an action on multiple variables, press Shift or Command on your keyboard, click the needed variables, and then click the needed icon.

Examples

Variable syntax:

For getting data stored in the RAW and JSON formats in variables, use:
{{env_var[id]}}

{{env_var[@shortname]}}

For getting data stored in the JSON format in variables containing nested structures, use:
{{env_var[id].key}}

{{env_var[id].key[1].param}}

Variables use:

Use of a variable to store a certificate and sign requests that you send to the API in the API Call node.

Screenshot 127: Storing a certificate in a variable.

Signing a request with a certificate by using a variable.

Screenshot 128: Signing a request using a variable.

Using the Sign the request with the secret key feature to store a secret key and sign the requests you send with it:

Create an API key and call it Key.

Create a variable, select the JSON value type, and insert the following construction (where secret is the value of the secret key.):

{

"key": {

"param": "12312",

"param2": "secret"

}

}

Save the variable with the secret key part.

Open the API Call node in the Edit mode and enter the request you want to use (with the actual conv_id and company_id parameter values from your environment):
{

"ops": [

{

"type": "create",

"conv_id": 0000000,

"obj": "task",

"action": "user",

"data": {

"code": 200

},

"ref": "test",

"company_id": "i000000000"

}

]

}

In Other, select the Sign the request with the secret key checkbox.

In the field below, enter the {{env_var[@secret-key-part].key.param2}} construction to read the necessary data from the JSON array stored in the secret-key-part variable.

In the upper-left corner of the page, click Deploy to save the changes.

Your requests sent from the API Call node will be signed with the secret key stored in the key variable.

Use variables to establish more secure authorization in Start nodes and conceal basic authentication credentials. You can use a variable, for example the webhook-var, with the following constructions:

{{env_var[@webhook-var].user}} for the username field

{{env_var[@webhook-var].pass}} for the user password field.

Screenshot 129: Using constructions in a variable.


### 2.3.8.4 Versions
Overview

Versions are created from stages. A version is a snapshot of a stage, containing all its objects, but not containing its tasks.

Create version

To create a version:

On the Workspace tab of your company, select the needed project, double-click Versions, and then in the upper-left corner, click Create.

Screenshot 130: Create a version.

In the Stages dialog, select the needed stage, and then click Continue.
Note: Empty stages are not available for selection. After selecting the stage, the success message appears if all the Processes have the Deployed status.

Screenshot 131: Create version page.

In the Create version dialog, enter the version number and change details (optional), and then click Ok.

Screenshot 132: Create version window.

The new version has been created.

Screenshot 133: Created version in the list.

Manage version

To see what additional actions you can perform on your version, click the needed one in the selected project.

Screenshot 134: Selected version in the list.

Now you can:

Check the variable information, by clicking the info icon .

Screenshot 135: Version info.

Perform more actions by clicking the options icon  and selecting:

Merge to merge the version with a stage.
Note: For more information, go to Merge.

Download to download the version

Delete to delete the version
Note: To perform an action on several versions, press Shift or Command on your keyboard, click the needed ones, and then click the options icon  .

Screenshot 136: Version three-dot menu.


### 2.3.8.5 Merge
Overview

Merge is an operation available for stages and versions in projects. Merging is adding data from a stage, version or a file (exported stage or version) to another stage. Thus, you can have a stage or version or a stage/version file as a source and an existing stage as a target.

Perform merge

Precondition
To perform a merge, you need to have at least one company and one Project in it. Before performing a merge, check the following:

No source stage Process has any errors.

All source stage Processes have the Active status.

The source stage is immutable: All source stage Processes are deployed.

The target stage is immutable: All target stage Processes are deployed.

To merge the version with another version, stage, or file:

On the Workspace tab of your company, select the needed project, and then the stage or version that you want to use as a merge source.

In the upper-left corner, click the options icon  , and then click Merge.

Screenshot 137: Version Merge selection.

In the Source and Target parts of the dialog, select the needed source (from the Stages, Versions, or From file tabs) and target correspondingly, and then click Continue.

Screenshot 138: Version merge window: source and target selection.

In the newly created folder dialog, click Merge.

Screenshot 139: Version merge window: merge confirmation.

The version has been merged to the selected stage, the success message appears in the lower-right corner of the page, and you can open the newly created stage by clicking Open stage.

Screenshot 140: Version merge progress indicator.

Error handling & troubleshooting

When performing a merge, you may encounter the following errors.
1. The stage is not immutable: There are undeployed Processes in a stage. The stage name has the warning icon with the number of undeployed Processes inside.

Screenshot 141: Merge errors.

Solution
First option: Open each Process in the Edit mode, and in the upper-right corner of the page, click Deploy.

Second option:

Right-click the not immutable stage with undeployed Processes and in the dropdown list, select Rollback.

Screenshot 142: Merge rollback.

In the Deploy Stage’s Processes dialog, click Deploy All.

Screenshot 143: Stage Processes deployment.

Right-click the needed not immutable stage, and in the dropdown list, select Edit.

Screenshot 144: Stage edit.

In the Edit stage dialog, select the Immutable stage checkbox, and then click Ok.

Screenshot 145: Immutable stage checkbox.

The stage becomes immutable and gets the lock icon next to its name.

Screenshot 146: Stage immutability indicator.

2. Unsuccessful merge. The merge was unsuccessful, and you get the corresponding notification in the upload master window.

Screenshot 147: Unsuccessful merge indicator.

Solution
First option: In the upload master window, click Show errors. The Errors list dialog opens with error details. You can find the corresponding Processes and fix the errors.

Screenshot 148: Merge errors display.

Second option: In the upload master window, click Rollback, which means reverting unsuccessful merge changes. Now you can fix errors and try to perform a merge once again.

Screenshot 149: Merge rollback.


## 2.3.9 Notation Schema for Corezoid Node Parameters
Description of Corezoid node parameters follows the general scheme:

Parameter Name [Required Status] [UI Element Type] [Data Type]: Brief description.

Parameter Required Status

[Required]: Mandatory parameter

[Optional]: Optional parameter

UI Element Type

[Field]: Text input field

[Action]: Action or command

Data Type

[String]: Sequence of characters, digits, or symbols treated as text. Includes alphanumeric and special characters.
Example: hello, +1-999-666-3333, %$@#.

[Number]: Positive and negative numbers with and without fractions.
Example: 0, 707, -100, 707.07.

[Boolean]: True or false values.
Example: true, false.

[Array]: List with a number of elements in a specific order—typically of the same type.
Example: rock (0), jazz (1), blues (2), pop (3).

[Object]: Object with nested structure, for example {{conv[{{Process_ID}}].ref[{{REF}}].parameter}}. See 2.3.5 Parameters for more details.

[Timestamp]: The unix time stamp is a number of seconds that have elapsed since midnight (00:00:00 UTC), 1st January 1970 (Unix time).
Example: 1632855600.

[Any]: Any of the data types mentioned above, and:

variables in double brackets, for example {{variable}},

dynamic variable contained in the currently processed tasks,

variables in nested structures (constructions), see 2.3.5 Parameters for more details.


