def main():
    display_main_menu()
    user_inputnum = get_user_input()
    print(user_inputnum)
    print("Average : ",calc_average(user_inputnum))
    print("Min and Max : ", find_min_max(user_inputnum))
    print("Sorted : ", sort_num(user_inputnum))
    print("Median : ", calc_median_num(user_inputnum))
def display_main_menu():
    print("Enter some numbers separated by commas (E.g. 5,67,99)")
def get_user_input():
    user_input = input()
    user_input_list = user_input.split(",")
    user_inputnum = [float(x) for x in user_input_list]
    return user_inputnum
def calc_average(user_inputnum):
    total = 0
    for i in user_inputnum:
        total += float(i)
    average = total/len(user_inputnum)
    return average

def find_min_max(user_inputnum):
    min_num = min(user_inputnum)
    max_num = max(user_inputnum)
    min_max = [min_num,max_num]
    return min_max

def sort_num(user_inputnum):
    return sorted(user_inputnum)

def calc_median_num(user_inputnum):
    user_inputnum = sorted(user_inputnum)
    if len(user_inputnum) % 2 == 1:
        median = user_inputnum[int((len(user_inputnum)-1)/2)]
    else:
        median = int(float(user_inputnum[int(len(user_inputnum)/2)]) + float(user_inputnum[int(len(user_inputnum)/2-1)]))/2
    return median

if __name__ == "__main__":
    main()