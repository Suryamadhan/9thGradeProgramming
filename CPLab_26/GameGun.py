"""======================================
Lab_26.1        Game Gun
---------
Object class for the Game Gun lab
========================================"""


class GameGun:
    def __init__(self):
        self.bulletCount = 100
        self.shotCount = 0
        self.clipSize = 16
        self.clip = []

        for i in range(0, self.clipSize):
            self.clip.append("[]")
    def resetClip(self):
        for i in range(0, self.clipSize):
            self.clip[i] = "[]"

    def shoot(self):
        if self.shotCount > 0:
            self.clip[self.shotCount-1] = "[]"
            self.shotCount -=1
            return "Boom!!!"
        else:
            return "Reload"

    def reload(self):
        if self.bulletCount >= self.clipSize:
            self.bulletCount -= self.clipSize
            self.shotCount = self.clipSize
        else:
            self.shotCount = self.bulletCount
            self.bulletCount = 0

        self.resetClip()

        for i in range(0, self.shotCount):
            self.clip[i] = "*"
    def getBulletCount(self):
        return self.bulletCount

    def getShotCount(self):
        return self.shotCount

    def __str__(self):
        return  "Bullets: " + str(self.bulletCount) +  \
                "\nClip: " + str(self.clip)

    """
    =========================================
    Constructor()....
        variable bulletCount: set to 100
        variable shotCount: set to 0
        variable clipSize: set to 16
        declare list clip

        for loop: from 0 to clipSize
            add "[]" to the list
    =========================================
    """


    """
    ============================================
    resetClip()...

        for loop: from 0 to clipSize
            set clip @ i to "[]"
    ===========================================
    """

	

    """
    ===============================================
    shoot()....

        if shotCount is greater than 0...
            set clip @ shotCount - 1 to "[]"
            subtract 1 from shotCount
            return "Boom!!!"

        otherwise...
            return "Reload!!!"
    ==============================================
    """


    """
    =====================================================
    reload()...

        if bulletCount is greater than or equal to clipSize
            subtract clipSize from bulletCount
            set shotCount to clipSize

        otherwise...
            set shotCount to bulletCount
            set bulletCount = 0

        run resetClip()

        for loop: from 0 to shotCount
            set clip @ i = "*"
    ========================================================
    """


    """
    =======================
    getBulletCount()...
        return bulletCount
    =======================
    """


    """
    ===========================
    getShotCount()...
        return shotCount
    ===========================
    """

	

    """
    ====================================================
    __str__()...
        return "Bullets:    " + bulletCount
               "Clip:       " + a printout of the clip

    Example:
    --------
    Bullets:	100
    Clip:	    [][][][][][][][][][][][][][][][]
    ======================================================
    """

