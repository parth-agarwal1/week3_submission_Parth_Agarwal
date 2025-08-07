

# Week 3 Submission - Parth Agarwal

This repository contains solutions to all four questions from the Week 3 ROS 2 assignment.

---

## Q1: Talker and Listener

- **Files**: `q1_talker.py`, `q1_listener.py`
- The **talker** node publishes messages to a topic at a rate of **15 messages/second**.
- The **listener** node subscribes to that topic and prints any received messages to the console.

---

## Q2: Alternate Color Publisher & Conditional Publisher

- **Files**: `q2_alternate.py`, `q2_conditional.py`
- `q2_alternate` publishes `"green"` and `"red"` alternately to the `/s1` topic, switching every **10 seconds**.
- `q2_conditional` subscribes to `/s1` and publishes the **opposite color** to the `/s2` topic.

---

## Q3: Custom Message Publisher

- **File**: `q3_custom_message.py`
- Publishes an example **custom `RoverStatus` message**, which contains:
  - Velocity (`geometry_msgs/Twist`)
  - Distance traveled
  - Current position (`geometry_msgs/Pose`)
  - Battery level
  - Time taken (`builtin_interfaces/Duration`)
- Demonstrates how to use and log custom message types in ROS 2.

---

## Q4: Clock Publisher

- **File**: `q4_clock.py`
- A single node publishes simulated time on four topics:
  - `/second`
  - `/minute`
  - `/hour`
  - `/clock`
- The `/second` count increments every second.
- Every time `/second` hits 60, `/minute` increments and `/second` resets.
- Similarly, `/hour` increments every time `/minute` reaches 60.
- The `/clock` topic publishes the full time in **HH:MM:SS** format.
- Only the `/clock` topic is **logged**, so the others may not appear in `rqt_graph`.

<img width="588" height="223" alt="Screenshot from 2025-08-08 00-11-16" src="https://github.com/user-attachments/assets/de982c9e-4f05-451c-b776-ab2f0f6e9f27" />
