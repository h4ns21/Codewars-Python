# First method
def hero(bullets, dragons):
    if dragons*2 > bullets:
        return False
    else:
        return True
      
# Second method
def hero(bullets, dragons):
    return dragons * 2 <= bullets
