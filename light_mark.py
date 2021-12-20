import matplotlib.pyplot as plt
import cv2
import torch

class cs_light_mark(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def light_check(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

        print(img.shape, type(img))

        height = img.shape[0]
        width = img.shape[1]

        total = img.sum()

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

    def forward(self, x):
        out = self.light_check(x)
        return out

if __name__ == "__main__" : 

    img = cv2.imread('imgs/02.jpg')
    model = cs_light_mark()

    out = model(img)
    print(out)

    # torch.save(model,'model.pt')

    # print('return value {:03}'.format(val))
    # plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    # plt.show()

