#a word-for-word, so to speak, translation of "The Cry Wolf Effect" into Python.
import random

#save me from typing random.randint 60000 times
#all probabilities ought to be positive integers, not .xx
def chance():
    return random.uniform(0,1)

#the actual state of nature
def emergency(emergency_chance):
    x = chance()
    if x>emergency_chance:
        return False
    return True

#in the paper nature is a lowercase omega, and accuracy is tau
def alarmCall(nature, accuracy):
    x = chance()
    if x < accuracy:
        return nature
    return not nature

#this is wrong. I know that to be true, but I can't figure out what
#the paper actually meant.
#it's not actually used anywhere so /shrug
def authorityBelief(prior, signal_accuracy):
    return (prior*signal_accuracy)/(prior*signal_accuracy+(1-prior)*(1-signal_accuracy))

#alarm is X and accuracy is tau
def authorityDecision(alarm, alarm_accurate, stratN, stratT, prior):
    probability_order = stratN * ((1 - prior) * alarm_accurate + prior * (1 - alarm_accurate)) + stratT * ((1 - prior) * (1 - alarm_accurate) + prior * alarm_accurate)
    if chance() < probability_order:
        return True
    return False

def evacuee_belief(aAction, pOrder, alarm_accurate, prior):
    pAlarm = (1 - prior)*(1 - alarm_accurate) + prior * alarm_accurate
    aBelief = authorityBelief(prior, alarm_accurate)
    if pOrder > pAlarm:
        return (1 - aBelief) + (prior * (1 - prior) * (2 * alarm_accurate - 1)) / (( 1 - pAlarm) * pOrder)
    return aBelief

#the evacuee's strategy is just how likely they are to actually believe
#the authority when it calls the alarm.
def evacuee_decision(aAction, pOrder, alarm_accurate, prior):
    if aAction and chance() < evacuee_belief(aAction, pOrder, alarm_accurate, prior):
            return True
    return False

#these payoffs have so many parameters... save me
#how are we going to learn anything from this?
def authority_payoff(state, aAction, eAction):
    risk = 0.25
    deadDependent = 5
    lostWork = 3
    serviceFee = 1
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
    risk = .25
    death = 10
    exitCost = 2
    if state:
        if eAction:
            return 0 - risk * death - exitCost
        return 0 - death
    if eAction:
        return 0 - exitCost
    return 0

def randStrategyState():
    if random.randint(1,3) == 1:
        return "More Alarms"
    elif random.randint(1,3) == 2:
        return "50-50"
    elif random.randint(1,3) == 3:
        return "Less Alarms"

def strategySelection(strategyPrompt):
    strategy = input(strategyPrompt)
    if strategy == "More Alarms":
        strategyOrder = .8
        strategyDont = .2
    elif strategy == "50-50":
        strategyOrder = .5
        strategyDont = .5
    elif strategy == "Less Alarms":
        strategyOrder = .2
        strategyDont = .8
    return([strategyOrder, strategyDont])

def main(eChance = .4, accuracy = .9):
    strategySelected = strategySelection("Enter selected strategy(More Alarms,)")
    nature = emergency(eChance)
    alarm = alarmCall(nature, accuracy)
    strategyOrder = strategySelected[0]
    strategyDont = strategySelected[1]
    if chance() < .3:
        prior = True
    else:
        prior = False
    order = authorityDecision(alarm, accuracy, strategyDont, strategyOrder, prior)
    leave = evacuee_decision(order, strategyDont, accuracy, prior) #not sure if strategyDont is actually what I want there
    print("Threat: " + str(nature))
    print("Evacuation Order: " + str(order))
    print("Exit Attempt: " + str(leave))
    print("Evacuee Payoff: " + str(evacuee_payoff(nature, leave)))
    print("Authority Payoff: " + str(authority_payoff(nature, order, leave)))

main()
