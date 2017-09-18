"""====================================================
Lab_26.2        Game Health
---------
This will be the object class for the Game Health lab
======================================================="""

class GameHealth:
    def __init__(self):
        self.health = []
        self.healthCount = 6
        self.healthLoad = 6

        for i in range(0,self.healthLoad):
            self.health.append("@")

    def resetHealth(self):
        for i in range(0, self.healthLoad):
            self.health[i] = "@"

    def takeDamage(self, dmg, amt):
        if dmg == 1:
            self.healthCount -= amt
            return "Taking " + str(amt) + " damage!"
        else:
            if self.healthCount + amt < self.healthLoad:
                self.healthCount += amt
            else:
                self.healthCount = self.healthLoad
            return "Power up " + str(amt) + "!"

    def getHealthCount(self):
        return self.healthCount

    def __str__(self):
        output = "Health: "
        for i in range(0, self.healthLoad):
            if i < self.healthCount:
                self.health[i] = "@"
            else:
                self.health[i] = "[]"
            output += self.health[i]
        return output



    """
    ============================================
    Constructor...
        new list called health
        set healthCount and healthLoad to 6

        for loop: from 0 to healthLoad
            add "@" to the health list
    ===========================================
    """

	
    """
    ============================================
    resetHealth()...
        for loop: from 0 to healthLoad
            set health @ i to "@"
    ============================================
    """


    """
    =====================================================
    takeDamage()...
        if dmg is 1
            subtract amt from healthCount
            return "Taking " + amt + " damage!"
        otherwise...
            if healthCount + amt is less than healhtLoad
                add amt to healhtCount

            otherwise...
                set healthCount to healthLoad
            return "Power Up + " + amt + "!"
    =====================================================
    """

	
    """
    ========================
    getHealthCount()...
        return healthCount
    ========================
    """

	

    """
    =======================================
    __str__()...
        set output to "Health: "
        for loop: from 0 to healthLoad
            if i is less than healthCount
                set health[i] to "@"
            otherwise...
                set health @ i to "[]"
            add health @ i to output
        return output
    ========================================
    """

