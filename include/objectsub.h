#ifndef objectsub_H
#define objectsub_H

#include <ros/ros.h>
#include <geometry_msgs/PointStamped.h>
//#include <PointStamped>
#include <iostream>


class objectsub
{
public:
    objectsub(ros::NodeHandle& nodeHandle);
    float getx();
    float gety();

private:
    ros::NodeHandle nh_;
    ros::Subscriber objectsubscriber;
    void objectCallback(const PointStamped& msg);
    float x=0;
    float y=0;
    
};

#endif



