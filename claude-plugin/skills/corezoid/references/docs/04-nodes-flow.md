<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

## 3. Nodes Description

### 3.1 Start
Overview

Screenshot 150: Start node view.

The Start node is the single entry point for tasks in a Process or State Diagram. It receives tasks from:

View Mode: Manual task creation for testing, debugging, and configuration

CSV: Bulk data import processing

Webhooks: External task sources

Copy Task: Task duplicates from other Processes

Call a Process: Function-like Process invocation

Corezoid API: Direct platform integration for task management


Diagram 5: Start node flow.

Key points:

Added automatically when creating a Process/State Diagram

Only one Start node per workflow

Serves as webhook endpoint for external tasks

Node Settings


The Start node has the following parameters:

Screenshot 151: Start node settings.

Title [Optional] [Field] [String]: Node title.

Description [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.
Note: Cannot be used with Start node as only one Start node is allowed per Process.

Remove node [Optional] [Action]: Deletes current node from Process.
Note: Cannot be used with Start node as only one Start node is allowed per Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Process ID [Required] [Field] [String]: Unique identifier that allows you to direct your tasks to the needed Process from any other Process within Corezoid.

API key [Optional] [Field] [String]: Authentication key for secure system access. After clicking the field, you can enter the API key name, and the following key parameters will be generated automatically.

Login [Preset] [Field] [String]: Associated API login.

Secret [Preset] [Field] [String]: Generated secret key value.

Copy [Optional] [Action]: Copy key to clipboard.

Direct URL for tasks upload [Optional] [Action] [Boolean]: Enable webhook endpoint for receiving tasks. The checkbox is selected by default, which means you have to specify the generated endpoint URL value when subscribing to a webhook. 
Supported input formats: JSON, XML, and NVP.
Note: If you clear the checkbox, the endpoint URL will be turned off. When you select it again, a new endpoint URL will be generated, and you will need to update your webhook subscription.

Type auth [Optional] [Action] [String]: Authorization type to secure received requests processing by using the Basic option and to process all requests by using the No Auth option.
Note: For more information, go to Enable secure authorization.

Copy Webhook via JSON [Optional] [Action]: Copy endpoint URL in JSON format.

Copy Webhook via XML [Optional] [Action]: Copy endpoint URL in XML format.

Copy Webhook via NVP [Optional] [Action]: Copy endpoint URL in NVP format.

Connect to messenger [Optional] [Action]: Automatically configures your Process to receive messages from messengers (Telegram, Viber, Apple Business Messages, Line (partial support), and Facebook and Google Messengers).

Enable secure authorization

Now, you can enhance security for the Start node in a Process by enabling basic authentication, ensuring the username and password protection for receiving requests via Direct URL in user companies. To do so:

In the Start node settings, select Basic in the Type auth dropdown list.

Screenshot 152: Authorization type selection.

Enter the username and password in the corresponding fields and select the checkbox to save your authentication.

Screenshot 153: Specifying username and password.

Now, your node webhook is protected, and only the requests containing authorization credentials will be processed.

Username and password credentials are fully displayed in the Start node settings in the Edit mode and on the Webhook tab of the View details menu for a Process. To conceal basic authentication credentials, use variables with credentials. For example, you can use the webhook-var variable with the following constructions:

{{env_var[@webhook-var].user}} for the Username field

{{env_var[@webhook-var].pass}} for the Password field

Where:
- {{env_var[]}}: construction containing the @webhook-var variable
- [@webhook-var].parameter: variable in the construction with Username or Password parameter.

For more information on how to create a variable, go to Variable.

Important:

If you change settings, and select No Auth in the Type auth dropdown list, you will turn off the authorization and will have to enter credentials next time.

All the requests that don't contain authentication will not be processed, and the Access denied error will appear in the task.

If you have an alias linked to a Process in which you've activated the basic authorization, sending data to the alias' Direct URL also requires sending authorization credentials. Sending requests to the alias' Direct URL with no credentials will result in the Access denied error.

Examples

Add tasks manually

This is the fastest and easiest way to create a new task in Corezoid.

Screenshot 154: Manual task adding.

Importing task from CSV

If you have data stored in a file that you want to turn into tasks, you can easily do so by using the Import from CSV option. Thus, you can quickly import large amounts of data and create tasks from it.

Screenshot 155: Importing a task from CSV.

If your Process has required parameters, the CSV file must have columns for these parameters. Select any column as a Task reference (REF) and specify the data type for each column, such as String or Number.

Sending task to Webhook

In Corezoid, every Start node serves as an endpoint with its unique URL. This endpoint URL can be used to subscribe to webhooks, and you can receive external data and trigger your Corezoid Processes automatically.
The endpoint URL is generated and copied to your clipboard:

JSON
https://www.corezoid.com/api/1/json/public/0060000/*8b568f9c430f045b0c207ff8221

XML
https://www.corezoid.com/api/1/xml/public/0060000/*8b568f9c430f045b0c207ff8221

NVP
https://www.corezoid.com/api/1/nvp/public/0060000/*8b568f9c430f045b0c207ff8221

Screenshot 156: Sending a task to a webhook.

The endpoint URLs generated by Corezoid are identical except for their payload format.

Sending task from another Process

In Corezoid, it's possible to send tasks from one Process to another by using the Copy Task or Call a Process nodes:

With the Copy Task node, you can duplicate a task and send it to a different Process:


Screenshot 157: Duplicating a task to a different Process.

With the Call a Process node, you can call another Process, like a function in programming

Screenshot 158: Calling another Process.

Corezoid API

With the Corezoid API (asynchronous), you can easily send a task to the Start from any API source connected.

Error handling & troubleshooting

When working with your Process, you may encounter the following issues.

Table 2: Start node issues.


### 3.2 End
Overview


Screenshot 159: End node options view: error and success.

The End node marks the final point in a Process or State Diagram. Key characteristics:

Multiple End nodes allowed per workflow

No outgoing connections

Automatically added when creating a Process

Shows task counter in View mode

Status indicators:

Green: Successful task completion

Red: Task processing error

Diagram 6: End node flow.

In the View mode, each End node has a counter that displays the number of tasks that have reached the node.

Screenshot 160: Task counters.

Node Settings


The End node has the following parameters:

Screenshot 161: End node settings.

Title [Optional] [Field] [String]: Node title.

Description [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Success/Error [Required] [Action]:

Success: Indicates that the task processing was successful with the color green.

Error: Indicates that there was an error during the task processing with the color red.

Save the tasks in an archive [Optional] [Action]: The checkbox is selected by default and indicates that the task will be saved in an archive until the end of the current month. Thus, you can view and manage processed tasks (debugging and short-term monitoring purposes). If you clear the checkbox, the task will be deleted after processing.

On the first day of each month, all the archives are cleared, thus all the tasks are deleted regardless of whether the checkbox Save the tasks in an archive is selected.

Examples

Moving tasks to End node to get statistics

In the example below, you can see the segmentation of the users by age, representing the distribution of users across various age categories.

Screenshot 162: Distribution of tasks between End nodes.

Using End node to break out of infinite loops

In Corezoid, an infinite loop occurs when a task continuously cycles through a sequence of nodes without reaching an End node. This can happen if the Process logic doesn't include conditions or exit points that allow the task to terminate:

Task enters a node. The task, a unit of data in JSON format, enters a node in the Corezoid Process.

Node execution. The node performs its designated function, which could involve data manipulation, API calls, or conditional checks.

Transition. Based on the node's configuration and the task's parameters, the task transitions to the next node in the Process.

Loop formation. If the Process logic directs the task back to a previously visited node without encountering an End node, an infinite loop is formed.

Continuous cycling. The task continues to cycle through the same sequence of nodes repeatedly, consuming resources and preventing the Process from completing.

In the example below, you can see the End node usage for breaking out of infinite loops.

Screenshot 163: Task looping prevention using the End node.

Error handling & troubleshooting

When working with your Process, you may encounter the following issues.

Table 3: End node issues.


### 3.3 Condition
Overview

Screenshot 164: Condition node view

The Condition node works as an "if" statement and enables you to evaluate task parameters and direct the flow of your tasks based on specific requirements set by the user. The Condition node may consist of one or more Condition blocks; each block includes one or more conditions and a single output edge, which leads to the End node. By using multiple Condition blocks, you can create a nested if/switch-case structure and achieve more flexibility in controlling the task flow based on various conditions.

When a task enters the Condition node, it is evaluated against each condition in the topmost Condition block:

If the task satisfies every condition in the block, it goes to the End node of the block.

If the task doesn’t satisfy at least one condition in the block, it goes to the next Condition block.

If the task doesn’t satisfy all the conditions of any Condition block, it goes to the default End node.

Diagram 7: Condition node flow.

Task Flow

Task enters Condition node

Evaluation starts with topmost Condition Block

Two possible outcomes:

Success: Task matches all conditions → proceeds to block's End node

Failure: Task fails any condition → moves to next block

Note: If task fails all blocks, it routes to default End node.

Example Structure


Condition Node

├── Block 1: if (condition A AND condition B)

│   └── End Node 1

├── Block 2: if (condition C)

│   └── End Node 2

└── Default End Node (no conditions met)

Schema 1: Condition node structure.

Node Settings

The Condition node has the following parameters:


Screenshot 165: Condition node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Drag Condition Block [Optional] [Action]: point the mouse cursor on the icon and hold down the left mouse button to drag the Condition Block up or down. Thus, you can change the arrangement of Condition Blocks in the node.

Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets.

Comparison operator [Required] [Action]: The way the key and the value have to be compared:

Equal to (==)

Not equal (!=)

More than (>)

More than or equal to (>=)

Less than (<)

Less than or equal to(<=)

Regular Expression (RegExp)).

12. Value [Required] [Field] [Any]: Value to compare. Data type depends on the Type of data selected. See data types descrition for more details.

Note: For more information, go to Parameters, Functions.

	13. Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.

	14. Delete condition [Optional] [Action]: delete the condition line from the Condition Block.
	
	15. Add condition [Optional] [Action]: add a new condition line to the block.


## 16. New block [Optional] [Action]: add a new Condition Block to the node.
17. Paste [Optional] [Action]: paste the copied condition block. For at least one condition (key and value) specified in the block when pointing the cursor over the Drag Condition Block icon, the copy icon appears to the left. You can click this icon to copy the Condition Block and paste it to another one using the Paste button:


Screenshot 166: Condition block copy and paste.

Actions available in the Condition Block

You can do the following actions in the Condition Block:

Add a new condition: Below the Key field, click + Add condition, and then fill in the needed information in the condition line that appears.

Delete a condition: On the right side of the condition line, click the trash icon

Add a new Condition Block: Below the condition line, click + New block, and then fill in the needed information in the block that opens.

Copy a Condition Block: On the right side of the Condition Block, hover over the red/gray line, and then click the copy icon

Paste a Condition Block: In the lower-right corner of the panel, click Paste.

Screenshot 167: Condition block operations.

Examples

Adding one Condition block and one condition

In the examples below, we check if the condition is met: whether the value of the age parameter in the task is above 18:

Screenshot 168: Condition is met.

Screenshot 169: Condition is not met.

To pass a condition check, the task's parameters must meet the condition: if a task does not contain the age parameter, it fails to meet the condition.

Adding one Condition block with two Conditions

In the examples below, we check whether the two conditions of the Condition block are met:
whether the value of the age parameter in the task is above 18, and the value of the gender parameter is female:

Screenshot 170: Both conditions are met.

Screenshot 171: Only one condition is met.

If one block contains several conditions, all of them must be met for the block check to be considered true.

Adding two Condition blocks with one Condition in each

In the example below, the task's parameters are evaluated against two separate Condition blocks. Even though the conditions sets in both blocks are met, the task will only follow the output edge of the top block since it is the first one to be checked against.

Screenshot 172: Adding two blocks each with one condition.

You can access a single task parameter or a whole task stored in a State Diagram by Getting Task Parameters from State Diagrams.

Comparing objects in Condition blocks

In the example Process below, we use two Condition nodes in sequence to compare object data type parameters in the following objects with nested parameters: data_obj1, data_obj2 and mod_obj.

In-depth comparison

In Condition nodes, we can compare objects with as many nesting levels and parameters as we need, owing to the in-depth object comparison.

Screenshot 173: In-depth comparison of object in the Condition node.

First, we define the objects and their parameters in the task.

Screenshot 174: Objects comparison: defining parameters.

Then, we send the task to our Process. It passes through the first Condition node, where the check is performed for the data_obj1 and data_obj2 objects whether they are identical, and proceeds to the second Condition node. In the second Condition node, the data_obj1 and mod_obj1 are compared. As these objects are different, the task ends up in the final data_obj1 !=mod_obj node.

Screenshot 175: Objects comparison: result.

Error handling & troubleshooting

When working with your Process or State Diagram, you may encounter the following issues.

Table 4: Condition node issues.


### 3.4 Delay
Overview


Screenshot 176: Delay node view.


Manages workflow timing by pausing task progression.

Core Features

Introduces specified time delays in specified time measurement units

Schedules task execution

Controls workflow timing

Use Cases

Schedule task release at specific times (e.g., 7 PM)

Add processing intervals between steps

Automate time-dependent actions

Diagram 8: Delay node flow.

Node Settings

The Delay node has the following parameters:


Screenshot 177: Delay node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

Number of tasks in the queue [Optional/Required when 9 is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached. Set to 30 by default.

Maximum interval, for which the task stays in the node before being forwarded [Required] [Action]: The amount of time a task is allowed to be in the node can be set in seconds, minutes, hours, and days. Selected by default.

Maximum interval [Required] [Field] [Number]: The amount of time a task is allowed to be in the node. Has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval for which the task stays in the node before being forwarded:

Seconds

Minutes

Hours

Days.

Examples

Delaying a task by an x amount of time

Below, you can see the following examples:

Delaying a task for a time interval specified with an integer number. For example, you can use it in a Process for sending an email to your customers 30 minutes after they sign up for your service.

Screenshot 178: Delaying a task for specified amount of time.

Delaying a task for a time interval specified with Unix time: sending an email to your customers after a certain period of time after they sign up for your service.

Screenshot 179: Delaying a task for the Unix time-specified interval.

Delaying a task until a time specified with Unix time: sending an email to your customers at a certain time.

Screenshot 180: Delaying a task until the Unix time-specified moment.

Using dynamic timer for each task

Below, you can see the example where:

date variable is converted to Unixtime to be used in the Delay logic (the format is DD.MM.YYYY hh:mm:ss).

Screenshot 181: Delaying a task using the date variable converted to Unix time.

offset_GMT variable is used to adjust the Corezoid server time zone value.

Screenshot 182: Using offset_GMT variable to adjust the Corezoid server time zone value.

Error handling & troubleshooting

When working with your Process or State Diagram, you may encounter the following issues.

Table 5: Delay node issues.


