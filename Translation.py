#a word-for-word, so to speak, translation of "The Cry Wolf Effect" into Python.
import random

#save me from typing random.randint 60000 times
#all probabilities ought to be positive integers, not .xx
def chance():
    return random.randint(0,100)

#the actual state of nature
def emergency(emergency_chance):
    x = chance()
    if x>emergency_chance:
        return false
    return true

#in the paper nature is a lowercase omega, and accuracy is tau
def alarmCall(emergency_chance, accuracy):
    nature = emergency(emergency_chance)
    x = chance()
    if x<accuracy:
        return nature
    return not nature

#this is wrong. I know that to be true, but I can't figure out what
#the paper actually meant.
def authorityBelief(prior, signal_accuracy):
    return (prior*signal_accuracy)/(prior*signal_accuracy+(1-prior)(1-signal_accuracy))

#alarm is X and accuracy is tau
def authorityDecision(alarm, alarm_accurate, stratN, stratT, prior):
    probability_order = stratN * ((1 - prior) * alarm_accurate + prior * (1 - alarm_accurate)) + stratT * ((1 - prior) * (1 - alarm_accurate) + prior * alarm_accurate)
    if chance()<probabilityOrder:
        return true
    return false

def evacuee_belief(aAction, pOrder, alarm_accurate, prior):
    pAlarm = (1 - prior)(1 - alarm_accurate) + prior * alarm_accurate
    aBelief = authority_belief(prior, alarm_accurate)
    if pOrder > pAlarm:
        return (1 - aBelief) + (prior * (1 - prior) * (2 * alarm_accurate - 1)) / (( 1 - pAlarm) * pOrder)
    return aBelief

#the evacuee's strategy is just how likely they are to actually believe
#the authority when it calls the alarm.
def evacuee_decision(aAction, pOrder, alarm_accurate, prior):
    if aAction and chance() < EvacueeBelief(aAction, pOrder, alarm_accurate, prior):
            return true
    return false

#these payoffs have so many parameters... save me
#how are we going to learn anything from this?
def authority_payoff(state, aAction, eAction):
    if state:
        if aAction:
            if eAction:
                return 0 - risk * deadDependent - lostWork - serviceFee
            return 0 - deadDependent - serviceFee
        return 0 - deadDependent
    if aAction:
        if eAction:
            return 0 - lostWork - serviceFee
        return 0 - serviceFee
    return 0

def evacuee_payoff(state, eAction):
    if state:
        if eAction:
            return 0 - risk * death - exitCost
        return 0 - death
    if eAction:
        return 0 - exitCost
    return 0
            
            
