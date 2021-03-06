# FRA502 Service Robot: Phase 3
Krittapak Jakparinyakul 61340500002
Name Project: หุ่นยนต์นำทางไปยังห้องประชุม

หุ่นยนต์จะทำหน้าที่นำทางไปยังห้องประชุมต่าง ๆ โดยการสั่งงานด้วยเสียงกับตัวหุ่นยนต์ เพื่อบอกห้องประชุมที่จะให้หุ่นยนต์นำทางไป และเมื่อหุ่นยนต์นำทางถึงเป้าหมาย หุ่นยนต์จะกลับมาสู่ตำแหน่ง home ที่หุ่นยนต์อยู่ เพื่อใช้อำนวยความสะดวกให้กับผู้ที่มาร่วมประชุม ไม่เสียเวลาในการเดินหาห้อง

# Environment
* OS: Ubuntu 20.04.3 LTS
* ROS: Noetic Ninjemys
* Gazebo: 11.9

# Package
* actionlib
* amcl
* gazebo_ros
* geometry_msgs
* map_server
* move_base_msgs
* pyaudio
* rospy
* rviz
* speech_recognition
* std_msgs

# How to run
เริ่มรันจาก
```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
คำสั่งเพื่อเปิด Gazabo
```
roslaunch robot_navigation testworld.launch
```
คำสั่งเพื่อเปิด Rviz
```
roslaunch robot_navigation robot_navigation.launch
```
จากนั้นให่เปิด Rviz และใช้ 2D Pose Estimate ให้หุ่นยนต์อยู่ในตำแหน่งในภาพ
![Screenshot from 2021-12-10 16-30-32](https://user-images.githubusercontent.com/57758268/145551135-60ad262c-2a7a-47e3-9f24-84cdaec671e4.png)
คำสั่งเพื่อสั่งงานด้วยเสียงกับหุ่นยนต์
```
python3 ~/catkin_ws/src/robot_navigation/scripts/voice_control.py
```
# How to create map
คำสั่งเพื่อเปิด Gazabo
```
roslaunch robot_navigation testworld.launch
```
คำสั่งเพื่อสร้างแผนที่
```
roslaunch robot_navigation robot_navigation_slam.launch slam_methods:=gmapping
```
จะดึงการควบคุมจาก turtlebot3 มา
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
เมื่อสร้างแผนที่เสร็จ ถ้าต้องการบันทึก
```
rosrun map_server map_saver -f ~/catkin_ws/src/robot_navigation/map/maps
```

# How to use voice to control robot
การสั่งงานเป็นภาษาอังกฤษ (English) โดยเมื่อเจอคำประโยค

- Choose the meeting room you will go to?
- You can select: meeting room 10 - meeting room 60

การทำงาน หุ่นยนต์กำลังรอรับคำสั่งเสียง ให้สั่งงานด้วยเสียงพูด ตัวอย่างเช่นอยากไปห้องประชุม 10 ให้ใช้คำสั่งเสียง "meeting room 10" หุ่นยนต์จะตอบกลับมา "meeting room 10. I have recieve command." และ "Follow me going to meeting room 10." หุ่นยนต์จะนำทางไปยังห้องประชุม 10 เมื่อถึงห้องประชุม หุ่นยนต์จะตอบกลับมา "You have arrived at the meeting room. I will go home, Goodbye..." จากนั้นหุ่นยนต์จะกลับไปยังตำแหน่ง home และรอรับคำสั่งต่อไป จะมี state การทำงานซ้ำตามที่กล่าวมา

# Problem
* เมื่อใส่ model โต๊ะ เก้าอี้ ที่จะใช้ทำห้องประชุม จะไม่สามารถเปิด world ที่ save ไว้ขึ้นมาได้ เนื่องจาก Gazebo ค้าง ทำงานต่อไปไม่ได้ จึงเปลี่ยน model เป็นสี่เหลี่ยม และทรงกระบอก เพื่อแก้ปัยหาให้สามารถเปิดและทำงานส่วนอื่นต่อไปได้
* เมื่อหุ่นยนต์เช้าถึงตำแหน่งเป้าหมาย บางครั้งหุ่นยนต์จะหมุนรอบตัวเองหลายรอบ เพื่อหาตำแหน่งที่เหมาะสม ในการหยุด
* เมื่อสั่งงานด้วยเสียงบางครั้ง ตัวโปรแกรมประมวลผลช้า ทำให้บางครั้งต้องรอนาน หรือต้องสั่งหุ่นยนต์หลายรอบ
