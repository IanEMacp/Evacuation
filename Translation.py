#a word-for-word, so to speak, translation of "The Cry Wolf Effect" into Python.
import random

#save me from typing random.randint 60000 times
#all probabilities ought to be positive integers, not .xx
def Chance():
    return random.randint(0,100)

#the actual state of nature
def Emergency(emergencyChance):
    x = Chance()
    if x>emergencyChance:
        return false
    return true

#in the paper nature is a lowercase omega, and accuracy is tau
def AlarmCall(eChance, accuracy):
    nature = Emergency(eChance)
    x = Chance()
    if x<accuracy:
        return nature
    return not nature

#this is wrong. I know that to be true, but I can't figure out what
#the paper actually meant.
def AuthorityBelief(prior, aAccurate):
    return (prior*aAccurate)/(prior*aAccurate+(1-prior)(1-aAccurate))

#alarm is X and accuracy is tau
def AuthorityDecision(alarm, alarmAccurate, stratN, stratT,prior):
    probabilityOrder = stratN*((1-prior)*alarmAccurate+prior*(1-alarmAccurate))+stratT*((1-prior)*(1-alarmAccurate)+prior*alarmAccurate)
    if chance()<probabilityOrder:
        return true
    return false

def EvacueeBelief(aAction,pOrder,aAccurate,prior):
    pAlarm = (1-prior)(1-aAccurate)+prior*aAccurate
    aBelief = AuthorityBelief(prior,aAccurate)
    if pOrder>pAlarm:
        return (1-aBelief)+(prior*(1-prior)*(2*aAccurate-1))/((1-pAlarm)*pOrder)
    return aBelief

#the evacuee's strategy is just how likely they are to actually believe
#the authority when it calls the alarm.
def EvacueeDecision(aAction,pOrder,aAccurate,prior):
    if aAction and Chance()<EvacueeBelief(aAction,pOrder,aAccurate,prior):
            return true
    return false

#these payoffs have so many parameters... save me
#how are we going to learn anything from this?
def AuthorityPayoff(state, aAction, eAction):
    if state:
        if aAction:
            if eAction:
                return 0-risk*deadDependent-lostWork-serviceFee
            return 0-deadDependent-serviceFee
        return 0-deadDependent
    if aAction:
        if eAction:
            return 0-lostWork-serviceFee
        return 0-serviceFee
    return 0

def EvacueePayoff(state,eAction):
    if state:
        if eAction:
            return 0-risk*death-exitCost
        return 0-death
    if eAction:
        return 0-exitCost
    return 0
            
            
