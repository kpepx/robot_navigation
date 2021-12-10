# FRA502 Service Robot: Phase 3
Krittapak Jakparinyakul 61340500002
Name Project: หุ่นยนต์นำทางไปยังห้องประชุม

หุ่นยนต์จะทำหน้าที่นำทางไปยังห้องประชุมต่าง ๆ โดยการสั่งงานด้วยเสียงกับตัวหุ่นยนต์ เพื่อบอกห้องประชุมที่จะให้หุ่นยนต์นำทางไป และเมื่อหุ่นยนต์นำทางถึงเป้าหมาย หุ่นยนต์จะกลับมาสู่ตำแหน่ง ้home ที่หุ่นยนต์อยู่ เพื่อใช้อำนวยความสะดวกให้กับผู้ที่มาร่วมประชุม ไม่เสียเวลาในการเดินหาห้อง

# Environment
* OS: Ubuntu 20.04.3 LTS
* ROS: Noetic Ninjemys
* Gazebo: 

# How to run
คำสั่งเพื่อเปิด Gazabo
```
roslaunch robot_navigation testworld.launch
```
คำสั่งเพื่อเปิด Rviz
```
roslaunch robot_navigation robot_navigation.launch
```
คำสั่งเพื่อสั่งงานด้วยเสียงกับหุ่นยนต์
```
rosrun robot_navigation voice_control.py
```
