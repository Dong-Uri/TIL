from math import ceil, log2, gcd


class SegmentTreeLazy:
    def __init__(self, input_list, calculation_method='sum'):
        self.level = 0
        self.length = 0
        self.input_list = input_list
        self.input_list_length = len(input_list)
        self.input_start_index = 0
        self.tree_index = 1
        self.input_end_index = self.input_list_length - 1
        self.calculation_method = calculation_method
        self.result_list = []
        self.lazy_check_list = []
        self.lazy_value_list = []
        self.default_value = None

    def method(self, left_result, right_result):
        if self.calculation_method == 'sum':
            return left_result + right_result
        elif self.calculation_method == 'max':
            return max(left_result, right_result)
        elif self.calculation_method == 'gcd':
            return gcd(left_result, right_result)

    def range_node(self, update_value, update_range):
        if self.calculation_method == 'sum':
            return update_value * update_range

        return update_value

    def push_down(self, update_value, tree_index, input_start_index, input_end_index):
        if input_start_index == input_end_index:
            self.result_list[tree_index] = update_value
            return self.result_list[tree_index]

        self.lazy_check_list[tree_index] = True
        self.lazy_value_list[tree_index] = update_value

        self.result_list[tree_index] = self.range_node(update_value, input_end_index - input_start_index + 1)

        return self.result_list[tree_index]

    def update_process(self, update_start_index, update_end_index, update_value, input_start_index, input_end_index, tree_index):
        if update_end_index < input_start_index or update_start_index > input_end_index:
            return self.result_list[tree_index]

        if input_start_index == input_end_index:
            self.result_list[tree_index] = update_value

            return self.result_list[tree_index]

        if update_start_index <= input_start_index and input_end_index <= update_end_index:
            self.lazy_check_list[tree_index] = True
            self.lazy_value_list[tree_index] = update_value

            self.result_list[tree_index] = self.range_node(update_value, input_end_index - input_start_index + 1)

            return self.result_list[tree_index]

        input_mid_index = (input_start_index + input_end_index) // 2

        if self.lazy_check_list[tree_index]:
            self.lazy_check_list[tree_index] = False

            self.push_down(self.lazy_value_list[tree_index], tree_index * 2, input_start_index, input_mid_index)
            self.push_down(self.lazy_value_list[tree_index], tree_index * 2 + 1, input_mid_index + 1, input_end_index)
            self.lazy_value_list[tree_index] = self.default_value

        left_result = self.update_process(update_start_index, update_end_index, update_value, input_start_index, input_mid_index, tree_index * 2)

        right_result = self.update_process(update_start_index, update_end_index, update_value, input_mid_index + 1, input_end_index, tree_index * 2 + 1)

        self.result_list[tree_index] = self.method(left_result, right_result)

        return self.result_list[tree_index]

    def update_range(self, update_start_index, update_end_index, update_value):
        self.tree_index = 1

        for update_index in range(update_start_index, update_end_index + 1):
            self.input_list[update_index] = update_value

        self.update_process(update_start_index, update_end_index, update_value, self.input_start_index, self.input_end_index, self.tree_index)

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
        if self.calculation_method == 'sum':
            self.default_value = 0
        elif self.calculation_method == 'max':
            self.default_value = -1
        elif self.calculation_method == 'gcd':
            self.default_value = 1

        self.level = ceil(log2(self.input_list_length)) + 1
        self.length = pow(2, self.level)
        self.result_list = [0] * self.length
        self.lazy_check_list = [False] * self.length
        self.lazy_value_list = [self.default_value] * self.length

        self.process(0, self.input_list_length-1, 1)


def main():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    segment_tree_sum = SegmentTreeLazy(number_list, 'sum')
    segment_tree_sum.make()
    print(segment_tree_sum.result_list)

    segment_tree_sum.update_range(2, 7, 5)
    print(segment_tree_sum.result_list)

    print('new')
    segment_tree_sum.update_range(2, 5, 6)
    print(segment_tree_sum.result_list)



if __name__ == '__main__':
    main()
