class FenwickTree:
    def __init__(self, input_list):
        self.input_list = input_list
        self.input_list_length = len(self.input_list)
        self.result_list = [0] * (self.input_list_length + 1)

    def update(self, input_index, input_value):
        while input_index < len(self.result_list):
            self.result_list[input_index] += input_value
            input_index += (input_index & -input_index)

    def get_index_range(self, index):
        result = 0

        while index > 0:
            result += self.result_list[index]
            index -= (index & -index)

        return result

    def get_range(self, range_start_index, range_end_index):
        left_result = self.get_index_range(range_start_index-1)
        right_result = self.get_index_range(range_end_index)

        return right_result - left_result

    def make(self):
        input_index = 1
        for input_value in self.input_list:
            self.update(input_index, input_value)
            input_index += 1


def main():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fenwick_tree_sum = FenwickTree(number_list)
    fenwick_tree_sum.make()
    print(fenwick_tree_sum.result_list)
    print(fenwick_tree_sum.get_range(3, 5))

    fenwick_tree_sum.update(4, 3)
    print(fenwick_tree_sum.result_list)
    print(fenwick_tree_sum.get_range(3, 5))


if __name__ == '__main__':
    main()
