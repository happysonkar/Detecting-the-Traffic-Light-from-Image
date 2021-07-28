# import the required packages
import xml.etree.cElementTree as ET
import cv2

# LOADING THE IMAGES
img_1=cv2.imread("36930.png") 
img_2=cv2.imread("51638.png")
img_3=cv2.imread("71062.png")
img_4=cv2.imread("74482.png")
img_5=cv2.imread("75940.jpg")

# fUNCTION TO GET TRAFFIC LIGHTS
def get_traffic_lights(img,xml_file):
    # Initialize the List and variables
    bbox=[]
    color=[]
    count=0
    mytree=ET.ElementTree(file=xml_file)
    # Get the ROOT element
    myroot=mytree.getroot()   
    #print(myroot)
    for chd in myroot:
        if chd.tag=='object':
            for attr in chd:
                if attr.tag=='name':
                    #print(attr.text)
                    color.append(attr.text)
                if attr.tag=='bndbox':
                    for box in attr:
                        if (box.tag=='xmin' or 'ymin' or 'xmax' or 'ymax'):
                            a=int(float(box.text))
                            bbox.append(a)                    
                        if len(bbox)==4:
                            #print(bbox)
                            #print(color)
                            #PUT the color Name of traffic light 
                            cv2.putText(img, color[count], (bbox[0],bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),1)
                            #Draw the rectangle around traffic light
                            cv2.rectangle(img, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (0,255,0),2)
                            bbox=[]
                            count+=1                 
    return img                  

#Calling the Function
img1=get_traffic_lights(img_1,'36930.xml')
img2=get_traffic_lights(img_2,'51638.xml')
img3=get_traffic_lights(img_3,'71062.xml')
img4=get_traffic_lights(img_4,'74482.xml')
img5=get_traffic_lights(img_5,'75940.xml')

# Output the Image
cv2.imshow("Output", img1)
cv2.imshow("Output1", img2)
cv2.imshow("Output2", img3)
cv2.imshow("Output3", img4)
cv2.imshow("Output4", img5)

cv2.waitKey(0)
# save the output image
cv2.imwrite('Output1.png',img1)
cv2.imwrite('Output2.png',img2)
cv2.imwrite('Output3.png',img3)
cv2.imwrite('Output4.png',img4)
cv2.imwrite('Output5.png',img5)

        