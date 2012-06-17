#! /usr/bin/python2

#config
schemeName = "wood"
bgImgWhite = "../images/woodenboard_white.jpg"
bgImgBlack = "../images/woodenboard_black.jpg"

# adv. config
squareSize = 64 # width of a square in pixel

#code
print "body." + schemeName + " #GameBoard td.whiteSquare, body." + schemeName + " #GameBoard td.highlightWhiteSquare, body." + schemeName + " div.lcs.white, #top div.lcs.white." + schemeName + " { background: url(../images/woodenboard_white.jpg) no-repeat; }";
print "body." + schemeName + " #GameBoard td.blackSquare, body." + schemeName + " #GameBoard td.highlightBlackSquare, body." + schemeName + " div.lcs.black, #top div.lcs.black." + schemeName + ", body." + schemeName + " a.toggle_theme { background: url(../images/woodenboard_black.jpg) no-repeat; }";
white = True
for y in range(0,8):
  for x in range (0, 8):
    if white:
      img = bgImgWhite
    else:
      img = bgImgBlack
    print "body." + schemeName + " #GameBoard #tcol"+str(x)+"trow"+str(y)+", body." + schemeName + " #"+str(chr(ord('a') + x))+str(8-y) + " { background-position: "+str((-x)*squareSize)+"px " +str((-y)*squareSize) +"px; }";
    white = not white
  white = not white
