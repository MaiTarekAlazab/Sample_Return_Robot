#include <objectsub.h>
objectsub::objectsub(ros::NodeHandle& nodeHandle) :
    nodeHandle_(nodeHandle)
{
    objectsubscriber= nodeHandle_.subscribe("object_pos", 1000, &objectsub::objectCallback,this);
}
void objectsub::objectCallback(const PointStamped& msg){
    x=msg.point[1];
    y=msg.point[2];

}
float objectsub::getx(){
    return x;
}
float objectsub::gety(){
    return y;
}
