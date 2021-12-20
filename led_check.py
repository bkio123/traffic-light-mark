import matplotlib.pyplot as plt
import cv2

def light_check(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    rtn, img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

    print(img.shape)

    # cv2.imshow('win',img)
    #
    # cv2.waitKey()

    print(img.shape, type(img))

    height = img.shape[0]
    width = img.shape[1]

    total = img.sum()
    ration_total =  (total / (width * height * 255)) * 100
    if ration_total < 0.2:
        return 4

    print(f'total = {total}, ration toral = {ration_total}')

    sum = img.sum(axis=0)
    print(sum.shape)

    range1 = int(width / 3)
    range2 = int(width / 3 * 2)

    sum1 = sum[:range1]
    sum2 = sum[range1:range2]
    sum3 = sum[range2:]

    print(sum1.shape, sum2.shape, sum3.shape)
    print(sum1.sum(), sum2.sum(), sum3.sum())
    print(sum1.sum()/total, sum2.sum()/total, sum3.sum()/total)

    r1 = sum1.sum() / total
    r2 = sum2.sum() / total
    r3 = sum3.sum() / total

    rlist = [r1,r2,r3]

    for i, v in enumerate(rlist):
        if v > 0.4:
            return i

    return 4

img = cv2.imread('imgs/04.jpg')
val = light_check(img)
print('return value {:03}'.format(val))
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

