import cv2 

frame = cv2.imread("images/frame_0.png")
height, width, _ = frame.shape

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
compiler = cv2.VideoWriter("Wave_Propagation_Video.mp4", fourcc, 20, (width, height))


for index in range(751):
    filename = f"images/frame_{index}.png"
    frame = cv2.imread(filename)
    compiler.write(frame)

compiler.release()
