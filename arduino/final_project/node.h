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
int extern rr, r, m, l, ll, M, L, LL, R, RR;
int extern _Tp;
int extern MotorL_I1;
int extern MotorL_I2;
int extern MotorR_I3;
int extern MotorR_I4;
int extern MotorL_PWML;
int extern MotorR_PWMR;
int time_for_rotate = 270;
/*===========================import variable===========================*/

// TODO: add some function to control your car when encounter a node
// here are something you can try: left_turn, right_turn... etc.
void do_ADVANCE()
{
    int times = 0;
    while(times <= 20){
      ll = digitalRead(LL);
      l = digitalRead(L);
      m = digitalRead(M);
      r = digitalRead(R);
      rr = digitalRead(RR);
      if(tracking_advance(ll,l,m,r,rr)){
        times ++;
      }else{
        times = 0;
      }
    }
}

void do_TURN_RIGHT()
{
    analogWrite(MotorL_PWML, 255);
    analogWrite(MotorR_PWMR, 150);
    digitalWrite(MotorL_I1, LOW);
    digitalWrite(MotorL_I2, HIGH);
    digitalWrite(MotorR_I3, HIGH);
    digitalWrite(MotorR_I4, LOW);
    delay(800);
    analogWrite(MotorL_PWML, 100);
    analogWrite(MotorR_PWMR, 100);
    while(digitalRead(M) != 1);
    digitalWrite(MotorL_PWML, LOW);
    digitalWrite(MotorR_PWMR, LOW);
    do_ADVANCE();
}

void do_TURN_LEFT()
{
    analogWrite(MotorL_PWML, 255);
    analogWrite(MotorR_PWMR, 150);
    digitalWrite(MotorL_I1, LOW);
    digitalWrite(MotorL_I2, HIGH);
    digitalWrite(MotorR_I3, HIGH);
    digitalWrite(MotorR_I4, LOW);
    delay(280);
    analogWrite(MotorL_PWML, 100);
    analogWrite(MotorR_PWMR, 100);
    while(digitalRead(M) != 1);
    digitalWrite(MotorL_PWML, LOW);
    digitalWrite(MotorR_PWMR, LOW);
    do_ADVANCE();
}
void do_U_TURN(){
    analogWrite(MotorL_PWML, 255);
    analogWrite(MotorR_PWMR, 150);
    digitalWrite(MotorL_I1, LOW);
    digitalWrite(MotorL_I2, HIGH);
    digitalWrite(MotorR_I3, HIGH);
    digitalWrite(MotorR_I4, LOW);
    delay(500);
    analogWrite(MotorL_PWML, 100);
    analogWrite(MotorR_PWMR, 100);
    while(digitalRead(M) != 1);
    digitalWrite(MotorL_PWML, LOW);
    digitalWrite(MotorR_PWMR, LOW);
    do_ADVANCE();
}

void do_HALT()
{
    digitalWrite(MotorL_PWML, LOW);
    digitalWrite(MotorR_PWMR, LOW);
    delay(10000);
}
void do_command(BT_CMD cmd)
{
    if (cmd == 1)
    {
        do_ADVANCE();
    }
    if (cmd == 2)
    {
        do_U_TURN();
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
