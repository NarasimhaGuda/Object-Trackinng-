import cv2

def select_tracker():
    print('Select trackeret to be used')
    print('Enter 0 for BOOSTING:')
    print('Enter 1 for MIL:')
    print('Enter 2 for KCF:')
    print('Enter 3 for TLD:')
    print('Enter 4 for MEDIANFLOW:')
    print('Enter 5 for GOTURN:')
    print('Enter 6 for MOSSE:')
    print('Enter 7 for CSRT:')
    
    choice = input('enter the tracker number')
    
    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
        
    if choice =='1':
        tracker = cv2.TrackerMIL_create()
        
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
        
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
        
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
        
    if choice == '5':
        tracker = cv2.TrackerGOTURN_create()
        
    if choice == '6':
        tracker = cv2.TrackerMOSSE_create()
    
    if choice == '7':
        tracker = cv2.TrackerCSRT_create()

    
    return tracker

