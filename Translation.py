#a word-for-word, so to speak, translation of "The Cry Wolf Effect" into Python.
import random

#the actual state of nature
def Emergency(emergencyChance):
    x = random.randint(0,100)
    if x>emergencyChance:
        return false
    return true

#in the paper nature is a lowercase omega, and accuracy is tau
def AlarmCall(nature, accuracy):
    x = random.randint(0,100)
    if x<accuracy:
        return nature
    return not nature

#alarm is X and accuracy is tau
def AuthorityDecision(alarm, alarmAccurate):
    #needs prior belief
    probabilityOrder = stratN*((1-prior)*alarmAccurate+prior*(1-alarmAccurate))+stratT*((1-prior)*(1-alarmAccurate)+prior*alarmAccurate)
    
