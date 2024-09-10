from manim import *

class Main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFF0"
        array = [1, 4, 2, 3, 1, 2, 5]

        mObjArr = [None] * len(array)

        for i in range(len(array)):
            rect = Rectangle(height=array[i], width=1, stroke_width=1, stroke_color="#231F20")
            text = Text(f"{array[i]}")
            text.set_color("#231F20")
            text.move_to(rect.get_center())
            group = VGroup(rect, text)

            mObjArr[i] = group

        bGroup = VGroup(*mObjArr)
        bGroup.arrange()

        for i in mObjArr:
            i.align_to(bGroup, DOWN)
            self.play(Create(i))

        self.wait(2)

        def isSorted(aTC: list):
            flag = 0
            for i in range(len(aTC) - 1):
                if aTC[i] > aTC[i + 1]:
                    flag = 1

            if flag == 1:
                return False
            else:
                return True

        def highlightGR(obj1: VGroup, obj2: VGroup):
            self.play(obj1[0].animate.set_fill(GREEN_A, opacity=0.7))
            self.play(obj2[0].animate.set_fill(RED_C, opacity=0.7))

        def deHighlight(obj1: VGroup, obj2: VGroup):
            self.play(obj1[0].animate.set_fill("#FFFFF0", opacity=1))
            self.play(obj2[0].animate.set_fill("#FFFFF0", opacity=1))

        def swap(i1, i2, array: list):
            current = array[i1]
            next = array[i2]

            array[i1] = next
            array[i2] = current

        def switchPosition(group1: VGroup, group2: VGroup):
            center1 = group1.get_center()
            center2 = group2.get_center()

            self.play(group1.animate.move_to(center2).align_to(bGroup, DOWN))
            self.play(group2.animate.move_to(center1).align_to(bGroup, DOWN))

        start= 0
        while (isSorted(array) == False):
            smallest = array[start]
            index_to_swap = array.index(smallest)
            for i in range(start, len(array)):
                if array[i] < smallest:
                    smallest = array[i]
                    index_to_swap = i

            highlightGR(mObjArr[index_to_swap], mObjArr[start])
            switchPosition(mObjArr[start], mObjArr[index_to_swap])
            deHighlight(mObjArr[index_to_swap], mObjArr[start])
            swap(start, index_to_swap, array)
            swap(start, index_to_swap, mObjArr)
            start += 1

            print(array)   