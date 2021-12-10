#! /usr/bin/python3
import speech_recognition as sr
import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

voice = sr.Recognizer()

meeting = False
home = False

def command_voice():
    txt_voice = ""

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    if not meeting:
        rospy.loginfo("Choose the meeting room you will go to?")
        rospy.loginfo("You can select: meeting room 10 - meeting room 60")
        try:
            with sr.Microphone() as source:
                voice.adjust_for_ambient_noise(source, duration=0.5)
                audio_listen = voice.listen(source, timeout=5.0)

            txt_voice = voice.recognize_google(audio_listen)
            txt_voice = txt_voice.lower()

            rospy.loginfo(txt_voice + ". I have recieve command.")

        except sr.UnknownValueError:
            rospy.loginfo("Please say again.")

        except sr.RequestError as e:
            rospy.loginfo("Could not request results; {0}".format(e))
    else:
        txt_voice = "home"

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    if home:
        txt_voice = "complete"
        rospy.loginfo("You have arrived at the meeting room. I will go home, Goodbye...")
        goal.target_pose.pose.position.x = -0.053448
        goal.target_pose.pose.position.y = -0.76843
        goal.target_pose.pose.orientation.z = 0.00000
        goal.target_pose.pose.orientation.w = 1.00000
        client.send_goal(goal)
    else:
        if '10' in txt_voice:
            txt_voice = "1"
            rospy.loginfo("Follow me going to meeting room 10.")
            goal.target_pose.pose.position.x = 1.88361
            goal.target_pose.pose.position.y = -6.24199
            goal.target_pose.pose.orientation.z = 0.00000
            goal.target_pose.pose.orientation.w = 1.00000
            client.send_goal(goal)

        elif '20' in txt_voice:
            txt_voice = "2"
            rospy.loginfo("Follow me going to meeting room 20.")
            goal.target_pose.pose.position.x = 4.80985
            goal.target_pose.pose.position.y = -1.26030
            goal.target_pose.pose.orientation.z = 0.00000
            goal.target_pose.pose.orientation.w = 1.00000
            client.send_goal(goal)

        elif '30' in txt_voice:
            txt_voice = "3"
            rospy.loginfo("Follow me going to meeting room 30.")
            goal.target_pose.pose.position.x = 4.71645
            goal.target_pose.pose.position.y = 0.73284
            goal.target_pose.pose.orientation.z = 0.00000
            goal.target_pose.pose.orientation.w = 1.00000
            client.send_goal(goal)

        elif '40' in txt_voice:
            txt_voice = "4"
            rospy.loginfo("Follow me going to meeting room 40.")
            goal.target_pose.pose.position.x = 2.13262
            goal.target_pose.pose.position.y = 6.34936
            goal.target_pose.pose.orientation.z = 0.00000
            goal.target_pose.pose.orientation.w = 1.00000
            client.send_goal(goal)

        elif '50' in txt_voice:
            txt_voice = "5"
            rospy.loginfo("Follow me going to meeting room 50.")
            goal.target_pose.pose.position.x = -3.80442
            goal.target_pose.pose.position.y = 0.59250
            goal.target_pose.pose.orientation.z = 0.00000
            goal.target_pose.pose.orientation.w = 1.00000
            client.send_goal(goal)

        elif '60' in txt_voice:
            txt_voice = "6"
            rospy.loginfo("Follow me going to meeting room 60.")
            goal.target_pose.pose.position.x = -3.86585
            goal.target_pose.pose.position.y = -3.28640
            goal.target_pose.pose.orientation.z = 0.00000
            goal.target_pose.pose.orientation.w = 1.00000
            client.send_goal(goal)

    wait = client.wait_for_result()
    if wait:
        return txt_voice


if __name__ == '__main__':
    rospy.init_node('movebase_client_py')
    while(True):
        txt_output = command_voice()
        if txt_output == "home":
            #rospy.loginfo("In home")
            home = True
            meeting = False
        elif(txt_output == "1" or txt_output == "2" or txt_output == "3" or txt_output == "4" or txt_output == "5" or txt_output == "6"):
            meeting = True
            home = True
            #rospy.loginfo("In meeting")
        elif txt_output == "complete":
            #rospy.loginfo("complete")
            home = False
            meeting = False

        