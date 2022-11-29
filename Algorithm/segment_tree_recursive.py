from math import log2, ceil, gcd


class SegmentTree:
    def __init__(self, input_list, calculation_method='sum'):
        self.level = 0
        self.length = 0
        self.input_list = input_list
        self.input_list_length = len(self.input_list)
        self.input_start_index = 0
        self.tree_index = 1
        self.input_end_index = self.input_list_length - 1
        self.calculation_method = calculation_method
        self.result_list = []

    def method(self, left_result, right_result):
        if self.calculation_method == 'sum':
            return left_result + right_result
        elif self.calculation_method == 'max':
            return max(left_result, right_result)
        elif self.calculation_method == 'gcd':
            return gcd(left_result, right_result)

    def update_process(self, input_start_index, input_end_index, tree_index, update_index, update_value):
        # 구간에 영향을 미치지 않는 경우.
        if update_index < input_start_index or update_index > input_end_index:
            return self.result_list[tree_index]

        # 업데이트하고자하는 위치에 도달한 경우.
        if input_start_index == input_end_index:
            self.result_list[tree_index] = update_value
            return self.result_list[tree_index]

        input_mid_index = (input_start_index + input_end_index) // 2

        left_result = self.update_process(input_start_index, input_mid_index, tree_index * 2, update_index, update_value)

        right_result = self.update_process(input_mid_index + 1, input_end_index, tree_index * 2 + 1, update_index, update_value)

        self.result_list[tree_index] = self.method(left_result, right_result)

        return self.result_list[tree_index]

    def update(self, update_index, update_value):
        self.tree_index = 1
        self.input_list[update_index] = update_value

        self.update_process(self.input_start_index, self.input_end_index, self.tree_index, update_index, update_value)

    def get_range_process(self, input_start_index, input_end_index, tree_index, range_start_index, range_end_index):
        if input_end_index < range_start_index or input_start_index > range_end_index:
            return 0

        if input_start_index >= range_start_index and input_end_index <= range_end_index:
            return self.result_list[tree_index]

        input_mid_index = (input_start_index + input_end_index) // 2

        left_result = self.get_range_process(input_start_index, input_mid_index, tree_index * 2, range_start_index, range_end_index)

        right_result = self.get_range_process(input_mid_index + 1, input_end_index, tree_index * 2 + 1, range_start_index, range_end_index)

        return self.method(left_result, right_result)

    def get_range(self, range_start_index, range_end_index):
        self.tree_index = 1
        return self.get_range_process(self.input_start_index, self.input_end_index, self.tree_index, range_start_index, range_end_index)

    def process(self, input_start_index, input_end_index, tree_index):
        if input_start_index == input_end_index:
            self.result_list[tree_index] = self.input_list[input_start_index]
            return self.result_list[tree_index]

        input_mid_index = (input_start_index + input_end_index) // 2

        left_result = self.process(input_start_index, input_mid_index, tree_index * 2)

        right_result = self.process(input_mid_index + 1, input_end_index, tree_index * 2 + 1)

        self.result_list[tree_index] = self.method(left_result, right_result)

        return self.result_list[tree_index]

    def make(self):
        self.level = ceil(log2(self.input_list_length)) + 1
        self.length = pow(2, self.level)
        self.result_list = [0] * self.length
        self.process(0, self.input_list_length-1, 1)


def main():
    #number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_list = [1, 2, 5, 5, 5, 5, 5, 5, 9, 10]

    segment_tree_sum = SegmentTree(number_list, 'sum')
    segment_tree_sum.make()
    print(segment_tree_sum.result_list)
    print(segment_tree_sum.get_range(3, 5))
    segment_tree_sum.update(4, 7)
    print(segment_tree_sum.result_list)
    print(segment_tree_sum.get_range(3, 5))

    segment_tree_max = SegmentTree(number_list, 'max')
    segment_tree_max.make()
    print(segment_tree_max.result_list)
    print(segment_tree_max.get_range(3, 5))
    segment_tree_max.update(4, 7)
    print(segment_tree_max.result_list)
    print(segment_tree_max.get_range(3, 5))

    segment_tree_gcd = SegmentTree(number_list, 'gcd')
    segment_tree_gcd.make()
    print(segment_tree_gcd.result_list)
    print(segment_tree_gcd.get_range(3, 5))
    segment_tree_gcd.update(4, 7)
    print(segment_tree_gcd.result_list)
    print(segment_tree_gcd.get_range(3, 5))


if __name__ == '__main__':
    main()