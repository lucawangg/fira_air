#============================================================================

from djitellopy import tello
import cv2
import numpy as np
import time
import logging
import at

#============================================================================

tag_list = [3,4]

#============================================================================

robot = tello.Tello()
robot.LOGGER.setLevel(logging.ERROR)
robot.connect() 
robot.streamon()
robot.takeoff()
time.sleep(3)

#============================================================================

state = 'TAG'
tag_now = 0

while True:
    img = cv2.resize(cv2.cvtColor(robot.get_frame_read().frame , cv2.COLOR_RGB2BGR), [960,720])
    tags = at.get_tags(img)
    img_debug = img.copy()
    height = robot.get_height()

    #----------------------------------------------
    err_x = 0
    err_y = 0
    err_dist = 0
    err_angle = 0
    motor_x = 0
    motor_y = 0
    motor_dist = 0
    motor_angle = 0
    #---------------------------------------------- GOTO TAG

    if state == 'TAG':
        seen = False

        for tag in tags:
            if tag[0] == tag_list[tag_now]:

                err_x = tag[1]
                if err_x > 30: motor_x = 20
                elif err_x < -30: motor_x = -20
                else: motor_x = 0

                err_y = 0-tag[2]
                if err_y > 30: motor_y = 20
                elif err_y < -30: motor_y = -20
                else: motor_y = 0

                err_dist = tag[3] - 50
                if err_dist > 30: motor_dist = 20
                elif err_dist < -30: motor_dist = -20
                else: motor_dist = 0

                err_angle = tag[4]
                if err_angle > 30: motor_angle = 20
                elif err_angle < -30: motor_angle = -20
                else: motor_angle = 0

                robot.send_rc_control(int(motor_x),int(motor_dist),int(motor_y),int(motor_angle))

                seen = True
                break

        if seen == False:
            robot.send_rc_control(0,0,0,0)              
            state = 'SEARCH'
            print('SEARCH MODE')
                
        else:
            #.............
            if motor_x == 0 and motor_y == 0 and motor_dist == 0 and motor_angle == 0:
                robot.send_rc_control(0,0,0,0)
                print('BORO TUUU')
                
                robot.move_up(30)
                robot.move_forward(150)
                
                tag_now += 1
                if tag_now >= len(tag_list):
                    robot.land()
                    break
            #.............
        
        


    #---------------------------------------------- SEARCH MODE


    elif state == 'SEARCH':
        seen = False
        for tag in tags:
            if tag[0] == tag_list[tag_now]:
                seen = True
                break

        if seen == True:
            robot.send_rc_control(0,0,0,0)
            state = 'TAG'
            print('TAG FOUND')


    #---------------------------------------------- SHOW IMAGE


    cv2.imshow('img', img_debug)
    key = cv2.waitKey(1)
    if key == ord('e'):
        break

robot.land()
