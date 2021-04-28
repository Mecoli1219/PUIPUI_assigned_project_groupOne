/***************************************************************************/
// File			  [node.h]
// Author		  [Erik Kuo, Joshua Lin]
// Synopsis		[Code for managing car movement when encounter a node]
// Functions  [/* add on yout own! */]
// Modify		  [2020/03/027 Erik Kuo]
/***************************************************************************/

#include <SoftwareSerial.h>
#include <Wire.h>
/*===========================import variable===========================*/
int extern rr, r, m, l, ll;
int extern _Tp;
int extern MotorL_I1;
int extern MotorL_I2;
int extern MotorR_I3;
int extern MotorR_I4;
int extern MotorL_PWML;
int extern MotorR_PWMR;
int time_for_rotate = 2000;
/*===========================import variable===========================*/

// TODO: add some function to control your car when encounter a node
// here are something you can try: left_turn, right_turn... etc.
void do_ADVANCE()
{
    tracking(ll, l, m, r, rr);
}

void do_TURN_RIGHT()
{
    digitalWrite(MotorL_PWML, HIGH);
    digitalWrite(MotorR_PWMR, HIGH);
    digitalWrite(MotorL_I1, HIGH);
    digitalWrite(MotorL_I2, LOW);
    digitalWrite(MotorR_I3, LOW);
    digitalWrite(MotorR_I4, HIGH);
    delay(time_for_rotate);
}

void do_TURN_LEFT()
{
    digitalWrite(MotorL_PWML, HIGH);
    digitalWrite(MotorR_PWMR, HIGH);
    digitalWrite(MotorL_I1, LOW);
    digitalWrite(MotorL_I2, HIGH);
    digitalWrite(MotorR_I3, HIGH);
    digitalWrite(MotorR_I4, LOW);
    delay(time_for_rotate);
}

void do_HALT()
{
    digitalWrite(MotorL_PWML, LOW);
    digitalWrite(MotorR_PWMR, LOW);
}
void do_command(BT_CMD cmd)
{
    if (cmd == 1)
    {
        do_ADVANCE();
    }
    if (cmd == 2)
    {
        do_TURN_LEFT();
        do_TURN_LEFT();
    }
    if (cmd == 3)
    {
        do_TURN_RIGHT();
    }
    if (cmd == 4)
    {
        do_TURN_LEFT();
    }
    if (cmd == 5)
    {
        do_HALT();
    }
}
