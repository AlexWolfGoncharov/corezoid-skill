<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

### 3.15 Set State
Overview

The Set State node is used for a State Diagram only.

Screenshot 253: Set State node view.


The Set State node is designed to store tasks and control their flow through a State Diagram. It allows you to keep a task within the node until there is the task modification request and certain condition is met after which it is forwarded to the next node associated with that condition. In a way, the Set State node in a State Diagram combines the functionality of the Condition and Waiting for Callback nodes found in Processes.
The general flow:

A task enters Set State node and waits for a modification.

Waits for any type of modification:

Manual

API

Modify Task node

Any modification triggers parameters check:

Compares current parameters with conditions

The task moves forward when:

Any modification occurred

Parameters match conditions

Returns to wait if no match

Note: Initial parameter match on entry doesn't trigger forwarding. Only modification + condition match enables forwarding.

Diagram 20: Set State task forwarding logic.

In a State Diagram, you have the flexibility to manage tasks from outside the Diagram by using:

Modify Task node

API Call node

Manually created or imported tasks in the View mode

Diagram 21: Set State node flow.

Modify Task Interaction:

Starts with Modify Task node

Flows to Set State

Conditions check with decision point

Proceeds to Next Node or returns to Set State

API Call Interaction:

Initiates with API Call

Moves to Set State

Evaluates conditions

Advances or remains in Set State

View Mode Interaction:

Begins with manual task creation

Enters Set State

Checks conditions

Continues or stays in Set State

Node Settings

The Set State node has the following parameters:

Screenshot 254: Set State node settings.

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


Screenshot 255: Condition copy and paste.

Actions available in the Condition Block

You can do the following actions in the Condition Block:

Add a new condition: Below the Key field, click + Add condition, and then fill in the needed information in the condition line that appears.

Delete a condition: On the right side of the condition line, click the trash icon

Add a new Condition Block: Below the condition line, click + New block, and then fill in the needed information in the block that opens.

Copy a Condition Block: On the right side of the Condition Block, hover over the red/gray line, and then click the copy icon

Paste a Condition Block: In the lower-right corner of the panel, click Paste.

Delete a Condition Block: On the right side of the Condition Block, hover over the red/gray line, and then click the trash icon  that appears.

Screenshot 256: Condition block operations.

The Set State node does not necessarily have to contain a condition. If it does not have a condition, the tasks will stay in it forever.

18. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

19. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

20. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

21. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a default value of 86400 seconds. You can set a shorter interval manually or by using the Unixtime function.

22. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Storage
Description: In the example below, you can see how to safely store any values you might need to run your Processes, such as login and password, within the Set State node.

Precondition:

Create a State Diagram.

Add the Set State node.

Add tasks with sensitive parameters.

Flow: You can refer to sensitive parameters when you need to use them in other State Diagrams, without revealing their actual value.

Screenshot 257: Set State use for storage.

Reacting to task parameters changes
Description: In the example below, you can see how the Set State node handles and modifies the received tasks.

Precondition:

Create a State Diagram.

Add the Set State node.

In the Condition block of the Set State node, add the Status key and the Inactive value.

Flow:

The condition is met.

Screenshot 258: Set State use-condition is met.

The condition is not met.

Screenshot 259: Set State use-condition is not met.

Error handling & troubleshooting

When working with your State Diagram, you may encounter the following issues.

Table 31: Set State node issues.


### 3.16 Waiting for Callback
Overview

Screenshot 260: Waiting for Callback node view.

The Waiting for Callback node is used for a Process only.

The Waiting for Callback node suspends task processing until receiving a response. It's primarily used when waiting for user actions - for example, when a chatbot awaits user input.

Like the Set State node, tasks remain in the Waiting for Callback node until modified or expired. However, while Set State requires specific conditions to be met, Waiting for Callback releases the task upon any modification.

Ways to trigger a callback:

Manual task creation in View mode

Modify Task node action

Corezoid API call

Callback URL request

Diagram 22: Waiting for Callback node flow.


Corezoid API vs Request to Callback URL:

Corezoid API provides a code-based framework for performing UI operations within a specified format. For more information, go to Corezoid API.

Callback URL is the API request made specifically to the URL provided within the Waiting for Callback node. This method is recommended for replying to tasks from outside Corezoid.

Node Settings

The Waiting for Callback node has the following parameters:

Screenshot 261: Set State node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Corezoid [Required] [Field] [String]: Callback URL for an API call.

Copy [Optional] [Action]: Click to copy the Corezoid URL.

Mandrill [Required] [Field] [String]: Is a legacy feature, a Callback URL that allows you to receive callbacks directly from Mandrill.

Copy [Optional] [Action]: Click to copy the Mandrill URL.

Path to task ID [Optional] [Field] [String]: Displays called task ID in API Call parameters.

Synchronous [Optional] [Action]:

Returns error task_not_in_current_sync_callback_node if task not found in current node during Callback URL request.

When disabled, request succeeds regardless of task location.

15. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

16. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

17. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

18. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds and default value of 1 day. You can set a shorter interval by using the Unixtime function.

19. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Manually modified task
In the example below, you can see how the task is modified manually.

Screenshot 262: Manually modified task in the Waiting for Callback node.

The Modify button in the task window is available in the Archive tab that opens the New Task dialog.

Screenshot 263: A task in the Waiting for Callback node’s archive.

Task modified in Modify Task node
In the example below, you can see a task modified with the Waiting for Callback node by using the Modify Task node in another Process.

Screenshot 264: A task modified in the Modify Task node.

Task modified by Corezoid API
In the example below, a task was modified with Corezoid API by using the Waiting for Callback node.

Screenshot 265: A task modified in the Corezoid API.

You can use the following request body with the task_id parameter instead of ref for your requests.

{

"ops": [

{

"type": "modify",

"obj": "task",

"ref": "test_ref",

"conv_id": "259715",

"data": {

"new_param": "test"

}

}]}

Task modified by Callback URL
In the example below, you can see the task modified by submitting the POST request to the URL provided within the Waiting for Callback node.

Screenshot 266: A task modified by the Callback URL.

Example request is sent in Postman.

Error handling & troubleshooting

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 32: Error parameter names.

*The error tag __conveyor_callback_return_type_tag__ may have the following values.

Table 33: Waiting for Callback node errors.


### 3.17 Modify Task
Overview


Screenshot 267: Modify Task node view.

The Modify Task node updates parameters of tasks in other Processes without disrupting their workflow. Common use cases:

Updating tasks in Waiting for Callback nodes to trigger their progression

Adjusting task parameters in Set State nodes to influence their path through State Diagrams

Diagram 23: Modify Task node flow.

You can only modify tasks that are in the Waiting for Callback or Set State nodes.

Settings

The Modify Task node has the following parameters:

Screenshot 268: Modify Task node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Alias or Process in which you want to modify the task [Required] [Field/Action] [String]: Select Process via directory icon  or enter Process ID or Alias.

Reference of the task you want to modify [Option] [Field/Action] [String]: Specify identifier for task modification.

Copy all task parameters to the new task [Optional] [Action]:

When selected: Sends all current task parameters plus node-specified parameters.

When not selected: Sends only node-specified parameters.

Code editor [Optional] [Action]: Shows the JSON format of the entered Key and Value. Click Code editor to open the code editor tab, where:

Screenshot 269: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 270: Code editor full-screen view.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets
To add a new parameter, specify a unique name, to update an existing parameter, use its original name as a key.

Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. 
See data types descrition for more details.

To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon  on the right side of the key-value line.

Screenshot 271: Add a key-value pair.

15. Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.


## 16. Delete key-value [Optional] [Action]: Delete the key-value pair.

## 17. Add key-value [Optional] [Action]: Add a new key-value pair.
18. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

19. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

20. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

21. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

22. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.


## 23. Synchronous callback [Optional] [Action]:
The checkbox is selected: Updates tasks sequentially, checking whether it is being modified in another Modify task node.

The checkbox is not selected: Only checks if task exists in the Process.

Note: Works only for tasks in Waiting for Callback or Set State nodes. Otherwise, returns no_api_callback_in_node_with_task error.

24. Project [Required] [Field/Action] [String]: Choose the Project containing the Process in which you would like to modify a task by clicking the directory icon  or by specifying its Process ID, name or Alias.

Note: this parameter is available with the Alias or process in which you want to modify the task parameter and applies to Modify Task nodes created within Stages in Projects. This feature allows you to modify tasks in Processes located in Stages of different Projects.

25. Stage [Required] [Field/Action] [String]: Choose the Stage containing the Process in which you would like to modify a task by clicking the directory icon  or by specifying its Process ID, name or Alias.

Note: this parameter is available with the Alias or process in which you want to modify the task parameter and applies to Modify Task nodes created within Stages in Projects. This feature allows you to modify tasks in Processes located in Stages of different Projects.

Examples

Modifying a task in the Waiting for Callback node

Description: In the example below, you can see how the I’m waiting task parameter is changed by I’m from modify.

Precondition:

Create a Process or a State Diagram, and add the Waiting for Callback node.

On the Waiting for Callback node details panel, add the param parameter, the I’m waiting value, and the ref1 reference.

Create a Process and add the Modify Task node.

In Basic settings of the Modify Task node details panel, add the Waiting for Callback node, the ref1 reference, the param parameter, and the I’m from modify value.

Screenshot 272: Modify Task and Waiting for Callback nodes combined use.

Flow: The task passes through the Modify Task node and gets a new parameter indicating the status of the modification. In this example, it is the ok value. When the modified task returns to the Waiting for Callback node, its parameter changes from I'm waiting to I'm from modify, reflecting the changes specified in the Modify Task node. System parameters are added to the task, so you can track where this modification came from.

Screenshot 273: Task parameters in Modify Task and Waiting for Callback nodes.

You can access a single task parameter or a whole task stored in a State Diagram by Getting Task Parameters from State Diagrams.

Error handling & troubleshooting

When an error occurs in the Modify Task node, a task goes to the auxiliary Condition output node that is used for storing error parameters.

Screenshot 274: Modify Task auxiliary debug node.

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 34: Error parameter names.

*The error tag __conveyor_modify_task_return_type_tag__ may have the following values.

Table 35: Modify Task node errors.


### 3.18 Sum
Overview

Screenshot 275: Sum node view.

The Sum node:

Calculates and accumulates totals from specified task parameters

Tracks parameter statistics

Integrates with other nodes for workflow analytics

Diagram 24: Sum node flow.

Unlike other nodes, in the Sum node, the total value is not added to the tasks but is stored within the node itself.

Node Settings

The Sum node has the following parameters:


Screenshot 276: Sum node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets
To add a new parameter, specify a unique name, to update an existing parameter, use its original name as a key.

Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. 
See data types descrition for more details.

Note: For more information, go to Parameters, Functions.

To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon  on the right side of the Value field.

Screenshot 277: A key-value pair add.

Sum ID [Optional] [Action]: Click to view the Sum ID.

Delete key-value [Optional] [Action]: Delete the key-value pair.

Add key-value [Optional] [Action]: Add a new key-value pair.

Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Using the Sum node as a counter

Description: In the example below, you can see how to use the Sum node as a counter.

Precondition:

Add the Sum node to your Process.

In Summation Parameters of the Sum node details panel, add the Count parameter and the 1 value (a positive or negative number).

Flow: Each time a task passes through the Sum node, the Counter value increases by 1, effectively counting the number of tasks that have passed through the node.

Such a counter can be used to monitor the number of payments or charges on an account or to record different types of payments/multiple accounts.

Screenshot 278: Sum node counter.

You can view the current Counter value on a Dashboard or access its value in a Process or a State Diagram.

Summing up a parameter

Description: In the example below, you can see how to use the Sum node to calculate a parameter value.

Precondition:

Add the Sum node to your Process or State Diagram.

In Summation Parameters of the Sum node details panel, add the Payment_total parameter and the {{amount}} value (as a variable).

Screenshot 279: Summation parameters.

Flow: Each time a task passes through the Sum node, the Sum node tracks and accumulates the values of the {{amount}} task parameter, calculates the total, and stores it in the Payment_total parameter.

You can sum multiple task parameters within the Sum parameter by using the $.math({{param1}}+{{param2}}) math function.

Error handling & troubleshooting

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 36: Error parameter names.

*The error tag __conveyor_api_sum_return_type_tag__ may have the following values.

Table 37: Sum node errors.

When working with your Process, you may encounter the following issues.

Table 38: Sum node issues.


### 3.19 Parallel Processing Node (Coming Soon)

