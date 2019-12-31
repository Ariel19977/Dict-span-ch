import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
if __name__ == "__main__":
    fr = open("result_span_zh _1_chin.txt", 'r', encoding='utf-8')
    fr1 = open("result_span_zh _1_span.txt", 'r', encoding='utf-8')
    arrayOLines = fr.readlines()
    array1Lines = fr1.readlines()
    len_array = len(arrayOLines)
    len1_array = len(array1Lines)
    arrayOLines[0] = arrayOLines[0].lstrip('\ufeff')

    result_list = []
    for i, j in zip(range(len_array), range(len1_array)):
        arrayOLines[i] = arrayOLines[i].strip()
        array1Lines[j] = array1Lines[j].strip()
        temp = []
        temp.append(arrayOLines[i])
        temp.append(array1Lines[j])
        result_list.append(temp)
    fr.close()
    fr1.close()
    #去重
    result_list = list(set([tuple(t) for t in result_list]))
    result_list = [list(v) for v in result_list]
    #排序
    result_list = sorted(result_list, key=lambda result: result[0])
    print(result_list)
    fw = open("result_span_zh _sort_set.txt", 'a', encoding="utf-8")
    for list in result_list:
        for l in list:
            fw.write(l)
            fw.write("\n")
        fw.write("\n")
    fw.close()

