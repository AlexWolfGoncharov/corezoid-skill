<!-- Part of Corezoid docs. See docs/INDEX.md for full navigation. -->

### 3.10 Queue
Overview

Screenshot 219: Queue node view.

The Queue node enables you to temporarily hold a task until you are ready to process it. It is commonly used when tasks require manual intervention, such as when an employee needs to perform certain actions to process an order, such as contacting a client or preparing an order for shipment.
A workflow involving the Queue node consists of two Processes:

Includes the Queue node, which accumulates and holds all incoming tasks until they are ready for processing.

Involves the Get from Queue node, which is used to retrieve tasks when you are prepared to process them.

Diagram 14: Queue and Get from Queue nodes interaction flow.

Node Settings

The Queue node has the following parameters:


Screenshot 220: Queue node settings.

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

Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. See data types descrition for more details.

Code editor [Optional] [Action]: Shows the JSON format of the entered Key and Value. Click Code editor to open the code editor tab, where:

Screenshot 221: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 222: Code editor full-screen mode.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.

Delete key-value [Optional] [Action]: Delete the key-value pair.

Add key-value [Optional] [Action]: Add a new key-value pair.

To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon on the right side of the key-value line.

Screenshot 223: Key-value pair adding.

Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

Number of tasks in the queue [Required] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

Maximum interval [Required] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Using Queue and Get from Queue nodes together
In the example below, you can see how the Queue node in one Process and the Get from Queue node in another Process work together. The parameter specified in the Queue node is not added to the tasks until after they pass through that node. Two parameters are added to a task when it is released from the Get from Queue node:

queue_task_id: Contains the task ID of the stored task and is useful for tracking and identifying individual tasks as they are retrieved from the Queue node.

queue_task_data: Contains the task parameters of the stored task that include the data that the task originally had, as well as any additional parameters that were specified in the Queue node.

Screenshot 224: Using Queue and Get from Queue.

You can access a single task parameter or a whole task stored in a State Diagram by Getting Task Parameters from State Diagrams.

Error handling & troubleshooting

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 22: Error parameter names.

*The error tag __conveyor_queue_return_type_tag__ may have the following values.

Table 23: Queue node errors.


### 3.11 Get from Queue
Screenshot 225: Get from Queue node view.

Overview

The Get from Queue node enables you to retrieve tasks from any Queue node that you have set up in your Corezoid Processes.

Diagram 15: Queue and Get from Queue nodes interaction flow.

Node Settings

The Get from Queue node has the following parameters:


Screenshot 226: Get from Queue node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Alias or process with the Queue Node [Required] [Field/Action] [String]: Choose the Process or alias that contains the Queue node from which you want to take tasks by clicking the directory icon  or by specifying its Process ID or Alias.

Queue Node [Required] [Field/Action] [String]: Select the specific Queue node from the Process you’ve selected above.

Take From The Queue start/ Take From The Queue end [Required] [Action]: Choose whether to take tasks from the start or the end of the selected Queue node.

Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded is selected] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

Examples

Using the Get from Queue node to retrieve a task stored in the Queue node
See the example in Queue.

Error handling & troubleshooting

When an error occurs in the Get from Queue node, a task goes to the auxiliary Condition output node that is used for storing error parameters.

Screenshot 227: Get from Queue auxiliary debug node.

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 22: Error parameter names.

*The error tag __conveyor_get_task_return_type_tag__ may have the following values.

Table 23: Get from Queue node errors.


### 3.12 Copy Task
Overview

Screenshot 228: Copy Task node view.

The Copy Task node allows you to send a copy of a task to another Process. When you use the node, the task is essentially duplicated with one copy proceeding in the current Process and a new copy being passed to another Process. The two copies are independent of one another, but unlike the Call a Process node, the Copy Task node does not wait for a response from the other Process.

Diagram 16: Copy Task node flow.

Node Settings

The Copy Task node has the following parameters:

Screenshot 229: Copy Task node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Alias or process to which you want to copy the task [Required] [Field/Action] [String]: Choose the Process to which you would like to copy a task by clicking the directory icon  or by specifying its Process ID or Alias.

Reference of the task copy  [Optional] [Action]: Specify the reference identifier for the copied task.

Copy all task parameters to the new task [Optional] [Action]:

When selected: all current task parameters will be sent along with any parameters specified in the node.
When not selected: Only the parameters specified in the node will be sent.

Code editor [Optional] [Action]: Shows the JSON format of the entered Key and Value. Click Code editor to open the code editor tab, where:

Screenshot 230: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 231: Code editor full-screen mode.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets
To add a new parameter, specify a unique name, to update an existing parameter, use its original name as a key.

Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. 
See data types descrition for more details.

Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.

Delete key-value [Optional] [Action]: Delete the key-value pair.

Add key-value [Optional] [Action]: Add a new key-value pair.

To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon  on the right side of the key-value line.

18. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

19. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

20. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

21. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

22. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

23. Project [Required] [Field/Action] [String]: Choose the Project containing the Process to which you would like to copy a task by clicking the directory icon  or by specifying its Process ID, name or Alias.

Note: this parameter is available with the Alias or process to which you want to copy the task parameter and applies to Copy Task nodes created within Stages in Projects. This feature allows you to copy tasks to Processes located in Stages of different Projects.

24. Stage [Required] [Field/Action] [String]: Choose the Stage containing the Process to which you would like to copy a task by clicking the directory icon  or by specifying its Process ID, name or Alias.

Note: this parameter is available with the Alias or process to which you want to copy the task parameter and applies to Copy Task nodes created within Stages in Projects. This feature allows you to copy tasks to Processes located in Stages of different Projects.

Examples

Duplicating a task and adding a new parameter to the task copy

Description: Below, you can see the example where the Copy Task node is used to duplicate a task from the Original Process to the Destination Process.

Precondition:

Add the Copy Task node to your Original Process.

In Basic settings of the Copy Task node details panel, add:

The Destination Process you want to copy a task from.

The my_reference reference.

Select the Copy all task parameters to the new task checkbox.

In Parameters, add:

The Origin parameter.

The Hey, I’m from Copy value.

Screenshot 232: Copy task original and destination Processes.

Flow: After adding a task to the Original Process, you can see that the Copy Task node not only duplicates the original task parameters but also adds some new ones. These system parameters are automatically generated by the Copy Task node and help trace the relationship between the original and copied tasks:

copy_conv_id: Stores the ID of the Process (Original Process) from which the task was copied.

copy_node_id: Indicates the ID of the Copy Task node that created the copied task.

copy_ref_id: Stores the ID of the initial task from which the copy was created.

The task in the Original Process does not include the parameter that was defined within the Copy Task node but has the conveyor_copy_task_result parameter to keep track of whether the duplication was successful.

Screenshot 233: Tasks in Copy Task Original and Destination Processes.

You can access a single task parameter or a whole task stored in a State Diagram by Getting Task Parameters from State Diagrams.

Error handling & troubleshooting

When an error occurs in the Copy Task node, a task goes to the auxiliary Condition output node that is used for storing error parameters.

Screenshot 234: Copy Task auxiliary debug node.

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 23: Error parameter names.

*The error tag __conveyor_copy_task_return_type_tag__ may have the following values.

Table 24: Copy Task node errors.

When working with your Process or State Diagram, you may encounter the following issues.

Table 25: Copy Task node issues.


### 3.13 Call a Process
Overview

Screenshot 235: Call a Process node view.

The Call a Process node allows you to simplify and optimize workflows, making them more understandable and easier to maintain. You can increase efficiency by incorporating the logic and functionality of other Processes into your current Process. Simply select the desired Process from the catalog or specify its identifier – and the Call a Process node will send a task to that Process and receive the result.

Benefits of the Call a Process node:

Breaking complex Processes into simpler parts

Ability to reuse code without duplication

Isolation of Processes from each other

In the called Process, you must use the Process Response node. Without it, tasks will get stuck in the Call a Process node and won't be able to return a result – like a function in programming without a return statement.

Diagram 17: Call a Process node flow.

Avoid recursion by using Call a Process. Although it is technically possible to use the Reply to Process node within the same Process, we advise against it, but instead, it is better to use the Copy Task node.

Diagram 18: Two Processes interaction in Call a Process and Reply to Process scheme.

Node Settings

The Call a Process node has the following parameters:

Screenshot 236: Call a Process node settings.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Alias or process to call [Required] [Field/Action] [String]: Select the Process to call by clicking the directory icon  or by specifying its Process ID/Alias.

Send all parameters [Optional] [Action]: When the checkbox is selected: All current task parameters will be sent along with any parameters specified in the node.

When the checkbox is not selected: Only the parameters specified in the node will be sent.

11. Code editor [Optional] [Action]: Shows the JSON format of the entered Key and Value. Click Code editor to open the code editor tab, where:

Screenshot 237: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 238: Code editor full-screen mode.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

12. Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets
To add a new parameter, specify a unique name, to update an existing parameter, use its original name as a key.

13. Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. See data types descrition for more details.

14. Type of data [Required] [Action]: Selects the data type for the Value:
	* String (S)
	* Number (N)
	* Boolean (B)
	* Array (A)
	* Object (O)
	
	Note: For more information, go to Data types.


## 15. Delete key-value [Optional] [Action]: Delete the key-value pair.

## 16. Add key-value [Optional] [Action]: Add a new key-value pair.
To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon  on the right side of the key-value line. 

Screenshot 239: A key-value pair add.

17. Alert if the number of tasks in the node queue reaches the following number [Optional] [Action]: Helps monitor whether the number of tasks in the node exceeds the specified threshold.

18. Number of tasks in the queue [Optional/Required if Alert if the number of tasks in the node queue reaches the following number is selected] [Field] [Number]: Number of tasks in the queue which triggers an alert when reached.

19. Maximum interval, for which the task stays in the node before being forwarded [Optional] [Action]: Select to limit the time a task is allowed to be in the node in seconds, minutes, hours, and days.

20. Maximum interval [Optional/Required if Maximum interval, for which the task stays in the node before being forwarded] [Field] [Number]: The amount of time a task is allowed to be in the node. It has a minimum value of 30 seconds. You can set a shorter interval by using the Unixtime function.

21. Maximum interval measuring unit [Required] [Action]: Selects the measuring unit for the maximum interval:

Seconds

Minutes

Hours

Days.

22. Project [Required] [Field/Action] [String]: Choose the Project containing the Process which you would like to call by clicking the directory icon  or by specifying its Process ID, name or Alias.

Note: this parameter is available with the Alias or process to call parameter and applies to Call a Process nodes created within Stages in Projects. This feature allows you to call Processes located in Stages of different Projects.

23. Stage [Required] [Field/Action] [String]: Choose the Stage containing the Process which you would like to call by clicking the directory icon  or by specifying its Process ID, name or Alias.

Note: this parameter is available with the Alias or process to call parameter and applies to Call a Process nodes created within Stages in Projects. This feature allows you to call Processes located in Stages of different Projects.

Examples

Basic usage of the Call a Process node
Description: Below, you can see the example where the Call a Process node is used to send a task from the Call Process to the Reply Process that sends back a reply.

Precondition:

Add the Call a Process node to your Call Process.

In Basic settings of the Call a Process node details panel, add:

The Reply Process you want to call.

The call_param parameter.

The I was added in Call value.

Clear the Send all parameters checkbox.
Parameters can be sent when:

The Send all parameters checkbox is selected + no parameters: All parameters that are part of the original task are sent.

The Send all parameters checkbox is cleared + parameters: Only the specified parameters are sent. You can either create new parameters or send parameters that are part of the original task.

The Send all parameters checkbox is selected + parameters: The specified parameters are added to the original task parameters. If you specify a parameter with the same name as one of the task parameters, only the specified parameter will be sent.

The Send all parameters checkbox is cleared + no parameters: The option is not permitted; at least one parameter must be sent.

Add the Reply to Process node to the Reply Process you are going to call.

In Basic settings of the Reply to Process node details panel:

Add the reply_param parameter.

Add the I was added in Reply value.

Clear the Send all parameters checkbox.

Screenshot 240: Parameters in tasks in Call a Process and Reply to Process nodes.

Flow: Add a task with the original_task parameter and the I’m from the original task value to the Call Process. Once the task reaches the Call a Process node, it gets stuck in the node, a new task with the call_param and system parameters is created and sent to the Reply Process. After the new task enters the Reply to Process node of the Reply Process, a new task with the reply_param parameter is generated and sent back to the Call a Process node while the task that entered the node continues to move downstream. Once the task from the Reply to Process node is received in the Call a Process node, its parameters are merged with the original task parameters and added to the original_task and reply_param parameters.

Screenshot 241: Parameters in tasks in Call a Process and Reply to Process nodes.

You can access a single task parameter or a whole task stored in a State Diagram by Getting Task Parameters from State Diagrams.

Error handling & troubleshooting

When an error occurs in the Call a Process node, a task goes to the auxiliary Condition output node that is used for storing error parameters.

Screenshot 242: Auxiliary node for Call a Process errors handling.

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 26: Error parameter names.

*The error tag __conveyor_rpc_return_type_tag__ may have the following values.

Table 27: Call a Process node errors.

When working with your Process, you may encounter the following issues.

Table 28: Call a Process node issues.


### 3.14 Reply to Process
Overview

Screenshot 243: Reply to Process node view.

The Reply to Process node serves to send data back from the Process that was called by the Call a Process node. This node must be used in conjunction with the Call a Process node and cannot be used alone.

Diagram 19: Reply to Process node flow.

You can use the Reply to Process node to differentiate between valid and invalid responses by marking them later with the Throw exception checkbox. This will separate them into an error node.

Node Settings

The Reply to Process node has the following parameters:

Screenshot 244: Reply to Process parameters.

Title [Optional] [Field] [String]: Node title.

Description  [Optional] [Field] [String]: Node description.

Show more [Optional] [Action]: Long descriptions are reduced to a compact view to simplify node settings. Click to see the whole description.

Copy node [Optional] [Action]: Creates a copy of the current node with all settings.

Remove node [Optional] [Action]: Deletes current node from Process.

Remove links [Optional] [Action]: Removes all connections to/from current node.

Info [Optional] [Action]: Displays node ID.

Errors info [Optional] [Action]: Displays node errors.

Mode parameters [Required] [Action]: Select the format you can specify data in the node to send it to the parent Process:

Key-Value: specify Keys and their Values.

Keys: specify Keys only.

Throw exception [Optional] [Action]: When selected, notifies the main Process of an error. You can customize the notification by adding an error message.

Error message [Optional/Required if Throw exception is selected] [Field] [String]

Code editor [Optional] [Action]: Shows the JSON format of the entered Key and Value. Click Code editor to open the code editor tab, where:

Screenshot 245: Code editor tab.

Code editor field [Optional] [Field] [Any]: Enter new keys and values or edit the existing ones in JSON format.

Full-screen mode [Optional] [Action]: Opens the Code editor field in the full-screen mode, where:

Screenshot 246: Code editor full-screen mode.

Code editor field [Optional] [Field] [Any]: Edit or add keys in values.

Format code [Optional] [Action]: Format your current code.

Quit the full-screen mode [Optional] [Action]: Quit the full-screen mode.

Key [Required] [Field] [String]: Key to specify a static name or a variable in {{}} curly brackets
To add a new parameter, specify a unique name, to update an existing parameter, use its original name as a key.

Value [Required] [Field] [Any]: The value you want to assign to the corresponding Key parameter. 
See data types descrition for more details.
Note: is inactive when Keys is selected in Mode parameters.

You must specify at least one parameter:

To add a key-value, click + Add “key-value” below the Key field.

To delete the key-value line, click the trash icon  on the right side of the key-value line.

Screenshot 247: Adding Key and Value to the node.

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

Examples

Basic usage of the Reply to Process node
Description: In the example below, you can see the usage of two Reply to Process nodes in one Process.

Precondition:

Create the Reply Process with one Condition node and two Reply to Process nodes.

Create the Call Process with the Call a Process node that includes the call_param parameter.

Screenshot 248: Call Process and Reply Process Processes.

Flow:
The Condition node checks the value of the error parameter:

If the value is False, it leads it to the Reply to Process node that has the Throw an exception checkbox cleared.

Screenshot 249: Task movement from Call a Process to a Reply to Process.
The task is sent back to the connected Call a Process node and has the parameters that were listed in the Reply to Process node.

Screenshot 250: Task return to the Call a Process.

If the value is True, the task is routed to the Reply to Process node that has the Throw an exception checkbox selected and an error message.

Screenshot 251: Throw exception box selected.

The task goes to the Error node of the Call Process and has all the typical error handling parameters, the error message specified before, along with the reply_param value.

Screenshot 252: Task is forwarded to the Error node.

No matter which parameters the task has when entering the Reply to Process node, only the parameters listed in the node will be sent back.

Error handling & troubleshooting

When an error occurs during the task processing, you may see the following error parameter names in the task.

Table 29: Error parameter names.

*The error tag __conveyor_rpc_reply_return_type_tag__ may have the following values.

Table 30: Reply to Process node errors.


