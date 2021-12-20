import matplotlib.pyplot as plt
import cv2
import torch
import sys

class cs_light_mark(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def light_check(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        rtn, img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

        # print(img.shape, type(img))

        height = img.shape[0]
        width = img.shape[1]

        total = img.sum()
        ration_total =  (total / (width * height * 255)) * 100
        if ration_total < 2: # under 2% area
            return 3

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

        max_val = max(rlist)
        index = rlist.index(max_val)

        return index


    def forward(self, x):
        out = self.light_check(x)
        return out


if __name__ == "__main__" : 

    model = cs_light_mark()
    print(model)

    torch.save(model,'model.pt')

