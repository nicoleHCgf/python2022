# This background is given to you.
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# Draw the rainbow using circles and gradients.
### Place Your Code Here ###
Circle (200, 300, 200, fill=gradient('white','red','white', start='bottom'))
Circle (200, 300, 170, fill=gradient('white','orange','white', start='bottom'))
Circle (200, 300, 140, fill=gradient('white','yellow','white', start='bottom'))
Circle (200, 300, 110, fill=gradient('white','green','white', start='bottom'))
Circle (200, 300, 80, fill=gradient('white','blue','white', start='bottom'))
Circle (200, 300, 50, fill=gradient('white','indigo','white', start='bottom'))
Circle (200, 300, 20, fill=gradient('white','violet','white', start='bottom'))
# Now draw grass that covers the bottom half of the circles.
### Place Your Code Here ###
Rect(0, 300, 400, 100, fill=gradient('limeGreen','forestGreen', start='top'))
