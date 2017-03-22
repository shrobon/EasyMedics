1. File Browser   - Done 
2. Separate File for Command Event Functios - Done 
3. File Saving  - Done 
4. Integration with vtk Test Code - Saving with JPEG_Writer Done 
5. Experimenting with filetypes :: using teapot stl
    select reader based on the filetype
6. Radio Button Cube - Done
7. Heart Radio Button - [Done]
    - heart is rendering (fixed about an axis) : Need to  reset camera  [DONE]

Notes: 
- If folder is selected let us assume Volume Rendering (Later use RadioButtons)
- Text and ScrollText for displaying the Logs - [DONE] [Inefficient]

Problems: 
- Problem of overlap if one project is Opened Before another is closed 
- PROBLEM WITH DELETING A COLOR fUNCTION - [SOLVED]


Example color functions:
        '''
        colorFunc.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
        colorFunc.AddRGBPoint(-77, 0.54902, 0.25098, 0.14902)
        colorFunc.AddRGBPoint(94, 0.882353, 0.603922, 0.290196)
        colorFunc.AddRGBPoint(179, 1, 0.937033, 0.954531)
        colorFunc.AddRGBPoint(260, 0.615686, 0, 0)
        colorFunc.AddRGBPoint(3071, 0.827451, 0.658824, 1)
        '''
        '''
        alphaChannelFunc.AddPoint(-3024, 0.0)
        alphaChannelFunc.AddPoint(-77, 0.0)
        alphaChannelFunc.AddPoint(94, 0.29)
        alphaChannelFunc.AddPoint(179, 0.55)
        alphaChannelFunc.AddPoint(260, 0.84)
        alphaChannelFunc.AddPoint(3071, 0.875)
        '''

1. Apply Box-Widget
2. Try Actor.Modified