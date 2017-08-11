# Node: [fsm_node.py](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/fsm/src/fsm_node.py)
finite-state machine realization

## Parameters
FSM specified in the [configuration file](https://github.com/OSLL/Duckietown-Software/tree/master/catkin_ws/src/duckietown/config/baseline/fsm/fsm_node)
* `~states`:
    states description such as: transitions rules, active nodes, lights configs 
* `~global_transitions`:
    global transitions, available from all states
* `~initial_state`:
    initial state of fsm
* `~nodes`:
    mapping from node names in fsm to ros switch topics for every node (using to switch on/off nodes) 
* `~events`:
    mapping from ros topic msgs to fsm events

## Subscribe Topics
* Subscribes to all topic in `~events` list; [duckietown_msgs/BoolStamped.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/BoolStamped.msg) 

## Publish Topics
* `~mode`: [duckietown_msgs/FSMState.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/FSMState.msg), publish fsm state when it's changing
* Publish to all `~nodes` topics; [duckietown_msgs/BoolStamped.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/BoolStamped.msg) 

## Services
* `~set_state`: [SetFSMState.srv](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/srv/SetFSMState.srv), sets fsm state

# Node: [logic_gate_node.py](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/fsm/src/logic_gate_node.py)
Using for switch "parallel_autonomy" and "not_parallel_autonomy" mode when intersection traversal is done

## Parameters
Specified in the [configuration file](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown/config/baseline/fsm/logic_gate_node/default.yaml)
* `~gates`:
    Descripts 
* `~events`:

## Subscribe Topics
* Subscribes to all topic in `~events` list; [duckietown_msgs/BoolStamped.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/BoolStamped.msg) 

## Publish Topics
* `~mode`: [duckietown_msgs/FSMState.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/FSMState.msg), publish fsm state when it's changing
* Publish to all `~nodes` topics; [duckietown_msgs/BoolStamped.msg](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/msg/BoolStamped.msg) 

## Services
* `~set_state`: [SetFSMState.srv](https://github.com/OSLL/Duckietown-Software/blob/master/catkin_ws/src/duckietown_msgs/srv/SetFSMState.srv), sets fsm state
